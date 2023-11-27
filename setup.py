from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Python client for Hacker News API with cached API calls built in."
LONG_DESCRIPTION = "The Hacker News Client is a Python-based tool designed to seamlessly engage with the official Hacker News Firebase API. This client incorporates a built-in request-cache mechanism for each API call, allowing for the efficient handling of complete data dumps without the need for redundant subsequent calls. This feature significantly optimizes your data wrangling processes, saving you time and resources."

# Setting up
setup(
    name="hacker-news-client",
    version=VERSION,
    author="InquestGeronimmo",
    author_email="rcostanl@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=["requests>=2.31.0", "pandas>=2.1.3", "yt_dlp>=2023.11.16"],
    keywords=["python", "hacker-news", "api"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)