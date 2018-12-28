import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plsqlutil",
    version="0.0.13",
    author="Danny Walsh",
    author_email="walshdanny700@gmail.com",
    description="Python util function for plsql",
    long_description=long_description,
    long_description_content_type="text/x-rst",
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
