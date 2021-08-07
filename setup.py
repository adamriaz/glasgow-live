from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

NAME = "glasgow-live"
DESCRIPTION = "News feeds from https://www.glasgowlive.co.uk/"
VERSION = "0.0.1"
AUTHOR = "Adam Riaz"
AUTHOR_EMAIL = "riaz_adam@hotmail.com"
LONG_DESCRIPTION = long_description
URL = "https://github.com/adamriaz/glasgow-live"

# Required packages
REQUIRED = ["feedparser", "facebook-scraper", "twint"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "dist", "*.egg-info"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "License :: OSI Approved :: MIT License",
    ]
)
