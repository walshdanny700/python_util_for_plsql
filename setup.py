import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_util_for_plsql",
    version="0.0.5",
    author="Danny Walsh",
    author_email="author@example.com",
    description="Python util function for plsql",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walshdanny700/python_util_for_plsql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
