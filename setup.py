from setuptools import setup, find_packages
from typing import List

HY = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HY in requirements:  # Correctly indented 'if' statement
            requirements.remove(HY)
    return requirements

setup(
    name='my_package',
    version='0.1',
    author='likith',
    author_email='likithguna2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fixed typo here
)
