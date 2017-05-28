from os import path
from glob import glob
from string import capwords
from setuptools import setup

base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

styles = []
for filename in glob(path.join(base_dir, 'pygments_base16', 'base16-*.py')):
    style = path.splitext(path.basename(filename))[0]
    class_name = '{}Style'.format(capwords(style, '-').replace('-', ''))
    styles.append('{}=pygments_base16:{}'.format(style, class_name))

setup(
    name='pygments-base16',

    version='1.0.1',

    description='Base16 styles for Pygments',
    long_description=long_description,

    url='https://github.com/mohd-akram/base16-pygments',

    author='Mohamed Akram',
    author_email='mohd.akram@outlook.com',

    license='MIT',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],

    keywords='pygments syntax highlighting',

    packages=['pygments_base16'],

    install_requires=['pygments>=2'],

    entry_points={
        'pygments.styles': styles
    }
)
