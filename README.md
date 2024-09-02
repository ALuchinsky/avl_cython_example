In this repository I learn how to create, build, install and deploy python packages that use cython

## Build

From root directory run

    $ python setup.py build_ext --inplace
    $ pip install .

After this you should have package `my_package` installed in your environment. To check this run

    $ ipython
    > import my_package.my_module as mm
    > mm.summ_array([1,2,3, 4])

the result should be

    > np.int64(10)

## Install

You can also install the package from GitHub:

    $  pip install git+https://github.com/ALuchinsky/avl_cython_example.git