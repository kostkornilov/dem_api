from setuptools import setup, find_packages

setup(
    name='dem_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'earthengine-api',
        'geemap',
        'matplotlib',
        'gdal',
    ],
    description='API for downloading DEM models from GEE and calculating various indicators.',
    author='Kostya Kornilov',
    author_email='k.kornilov1015@gmail.com',
    url='https://github.com/kostkornilov/dem_api',
)
