from setuptools import setup, find_packages

setup(
    name="helpers",                 # The package name you'll import
    version="0.1.0",                 # Start with 0.1.0
    packages=find_packages(),        # Automatically find all packages
    install_requires=[],             # List dependencies here (if any)
    python_requires=">=3.7",         # Minimum Python version
)
