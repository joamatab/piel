#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "openlane",
    "cocotb",
    "gdsfactory",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Dario Quintero",
    author_email="darioaquintero@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Photonic and electronic co-simulation system design tools interfaced with open-source design software like GDSFactory and OpenROAD.",
    entry_points={
        "console_scripts": [
            "piel=piel.cli:main",
        ],
    },
    extras_require={
        "develop": [
            "sphinx",
            "sphinx_autodoc_typehints",
            "sphinx-pydantic",
            "sphinx-autoapi",
            "sphinx-autobuild",
            "sphinx_rtd_theme",
            "sphinx-gallery",
            "nbsphinx",
            "myst_parser",
            "pandoc",
            "flake8",
        ]
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="piel",
    name="piel",
    packages=find_packages(include=["piel", "piel.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url='https://github.com/daquintero/piel',
    version="0.0.26",
    zip_safe=False,
)
