from setuptools import setup, find_packages

setup(
    name='opbnos-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
      'requests==2.22.0'
      # Add any required dependencies here
    ],
    author='Harrish Jeyabalu, Vibhitha Nandakumar',
    description='Python SDK to access and manage OPBNOS'
)
