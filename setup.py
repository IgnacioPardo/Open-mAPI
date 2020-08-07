from setuptools import setup, find_packages
import pathlib

setup(
    name='openmapi',
    packages = ['openmapi'], 
    version='1.4.0',
    license='MIT', 
    description='API COVID 19 por Provincias Argentinas',
    url='https://github.com/Creativity-Hub/Open-mAPI',
    download_url = 'https://github.com/Creativity-Hub/Open-mAPI/archive/1.4.0.tar.gz',
    author='Creativity Hub',
    author_email='info.creativityhub@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='mAPI, Open_mAPI, covid19, Argentina',
    python_requires='>=3.5, <4',
    install_requires=['bs4~=0.0.1'],
    project_urls={
        'Bug Reports': 'https://github.com/IgnacioPardo/Open-mAPI/issues',
        'Say Thanks!': 'https://saythanks.io/to/ignacio.pardo%40ort.edu.ar',
        'Source': 'https://github.com/IgnacioPardo/Open-mAPI',
    },
)
