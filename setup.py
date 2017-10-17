from setuptools import setup, find_packages

setup(
    name='helmetico',
    version="0.1.0",
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'helmetico = helmetico.commands.cli:cli',
    ]},
    description='A AWS Secure Tool')

