from setuptools import setup, find_packages

setup(
    name="clamito",
    version="0.0.1",
    author="Spencer A. Hill",
    author_email="shill1@ccny.cuny.edu",
    description="An AI-driven climate data analysis package.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/spencerahill/clamito",
    packages=find_packages(where="clamito"),
    package_dir={"": "clamito"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)