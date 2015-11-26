#! /usr/bin/python
from setuptools import setup, find_packages
import os


version = __import__('whiterabbit').get_version()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="whiterabbit",
    version=version,
    description="Django-based personal advisor",
    license="GPL",
    long_description=read("README.md"),
    keywords="django, agenda",
    author="Dmitry Kutsenko",
    author_email="d2emonium@gmail.com",
    url="http://github.com/d2emon/whiterabbit.git",
    platforms=["any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Office/Business",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
