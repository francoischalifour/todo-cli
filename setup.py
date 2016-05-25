import codecs
import os

from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()


long_description = read('README.md')


setup(
    name='todo',
    version='0.0.1',
    description='Command-line tool to manage To-Do lists',
    long_description=long_description,
    keywords='todo list task productivity project management',
    author='Francois Chalifour',
    author_email='francois.chalifour@gmail.com',
    url='https://github.com/francoischalifour/todo-cli',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    }
)
