# coding=utf-8
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='pyoms',
    version='0.0.1',
    description='Python to JavaScript.',
    author='Omelchenko Mihail - DJWOMS',
    author_email='socanime@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'Transcrypt==3.7.1'
    ],
    entry_points = {
        'console_scripts': [
            'build = transcrypt.__main__:main'
        ]
    },
)