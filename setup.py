from setuptools import setup, find_packages

with open('VERSION', 'r') as version_file:
    version = version_file.readline().strip()

setup(
    name="stem_renamer",
    version=version,
    author="Juhamikael",
    package=find_packages(),
    include_package_data=True
    # install_requires=[
    #     "kivy"
    # ]
)
