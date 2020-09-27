import setuptools

long_description = \
    """Tunepy2 is a collection of bitstring optimizers designed to be easy to use yet extensible. Tunepy2 also 
    contains a set of tools to help use bitstring optimizers to optimize hyperparameters for machine learning models."""

setuptools.setup(
    name="tunepy2",
    version="0.0.1",
    author="Ethan Fortner",
    author_email="ethan.fortner@icloud.co,",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
