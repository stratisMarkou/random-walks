# Script which downloads and preprocesses a collection of UCI datasets.
# Flag --dir specifies the relative path at which the script will work.
# The script creates a directory called "data" under --dir and downloads
# the UCI data there. It then preprocesses the data to a format ready
# to be consumed by the models. By default, this will overwrite an existing
# "data" directory. 
#
# For each dataset, the script creates an x.npy and y.npy array containing
# the model input and outputs under data/dataset_name/.


import os
import shutil
import zipfile
import urllib.request
import argparse
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,  \
                                  StandardScaler, \
                                  OrdinalEncoder, \
                                  Binarizer

from sklearn.utils import as_float_array
from sklearn.pipeline import Pipeline

argparser = argparse.ArgumentParser()
argparser.add_argument("--dir", dest="dir", required=True, type=str)
argparser.add_argument("--no-download", dest='no_download', action="store_true")
args = argparser.parse_args()


# =============================================================================
# Dataset downloader
# =============================================================================


def download_datasets(root_dir, datasets):
    
    # Directory to download data to
    data_dir = root_dir + '/data'
    
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
        
    os.mkdir(data_dir)
    
    # Loop over datasets and download them into tmp
    for dataset_name, info in datasets.items():
        
        print(f'Downloading {dataset_name} dataset')
        os.mkdir(f'{data_dir}/{dataset_name}')
        
        base_url = info['base_url']
        
        # Handle the case where the data must be unzipped
        if info['zipped']:
            
            # Download zip file
            url = f"{base_url}/{info['zipfile']}"
            save_location = f"{data_dir}/{dataset_name}/{info['zipfile']}"
            urllib.request.urlretrieve(url, save_location)
            
            # Unzip data
            with zipfile.ZipFile(save_location, 'r') as zip_handle:
                zip_handle.extractall(save_location[:-4])

        data = []
        for i, file_name in enumerate(info['files']):
            
            save_location = f'{data_dir}/{dataset_name}/{file_name}'

            if not info['zipped']:
                
                url = f"{base_url}/{file_name}"
                urllib.request.urlretrieve(url, save_location)
                
                if ('post-download' in info) and           \
                   (info['post-download'][i] is not None):
                    info['post-download'][i](save_location)

            _data = None
            
            if save_location[-5:] == '.xlsx' or '.xls':
                _data = np.array(pd.read_excel(save_location), dtype=str)
                
            else:
                _data = np.loadtxt(save_location,
                                   dtype=str,
                                   delimiter=info['delimiter'])
                
            _data = _data[1:] if info['drop-header'] else _data

            rows_with_missing = np.any(_data == '?', axis=1)
            print(f'{np.sum(rows_with_missing)}/{rows_with_missing.shape[0]} '
                  f'rows had missing data\n')
                
            if info['remove-missing']:
                _data = _data[~rows_with_missing, :]
                
            data.append(_data)

        data = np.concatenate(data, axis=0)
        np.save(f'{data_dir}/{dataset_name}/data.npy', data)


        
# =============================================================================
# Dataset processor
# =============================================================================


def process_dataset(data_dir, config):
    
    data = None
    try:
        data = np.load(f"{data_dir}/data.npy")
            
    except (FileNotFoundError, OSError):
        print("Missing this dataset! Not processed.")
        return
        
    # Set random seed and shuffle data
    np.random.seed(0)
    data = data[np.random.permutation(data.shape[0])]

    # Scaler for normalising input data
    scaler = StandardScaler()
    
    # Categorical transformer for encoding categorical classes into one hot
    categorical_transformer = OneHotEncoder(sparse=False)

    # Inputs x are all columns except output column
    mask = np.full(data.shape[1], True)
    mask[config["output_column"]] = False
    x = data[:, mask]

    # Preprocessor for scaling
    preprocessor = ColumnTransformer(transformers=[
        ('num', scaler, config["numerical_features"]),
        ('cat', categorical_transformer, config["categorical_features"])
    ])

    x = preprocessor.fit_transform(x)

    y = data[:, config["output_column"]].reshape(-1, 1)
    y = config["output_generator"](y)

    np.save(data_dir + "/x.npy", x)
    np.save(data_dir + "/y.npy", y)
    
    print(f'Input  shape: {x.shape}')
    print(f'Output shape: {y.shape}')

    
def adult_preprocess_test_file(file_location):
    
    fhandle = open('./data/adult/adult.test', 'r')
    content_minus_first_line = '\n'.join(fhandle.read().split('\n')[1:])
    fhandle.close()
    
    fhandle = open('./data/adult/adult.test', 'w')
    fhandle.write(content_minus_first_line)
    fhandle.close()
    
    return


ROOT_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases'

