from setuptools import setup, find_packages

import wordsearch

setup(
    name='wordsearch',
    packages=find_packages(),
    version=wordsearch.__version__,
    url='https://github.com/david-graves/pillar-kata-word-search',
    author='David Graves',
    author_email='graves.230@osu.edu',
    entry_points={
        'console_scripts':[
            'wordsearch = wordsearch:main'
        ]
    }
)
