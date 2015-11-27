from setuptools import find_packages, setup

__author__ = 'adb'


setup(
    name='VcfTools',
    version='0.1.0',
    author='Aditya Bharadwaj',
    author_email='adb@vt.edu',
    description='CLI for My VCF Tools',
    long_description=__doc__,
    py_modules=[
        'vcftools'
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyvcf',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'adb-vcftools = vcftools.cli:main'
        ]
    }
)
