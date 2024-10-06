from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
    return requirements

setup(
    name="ML Project",
    version="0.01",
    author="Zaeem Hassan",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)