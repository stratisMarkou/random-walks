# A tutorial introduction

## Hello world in C

Running the customary hello world programme in C is quite different than in
other languages like Python. C is a compiled language in which programmes must
be compiled before they are executed, in contrast to interpreted languages like
Python which are not compiled but are instead interpreted at runtime.

To print hello world , make a new
file called `hello.c` and write this into it

```
\#include <stdio.h>

main(){
	printf("hello, world\n");
}
```

Then compile it (in a UNIX-based system like Linux or MacOS) by running

```
$ cc hello.c
```

This will create a executable file called `a.out`, which you can execute from
the terminal by running

```
$ ./a.out
```

The name a.out comes from ["assembler output"](https://en.wikipedia.org/wiki/A.out), coined by [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), who apparently used this standard name for the output files of his assembler. This is a bit confusing since C uses a compiler and not an assembler ([what is the difference?](https://cs.stackexchange.com/questions/13904/is-there-any-real-difference-between-a-compiler-and-an-assembler)).

Here's what is happening in this programme
- The `\#include <stdio.h>` line tells the compiler to include the standard
  input/output library, which provides the `printf` function.
- The `main(){...}` is the declaration of a function which takes no arguments, whose insides are contained in the braces. `main` is a special function name in C, and every programme begins by executing at the start of `main`.
- `printf("hello, world\n")` prints the string "hello, world" followed by the
  new-line character - `printf` doesn't leave a new line on its own.

**Exercise 1.1:** Leaving out certain parts of the programme gives different
errors at compilation time. For example, removing the `;` after the function
call gives the compilation error "error: expected ';' after expression".
Another interesting error is if we replace the print statement by `printf(1);`,
then the programme compiles (but gives a warning). When run, this programme
gives a segmentation fault `Segmentation fault: 11`.

**Exercise 1.2:** Replacing the `"\n"` above by other expressions of the form
`"\c"`, where c is some other character, has different effects depending on c.
If c corresponds to one of the known escape seqences (like t), then the string is resolved according to that escape seqence. For other choices of c (like !), the symbol following the `/` is printed, whereas if c was a number the escape sequence was ignored.


## Variables and arithemtic

The following programme prints the conversion table from Fahrenheit to Celcius,
using the formula $^oC = 5 \times (^oF - 32) / 9$ and rounding C down to an
integer:

```
#include <stdio.h>

/* Print the conversion table from Fahrenheit to Celcius */

main(){

	int fahr, celcius;
	int lower, upper, step;
	
	lower = 0;
	upper = 300;
	step = 20;

	fahr = lower;
	while (fahr <= upper){

		celcius = 5 * (fahr - 32)  / 9;
		
		printf("%d\t%d\n", fahr, celcius);
		
		fahr = fahr + step;

	}

}
```
After compiling and running, it prints:
```
0		-17
20		-6
40		4
60		15
80		26
100		37
120		48
140		60
160		71
180		82
200		93
220		104
240		115
260		126
280		137
300		148
```
This program introduces a few fundamental aspects of C.

### Declaration and assignment

In C all variables must be declared before usage, and a variable *declaration*
consists of a **type** (e.g. `int`) and a **name** (e.g. `fahr`). Declarations
of variables of the same type can be made in the same line as above. Variable
can be assigned values through an *assignment* statement like
```
lower = 0;
```
A variable can also be declared and have a value assigned to it, both in the same statement, as in
```
int fahr = 0;
```
is also a valid statement. Once declared, a variable cannot be re-declared so
a programme containing
```
int fahr;
int fahr = 0; 
```
will not compile. Once defined, we are not allowed to re-define `fahr`
again. Important types included in C include

```
char   //character
short  //short integer
long   //long integer
float  //single-precision floating point
double //double-precision floating point
```

and here is a longer list of the [main types of
C](https://en.wikipedia.org/wiki/C_data_types#Basic_types), including their
sizes in bits, the ranges of numbers they can represent and their format
specifiers (the bit that goes after `%` when formatting a string, more of this
in a bit).

Note that a `char` represents a single byte (8 bits, 128 possible values). The ASCII (American Standard Code for Information Interchange), a standard code for some standard
symbols like letters or punctuation, contains exactly 128 elements, so the
`char` is an ideal type for representing ASCII characters. A `char` can be
readily mapped into an `int` and vice versa.

### Arithmetic

In this programme, division by 9 in the expression `5 * (fahr - 32)  / 9 ` evalatues to an integer, because integer division in C truncates the fractional part of the 'true' result - and this is an all-`int` experssion. However, arithmetic expressions between an `int` and a `float`, such as `5 / 9.0`, will automatically convert the `int` to a `float`, so the result will be a `float`. This carries over to expressions with other data types, and assignments like `float myfloat = 0;` will automatically handdle this conversion.

For example, if we define `float fahr = 0`, the experssion `5 * (fahr - 32) / 9` will evaluate to `-17.777...`. That's because at each stage of the expression, the `int` will be converted to a `float` and the computation carried out - leaving us with a float in the end and without any of that integer truncation.

This conversion also goes the other way, from `float` to `int`. This programme
```
main(){

	float myfloat = 3.14159;
	int myint = myfloat;

	printf("%d\n", myint);
}
```
compiles and prints 3.

### String formatting and `printf`

As we saw in the Fahrenheit programme, `printf` command supports string formatting. If we pass a string containing expressions like `%d` or `%f`, followed by as many arguments as `%`-expressions as the string contained, then these expressions will be evaluated to a string representation of those arguments. As with expressions, type conversions are premissible here as well. For a list of formatters of the main types see [this table](https://en.wikipedia.org/wiki/C_data_types#Basic_types).

### While-statement

The while loop `while (fahr <= upper){...}` is executed in the familiar way.
First the condition in the while statement is evaluated and if it's true, then
the contents of the loop are executed once. Then the condition is checked again
and the contents rerun, repeating until the condition is false. **Note that the
condition is only checked after all the contents of the loop have been run.**

### For-statement

## Symbolic constants

One way to keep C code tidy is to move constants to the top of a file using
`define` statements like so:

```
#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP  20

main(){

	int fahr;
	float celcius;

	for (fahr = LOWER; fahr == UPPER; fahr = fahr + STEP){
		
		celcius = (5.0 / 9.0) * (fahr - 32.0);
		
		printf("%3d %6.1f\n", fahr, celcius);
	}	

}
```

