from setuptools import setup, find_packages
setup(
    name='text_verification_tool',
    version='0.1',
    author='Xingjian Pan',
    author_email='xingjianpan@163.com',
    packages=find_packages(),
    entry_points = {
            'console_scripts': [
                        'killproc = killproc.killproc:main'
                        ]},
    install_requires=[],
    license='',
    description='',
    long_description=open('README.rst').read(),
    classifiers=["Environment :: Console"],
                     )
