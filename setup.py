from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='classical_influence',
    version='1.0.2',
    description='Análise da Influência de Músicas Classicas em Músicas Contemporâneas',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/ratopythonista/classical-influence',
    author='Rodrigo Guimarães Araújo',
    author_email='ratopythonista@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6.*',
    install_requires=[
            'loguru==0.3.2',
            'tensorflow==1.13.2',
            'keras==2.3.0',
            'librosa==0.7.0',
            'pytube==9.5.2',
            'matplotlib==3.1.1',
            'playsound==0.23.1'
        ],
)
