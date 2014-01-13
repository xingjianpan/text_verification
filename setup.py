import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='text_verification_tool',
    version='0.1',
    author='Xingjian Pan',
    author_email='xingjian.pan@thomsonreuters.com',
    description = ("The tool compare documents in different format",
                   "and report the difference in HTML format."),
    keywords = "source comparision pdf xml source html",
    packages = ['text_verification_challenge','tests'],
    license='',
    long_description=read('README'),
    classifiers=["Environment :: Console"],
    install_requires=[
        "lxml ==3.2.5",
        "pdfminder==20131113",
            ],
                     )
