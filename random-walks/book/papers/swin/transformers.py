from typing import List, Optional, Callable

import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_probability as tfp
tfk = tf.keras

# Type for random seed
Seed = [tf.Tensor, tf.Tensor]



class SelfAttention(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        projection_dim: int,
        name: str = "self_attention",
        **kwargs,
    ):

        super().__init__(name=name, **kwargs)

        # Split the seed and set up the dense layers
        seed1, seed2 = tfp.random.split_seed(seed, 2)

        self.Uk = tfk.layers.Dense(
            projection_dim,
            activation="gelu",
            use_bias=False,
            kernel_initializer=tf.initializers.GlorotNormal(seed=int(seed1[0])),
        )

        self.Uq = tfk.layers.Dense(
            projection_dim,
            activation="gelu",
            use_bias=False,
            kernel_initializer=tf.initializers.GlorotNormal(seed=int(seed2[0])),
        )


    def self_attention_weights(self, x: tf.Tensor) -> tf.Tensor:
        """
        Compute self-attention weights for tokens in a sequence

        Args:
            x: input sequence of tokens, shape (B, N, D)
        
        Returns:
            attention weights, shape (B, N, N)
        """
        k = self.Uk(x)
        q = self.Uq(x)

        dot_product = tf.matmul(k, q, transpose_b=True)
        dot_product /= tf.math.sqrt(tf.cast(tf.shape(k)[-1], tf.float32))

        return tf.nn.softmax(dot_product, axis=1)
    
    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Apply self-attention to a sequence of tokens

        Args:
            x: input sequence of tokens, shape (B, N, D)

        Returns:
            output sequence of tokens, shape (B, N, D)
        """
        return tf.matmul(self.self_attention_weights(x), x, transpose_a=True)



class MultiHeadSelfAttention(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        token_dim: int,
        projection_dim: int,
        num_heads: int,
        name: str = "multi_head_self_attention",
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)

        keys = tfp.random.split_seed(seed, 2*num_heads)
        self.self_attention = [
            SelfAttention(
                seed=key,
                projection_dim=projection_dim,
            ) for key in keys[::2]
        ]

        self.linear = [
            tfk.layers.Dense(
                token_dim,
                use_bias=False,
                activation=None,
                kernel_initializer=tf.initializers.GlorotNormal(seed=int(key[0])),
            ) for key in keys[1::2]
        ]

    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Apply multi-head self-attention to a sequence of tokens

        Args:
            x: input sequence of tokens, shape (B, N, D)

        Returns:
            output sequence of tokens, shape (B, N, D)
        """
            
        # Compute tokens for each head and apply linear 
        heads = [
            linear(sa(x))
            for sa, linear in zip(self.self_attention, self.linear)
        ]

        # Stack and sum across heads
        return tf.reduce_mean(tf.stack(heads, axis=2), axis=2)



class MLP(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        num_hidden: int,
        num_layers: int,
        num_output: Optional[int] = None,
        name: str = "mlp",
        **kwargs,
    ):

        super().__init__(name=name, **kwargs)

        # Set up output dimensions of linear layers
        out_feats = [num_hidden] * num_layers + [num_output]

        # Split the random key into sub-keys for each layer
        seeds = tfp.random.split_seed(seed, num_layers+1)

        self.linear = [
            tfk.layers.Dense(
                out_feat,
                activation=None,
                kernel_initializer=tf.initializers.GlorotNormal(seed=int(seed[0])),
            )
            for seed, out_feat in zip(seeds, out_feats)
        ]


    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Compute forward pass through the MLP.

        Args:
            x: input tensor of shape (..., feature_dim,)
        
        Returns:
            output tensor of shape (..., feature_dim,)
        """
        for layer in self.linear[:-1]:
            x = layer(x)
            x = tf.nn.gelu(x)
        return self.linear[-1](x)



class TransformerBlock(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        token_dimension: int,
        mlp_num_hidden: int,
        mlp_num_layers: int,
        num_heads: int,
        name: str = "swin_transformer_block",
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)

        key1, key2 = tfp.random.split_seed(seed, 2)
        self.mhsa = MultiHeadSelfAttention(
            seed=key1,
            token_dim=token_dimension,
            projection_dim=token_dimension,
            num_heads=num_heads,
        )

        self.mlp = MLP(
            seed=key2,
            num_hidden=mlp_num_hidden,
            num_layers=mlp_num_layers,
            num_output=token_dimension,
        )

        self.ln1 = tfk.layers.LayerNormalization(axis=2)
        self.ln2 = tfk.layers.LayerNormalization(axis=2)

    
    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Apply the transformer block to input tokens `x`.

        Arguments:
            x: input tensor of shape (B, N, D)

        Returns:
            output tensor of shape (B, N, D)
        """
        x = x + self.mhsa(self.ln1(x))
        x = x + self.mlp(self.ln2(x))

        return x
    


