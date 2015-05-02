from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'setuptools',
    'BTrees',
    'zope.component',
    'ZODB',
    'zope.index',
    'repoze.catalog',
    'zc.zlibstorage',
    'pytest',
    'pycrypto',
    'click',
    'bcrypt',
    'passlib']

setup(
    name="zerodb",
    version="0.7",
    description="End-to-end encrypted database",
    author="ZeroDB Inc.",
    author_email="michael@zerodb.io",
    url="http://zerodb.io",
    packages=find_packages(),
    tests_require=INSTALL_REQUIRES,
    install_requires=INSTALL_REQUIRES,
)