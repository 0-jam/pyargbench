# To build module:
# $ python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('modules/c_funcs.pyx'),
)
