from setuptools import setup, find_packages

setup(
    name='todo',
    version='0.0.1',
    description='Command line tool to manage To-Do lists',
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
