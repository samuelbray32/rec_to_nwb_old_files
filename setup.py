from setuptools import find_packages, setup

version = '0.1.020'
print(version)

setup(
    name='rec_to_nwb',
    version=version,
    author='Novela Neurotech',
    url="https://github.com/NovelaNeuro/rec_to_nwb",
    packages=find_packages(),
    package_data={'': ['logging.conf', 'data/fl_lab_header.xsd',
                       'data/header_schema.xsd', 'data/default_header.xml']},
    description='Data transformation from rec binary files into NWB 2.0 format',
    platforms='Posix; MacOS X; Windows',
    python_requires='>=3.6',
    install_requires=[
        'rec_to_binaries>=0.6.12'
    ]
)
