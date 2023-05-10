# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

README = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "package.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        README = stream.read().decode("utf8")

setup(
    long_description=README,
    name="geoh5py",
    version="0.7.0-rc.6",
    description="Python API for geoh5, an open file format for geoscientific data",
    python_requires="==3.*,>=3.7.0",
    project_urls={
        "documentation": "https://geoh5py.readthedocs.io/en/latest/",
        "homepage": "https://mirageoscience.com",
        "repository": "https://github.com/MiraGeoscience/geoh5py",
    },
    author="Mira Geoscience",
    author_email="support@mirageoscience.com",
    license="LGPL-3.0-or-later",
    keywords="geology geophysics data interoperability",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"console_scripts": ["publish = devtools.publish:publish"]},
    packages=[
        "geoh5py",
        "geoh5py.data",
        "geoh5py.groups",
        "geoh5py.handlers",
        "geoh5py.interfaces",
        "geoh5py.io",
        "geoh5py.objects",
        "geoh5py.objects.surveys",
        "geoh5py.shared",
        "geoh5py.workspace",
    ],
    package_dir={"": "."},
    package_data={
        "geoh5py.interfaces": ["*.pyi"],
        "geoh5py.io": ["*.orig"],
        "geoh5py.objects": ["*.orig"],
        "geoh5py.workspace": ["*.orig"],
    },
    install_requires=["h5py==3.*,>=3.2.1", "numpy!=1.19.4"],
    dependency_links=[
        "git+https://github.com/MiraGeoscience/poetry-publish.git@pending_fixes#egg=poetry-publish"
    ],
    extras_require={
        "dev": [
            "lockfile==0.*,>=0.12.2",
            "poetry-publish",
            "pylint==2.*,>=2.3.0",
            "pytest==3.*,>=3.0.0",
            "pytest-cov==2.*,>=2.7.1",
            "scipy==1.*,>=1.4.1",
            "sphinx==3.*,>=3.0.0",
            "sphinx-autodoc-typehints==1.*,>=1.10.0",
            "sphinx-rtd-theme==0.*,>=0.4.3",
            "toml==0.*,>=0.10.2",
        ]
    },
)
