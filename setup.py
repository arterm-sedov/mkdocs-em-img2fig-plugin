# setup.py

import os
from setuptools import setup, find_packages

def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mkdocs-em-img2fig-plugin',
    version='0.2',
    description='A MkDocs plugin that converts markdown encoded images surrounded by two asterisks into <figure> elements.',
	long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown',
    url='https://github.com/arterm-sedov/mkdocs-em-img2fig-plugin',
    author='Arterm Sedov',
	license='MIT',
	python_requires='>=3.9',
    install_requires=[
		'mkdocs'
	],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'em-img2fig = src:Image2FigurePlugin',
        ]
    }
)
