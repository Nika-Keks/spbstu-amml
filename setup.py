from setuptools import setup, find_packages

setup(
    name='spbstu-amml',
    packages=find_packages(),
    version='1.1.2',
    author='',
    description='modelhub',
    long_description='',
    url='',
    python_requires='>=3.8',
    install_requires=[
        #"tensorflow>=2.10.0",
        "dvc[s3]>=2.27.2",
        "protobuf==3.19.5"
    ]
)