class SwinTransformerBlock(tfk.Model):
    def __init__(
        self,
        seed: Seed,
        token_dimension: int,
        mlp_num_hidden: int,
        mlp_num_layers: int,
        num_heads: int,
        window_size: int,
        name: str = "swin_transformer_block", 
        **kwargs,
    ):

        super().__init__(name=name, **kwargs)

        self.window_size = window_size

        key1, key2, key3 = tfp.random.split_seed(seed, 3)
        self.first_block = TransformerBlock(
            seed=key1,
            token_dimension=token_dimension,
            mlp_num_hidden=mlp_num_hidden,
            mlp_num_layers=mlp_num_layers,
            num_heads=num_heads,
        )

        self.second_block = TransformerBlock(
            seed=key2,
            token_dimension=token_dimension,
            mlp_num_hidden=mlp_num_hidden,
            mlp_num_layers=mlp_num_layers,
            num_heads=num_heads,
        )

        self.linear = tfk.layers.Dense(
            token_dimension,
            activation=None,
            kernel_initializer=tf.initializers.GlorotNormal(seed=int(key3[0])),
        )


    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Apply the Swin Transformer block to input tokens `x`.

        Arguments:
            x: input tensor of shape (B, N, M, D)

        Returns:
            output tensor of shape (B, N, M, D)
        """

        N = tf.shape(x)[1]
        M = tf.shape(x)[2]

        # Reshape patches into shape (B, N//2, M//2, 4*D)
        x = tf.image.extract_patches(
            x,
            sizes=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            rates=[1, 1, 1, 1],
            padding="VALID",
        )

        # Project to obtain shape (B, N//2, M//2, D) and reshape down to (B, N//2 * M//2, D)
        x = self.linear(x)
        x = tf.reshape(x, [tf.shape(x)[0], -1, tf.shape(x)[-1]])
    
        # Apply the first transformer block
        x = self.first_block(x)

        # Shift windows
        x = shift_and_reshape(x, shift=self.window_size, N=N//2, M=M//2)
        x = self.second_block(x)

        # Shift windows back
        x = shift_and_reshape(x, shift=-self.window_size, N=N//2, M=M//2)

        return x
        

def shift_and_reshape(x: tf.Tensor, shift: int, N: int, M: int) -> tf.Tensor:
    """
    Given an input tensor of shape (B, N*M, D), shift the windows
    """
    x = tf.reshape(x, [tf.shape(x)[0], N, M, -1])
    x = shift_horizontally_and_vertically(x, shift)
    return tf.reshape(x, [tf.shape(x)[0], -1, tf.shape(x)[-1]])
    

def shift_horizontally_and_vertically(x: tf.Tensor, shift: int) -> tf.Tensor:
    """
    Shift windows in the input tensor `x` by shift along its width and height.
    For example, using shift == 1 (and neglecting the B and D dimensions),
    the N and M dimensions would change as follows:
    
                      Original                   Shifted
                 -------------------       -------------------
                |  x   x  |  x   o  |     |  o   o  |  o   o  |
                |  x   x  |  x   o  |     |  o   x  |  x   x  |
                |---------|---------| --> |---------|---------|
                |  x   x  |  x   o  |     |  o   x  |  x   x  |
                |  o   o  |  o   o  |     |  o   x  |  x   x  |
                 -------------------       -------------------
    
    Arguments:
        x: input tensor of shape (B, N, M, D)
        shift: amount of shift to apply

    Returns:
        output tensor of shape (B, N, M, D)
    """
    return tf.roll(tf.roll(x, shift, axis=1), shift, axis=2)


class PositionEmbedding(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        token_dimension: int,
        sequence_length: int,
        name: str = "position_embedding",
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)
        
        self.embeddings = tf.Variable(
            tf.random.normal(
                (sequence_length, token_dimension),
                seed=int(seed[0]),
            )
        )

    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Add position embeddings to input tensor.

        Arguments:
            x: input tensor of shape (B, N, D)

        Returns:
            output tensor of shape (B, N, D)
        """
        return x + self.embeddings[None, :, :]



class TinyVisionTransformer(tfk.Model):

    def __init__(
        self,
        seed: Seed,
        tokeniser: Callable,
        embedding: PositionEmbedding,
        token_dimension: int,
        mlp_num_hidden: int,
        mlp_num_layers: int,
        num_heads: int,
        num_blocks: int,
        num_classes: int,
        name: str = "tiny_vision_transformer",
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)

        seeds = tfp.random.split_seed(seed, num_blocks+1)
        self.blocks = [
            TransformerBlock(
                seed=seeds[i],
                token_dimension=token_dimension,
                mlp_num_hidden=mlp_num_hidden,
                mlp_num_layers=mlp_num_layers,
                num_heads=num_heads,
            )
            for i in range(num_blocks)
        ]

        self.final_mlp = MLP(
            seed=seeds[-1],
            num_hidden=mlp_num_hidden,
            num_layers=mlp_num_layers,
            num_output=num_classes,
        )

        self.tokeniser = tokeniser
        self.embedding = embedding
        self.class_token = tf.Variable(
            tf.zeros(
                (1, 1, token_dimension),
                dtype=tf.float32,
            )
        )


    def call(self, x: tf.Tensor) -> tf.Tensor:
        """
        Apply vision transformer to batch of images.

        Arguments:
            x: input image tensor of shape (B, H, W, C)

        Returns:
            output logits tensor of shape (B, num_classes)
        """

        class_token = tf.tile(
            self.class_token,
            [tf.shape(x)[0], 1, 1],
        )

        x = self.tokeniser(x)
        x = self.embedding(x)
        x = tf.concat([class_token, x], axis=1)

        for block in self.blocks:
            x = block(x)

        x = self.final_mlp(x[:, 0, :])
        return x - tf.math.reduce_logsumexp(x, axis=1, keepdims=True)

