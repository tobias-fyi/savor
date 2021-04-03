"""Setup script for the savor package."""

import os
from pathlib import Path
import setuptools

# The directory containing this file
HERE = Path().resolve(strict=True)

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# List of required dependencies
REQUIRED = [
    "pytest",
    "pandas",
    "psycopg2-binary",
    "airtable-python-wrapper",
]

setuptools.setup(
    name="savor",
    version="1.0.1",
    description="A set of simple tools to access, transform, and utilize savor data.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tobias-fyi/savor",
    author="Tobias Reaper",
    author_email="hi@tobias.fyi",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=REQUIRED,
)
