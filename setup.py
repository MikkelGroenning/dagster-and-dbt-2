from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=required_packages,
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
