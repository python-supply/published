from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="published",
    version="0.1.1",
    packages=["published",],
    install_requires=[],
    license="MIT",
    url="https://github.com/python-supply/published",
    author="Python Supply",
    author_email="contact@python.supply",
    description="Python library that serves as an example/template "+\
                "for a package publishing guide.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
