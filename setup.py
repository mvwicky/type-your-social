from setuptools import setup

# Package meta-data.
NAME = 'type-in-your-social'
DESCRIPTION = 'Just type in your social security number!'
URL = 'https://typeinyoursocial.com'
EMAIL = 'mvanwickle@gmail.com'
AUTHOR = 'Michael Van Wickle'

# What packages are required for this module to be executed?
REQUIRED = ['Flask', 'Flask-Caching', 'Flask-Compress', 'Flask-SSLify']

setup(
    name=NAME,
    version='0.1.1',
    packages=['social'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
