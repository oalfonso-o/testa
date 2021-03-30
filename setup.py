from setuptools import setup, find_packages

setup(
    name='testa',
    version='1.0.0',
    description='testa service',
    author='Oriol Alfonso',
    author_email='oriolalfonso91@gmail.com',
    packages=find_packages(),
    install_requires=['testb @ git+ssh://git@github.com/oalfonso-o/testb.git'],
    zip_safe=False,
)
