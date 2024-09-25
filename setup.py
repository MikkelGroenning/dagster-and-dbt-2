from setuptools import find_packages, setup

with open('project-repo/requirements.txt') as f:
    required_packages = f.read().splitlines()

#required_packages = [req.split(';')[0] for req in required_packages]

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=required_packages,
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
