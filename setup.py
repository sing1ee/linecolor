import os

import setuptools


setuptools.setup(
    name='linecolor',
    version='2017.03.22',
    keywords='command-line-color, colorful output of linux command like tail, cat and ect.',
    description='small tool for colorful output of linux command',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    author='zhangcheng',
    author_email='zh.milo@gmail.com',
    url='https://github.com/sing1ee/linecolor',
    packages=setuptools.find_packages(),
    license='MIT',
	entry_points = {
        'console_scripts': [
            'linecolor = linecolor.cmd:main'
        ]
    }
)
