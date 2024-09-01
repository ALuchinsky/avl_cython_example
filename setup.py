import setuptools
from Cython.Build import cythonize
import numpy

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tdavec",
    version="0.0.1",
    author="Aleksei Luchinsky",
    author_email="aluchi@bgsu.edu",
    description="Calculation TDA vectorization summaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ALuchinsky/avl_cython_example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=cythonize([
         'tdavec/func.pyx'
         ],
        annotate=True),
    include_dirs=[numpy.get_include()]
)