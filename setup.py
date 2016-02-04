from setuptools import find_packages
from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='OneSignalPythonSDK',
    packages=find_packages(exclude=['tests*']),
    version='0.1',
    description='A Python SDK for OneSignal (http://onesignal.com)',
    long_description=readme(),
    author='Waqas Younas, Zohaib Ijaz',
    author_email='waqas.younas@gmail.com, mzohaib.qc@gmail.com',
    url='https://github.com/gettalent/one-signal-python-sdk',
    keywords=['onesignal', 'onesignalsdk', 'sdk'],
    install_requires=[
        'requests',
        'pytest'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
    ]
)
