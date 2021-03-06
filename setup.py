# coding=utf-8
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='pyoms',
    packages=['pyoms'],
    version='0.0.5.5',
    description='Python to JavaScript.',
    author='Omelchenko Michail - DJWOMS',
    author_email='socanime@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',

    ],#'Topic :: Text Processing :: Linguistic',
    include_package_data=True,
    zip_safe=False,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'Transcrypt==3.7.11'
    ],
    entry_points={
        'console_scripts': [
            'build = transcrypt.__main__:main'
        ]
    },
)