datasets = {
    
    'concrete'       : {'base_url'       : f'{ROOT_URL}/concrete/compressive/',
                        'zipped'         : False,
                        'files'          : ['Concrete_Data.xls'],
                        'delimiter'      : ',',
                        'drop-header'    : True,
                        'remove-missing' : False}
}
    
    
    
# =========================================================================
# Regression datasets
# =========================================================================


# Abalone dataset
def abalone_output_generator(y):
    oe = StandardScaler()
    return oe.fit_transform(y)

abalone_config = {
    "numerical_features"   : [1, 2, 3, 4, 5, 6, 7],
    "categorical_features" : [0],
    "folder"               : "/abalone",
    "output_column"        : 8,
    "output_generator"     : abalone_output_generator
}

# Superconductor dataset
def superconductor_output_generator(y):
    oe = StandardScaler()
    return oe.fit_transform(y)

superconductor_config = {
    "numerical_features"     : list(range(81)),
    "categorical_features"   : [],
    "folder"                 : "/superconductor",
    "output_column"          : 81,
    "output_generator"       : superconductor_output_generator
}

# Protein dataset
def protein_output_generator(y):
    oe = StandardScaler()
    return oe.fit_transform(y)

protein_config = {
    "numerical_features"     : list(range(9)),
    "categorical_features"   : [],
    "folder"                 : "/protein",
    "output_column"          : 9,
    "output_generator"       : protein_output_generator
}

# Power plant dataset
def power_output_generator(y):
    oe = StandardScaler()
    return oe.fit_transform(y)

power_config = {
    "numerical_features"     : list(range(4)),
    "categorical_features"   : [],
    "folder"                 : "/power",
    "output_column"          : 4,
    "output_generator"       : power_output_generator
}


# =========================================================================
# Classification datasets
# =========================================================================

# Adult dataset
def adult_output_generator(y):
    oe = OrdinalEncoder()
    y[y == " <=50K."] = " <=50K"
    y[y == " >50K."] = " >50K"
    return oe.fit_transform(y)

adult_config = {
    "numerical_features"   : [0, 2, 4, 10, 11, 12],
    "categorical_features" : [1, 3, 5, 6, 7, 8, 9, 13],
    "folder"               : "/adult",
    "output_column"        : 14,
    "output_generator"     : adult_output_generator
}

# Mushroom dataset
def mushroom_output_generator(y):
    oe = OrdinalEncoder()
    return oe.fit_transform(y)

mushroom_config = {
    "numerical_features"   : [],
    "categorical_features" : [i for i in range(1, 22)],
    "folder"               : "/mushroom",
    "output_column"        : 0,
    "output_generator"     : mushroom_output_generator
}

# Credit approval dataset
def credit_output_generator(y):
    oe = OrdinalEncoder()
    return oe.fit_transform(y)

credit_config = {
    "numerical_features"   : [1, 2, 7, 10, 13, 14],
    "categorical_features" : [0, 3, 4, 5, 6, 8, 9, 11, 12],
    "folder"               : "/credit",
    "output_column"        : 15,
    "output_generator"     : credit_output_generator
}

# Bank marketing dataset
def bank_output_generator(y):
    oe = OrdinalEncoder()
    return oe.fit_transform(y)

bank_config = {
    "numerical_features"   : [0, 5, 9, 11, 12, 13, 14],
    "categorical_features" : [1, 2, 3, 4, 6, 7, 8, 10, 15],
    "folder"               : "/bank",
    "output_column"        : 16,
    "output_generator"     : bank_output_generator
}

# Concrete marketing dataset
def concrete_output_generator(y):
    oe = OrdinalEncoder()
    return oe.fit_transform(y)

concrete_config = {
    "numerical_features"   : [i for i in range(8)],
    "categorical_features" : [],
    "folder"               : "/concrete",
    "output_column"        : 8,
    "output_generator"     : concrete_output_generator
}



# =========================================================================
# Download and preprocess data
# =========================================================================

if not args.no_download:
    download_datasets(f"{args.dir}/", datasets)


print("Processing abalone dataset")
process_dataset(f"{args.dir}/data/abalone", abalone_config)

print("Processing adult dataset")
process_dataset(f"{args.dir}/data/adult", adult_config)

print("Processing mushroom dataset")
process_dataset(f"{args.dir}/data/mushroom", mushroom_config)

print("Processing credit dataset")
process_dataset(f"{args.dir}/data/credit", credit_config)

print("Processing bank dataset")
process_dataset(f"{args.dir}/data/bank", bank_config)

print("Processing superconductor dataset")
process_dataset(f"{args.dir}/data/superconductor", superconductor_config)

print("Processing protein dataset")
process_dataset(f"{args.dir}/data/protein", protein_config)

print("Processing power dataset")
process_dataset(f"{args.dir}/data/power", power_config)

print("Processing concrete dataset")
process_dataset(f"{args.dir}/data/concrete", concrete_config)