from setuptools import setup, find_packages

setup(
    name='vodapay-support-api-client',
    version='1.0.0',
    description='Python Library for interacting with VodaPay API for m-commerce.',
    author='Mmasehume Raphiri',
    packages=find_packages(),
    install_requires= open("requirements.txt").readlines(),
)
