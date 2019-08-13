from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
py_depthsampling does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='py_depthsampling',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python functions for visualising fMRI cortical depth sampling results created with CBS tools.",
    long_description=readme,
    author="Ingo Marquardt",
    author_email='',
    url='https://github.com/ingo-m/py_depthsampling',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
    },
    include_package_data=True,
    package_data={
        'py_depthsampling': [
                          'py_depthsampling.boot',
                          'py_depthsampling.crf',
                          'py_depthsampling.drain_model',
                          'py_depthsampling.eccentricity',
                          'py_depthsampling.ert',
                          'py_depthsampling.get_data',
                          'py_depthsampling.main',
                          'py_depthsampling.misc',
                          'py_depthsampling.permutation',
                          'py_depthsampling.plot'
        ]
    },
    install_requires=requirements,
    license="GNU General Public License Version 3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
