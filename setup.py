from setuptools import setup, Extension
from Cython.Build import cythonize  

extensions = [
    Extension("my_package.my_module", ["my_package/my_module.pyx"])
]

setup(
    name = "my_package",
    version = "0.0.1",
    packages = ["my_package"],
    ext_modules = cythonize(extensions),
    setup_requires=["Cython"],
    zip_safe = False
)