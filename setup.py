import setuptools

CURRENT_VERSION = '0.0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="white-rabbit",
    version=CURRENT_VERSION,
    author="JGabrielFreitas",
    author_email="jgabrielafreitas@gmail.com",
    description="white rabbit is a log-decorator to take up the execution time of functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jgabrielfreitas/white-rabbit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
