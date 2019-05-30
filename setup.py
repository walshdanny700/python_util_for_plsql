import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlLinter",
    version="0.0.23",
    author="Danny Walsh",
    author_email="walshdanny700@gmail.com",
    description="Linter tool for SQL packages written in Python",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/walshdanny700/sqlLinter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
