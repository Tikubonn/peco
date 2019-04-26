
from setuptools import setup, find_packages

setup(
  name = "peco",
  version = "0.9.0",
  description = "Simple template engine for HTML.",
  author = "tikubonn",
  author_email = "https://twitter.com/tikubonn",
  licence = "MIT",
  install_requires = [],
  dependency_links = [],
  test_suite = "tests",
  packages = find_packages(exclude=["tests"])
)

