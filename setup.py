"""Installer for the plonectl package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""

_base_requirements = [
    "setuptools",
    "Products.CMFPlone",
    "Jinja2",
    "dynaconf",
    "typer",
]

_bpython_support = [
    "bpython",
]
_ipython_support = [
    "prompt-toolkit>=3.0.28",
    "IPython",
]

_recommended = _bpython_support

_all = _bpython_support + _ipython_support

_test = [
    "relstorage",
    "zest.releaser[recommended]",
    "zestreleaser.towncrier",
    "plone.app.testing",
    "pytest",
    "pytest-cov",
    "pytest-plone>=0.2.0",
]

setup(
    name="plonectl",
    version="1.0.0a1",
    description="NextGen CLI controller for Plone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Distribution",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Érico Andrei",
    author_email="ericof@plone.org",
    url="https://github.com/plone/plonectl",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/plonectl",
        "Source": "https://github.com/plone/plonectl",
        "Tracker": "https://github.com/plone/plonectl/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=_base_requirements,
    extras_require={
        "bpython": _bpython_support,
        "ipython": _ipython_support,
        "recommended": _recommended,
        "all": _all,
        "test": _test,
    },
    entry_points="""
    [console_scripts]
    plonectl = plonectl.cli:cli
    """,
)
