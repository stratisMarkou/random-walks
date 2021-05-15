from distutils.core import setup
from Cython.Build import cythonize

setup(name="fastloop", ext_modules=cythonize('fastloop.pyx'),)