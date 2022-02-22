#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='rdrand TRNG',
    version="1.0.0",
    description='Python TRNG',
    author="Wojciech Lawren",
    license="LGPLv3",
    ext_modules=cythonize([
        Extension(
            "_rdrand",
            ["rdrand.pyx", "rdrand/rdrand.c", ],
            include_dirs=[],
            library_dirs=[],
            libraries=[],
            extra_compile_args=[],
            language="C",
        ),
    ]),
    setup_requires=[
        "cython >= 0.29.1",
    ],
    zip_safe=False,
)
