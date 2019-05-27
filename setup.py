
from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as stream:
  long_description = stream.read()

setup(
  name = "peco",
  version = "0.9.1",
  description = "Simple template engine for HTML.",
  long_description = long_description,
  licence = "MIT",
  author = "tikubonn",
  author_email = "https://twitter.com/tikubonn",
  url = "https://github.com/tikubonn/peco",
  install_requires = [],
  dependency_links = [],
  test_suite = "tests",
  packages = find_packages(exclude=["tests"]),
  entry_points = {
    "console_scripts": [
      "peco = peco_script.peco:main",
    ]
  },
  classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
  ]
)
