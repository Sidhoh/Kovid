from setuptools import setup, find_packages

setup(
    name='Kovid',
    version='1.0.0',
    description = "A python lib to get info on covid-19.",
    author = "roof",
    project_urls = {
        "Github": "https://github.com/roooof/Kovid",
    },
    author_email = "danduhman7@gmail.com",
    license = "MIT",
    packages = ["kovid"],
    install_requires=[
        'requests'
    ]
)
