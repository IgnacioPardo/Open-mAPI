from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='mAPI',
    version='2.0.0',
    description='API COVID 19 por Provincias Argentinas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/IgnacioPardo/Open-mAPI',
    author='Ignacio Pardo, Lucia Parrondo',
    author_email='ignacio.pardo@ort.edu.ar',
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
    package_dir={'': 'mAPI'},
    packages=find_packages(where='mAPI'),
    python_requires='>=3.5, <4',
    install_requires=['bs4~=0.0.1'],
    project_urls={
        'Bug Reports': 'https://github.com/IgnacioPardo/Open-mAPI/issues',
        'Say Thanks!': 'https://saythanks.io/to/ignacio.pardo%40ort.edu.ar',
        'Source': 'https://github.com/IgnacioPardo/Open-mAPI',
    },
)