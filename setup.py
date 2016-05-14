import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='todo',
    version='1.0.0',
    description='Command line tool to manage task lists',
    long_description=read('README.md'),
    author='Francois Chalifour',
    author_email='francois.chalifour@gmail.com',
    url='https://github.com/francoischalifour/todo-cli',
    license='MIT',
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    }
)
