from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirementss=[]
    HYPHEN_E_DOT='-e .'
    with open(file_path) as file_obj:
        requirementt=file_obj.readlines()
        requirementss=[req.replace('\n',"") for req in requirementt]
        if HYPHEN_E_DOT in requirementss:
            requirementss.remove(HYPHEN_E_DOT)
    return requirementss


setup(
    name='mlproj',
    version='0.0.1',
    author="Joy",
    author_email="juhigajjam123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)