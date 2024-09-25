# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_university',
 'dagster_university.assets',
 'dagster_university.jobs',
 'dagster_university.partitions',
 'dagster_university.resources',
 'dagster_university.schedules',
 'dagster_university.sensors']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.35.20,<2.0.0',
 'dagit>=1.8.6,<2.0.0',
 'dagster-cloud>=1.8.7,<2.0.0',
 'dagster-dbt>=0.24.7,<0.25.0',
 'dagster-duckdb-pandas>=0.24.6,<0.25.0',
 'dagster-duckdb>=0.24.6,<0.25.0',
 'dagster>=1.8.6,<2.0.0',
 'dbt-core>=1.8.6,<2.0.0',
 'dbt-duckdb>=1.8.3,<2.0.0',
 'duckdb==1.1.0',
 'faker>=28.4.1,<29.0.0',
 'geopandas>=1.0.1,<2.0.0',
 'kaleido==0.2.1',
 'matplotlib>=3.9.2,<4.0.0',
 'pandas>=2.2.2,<3.0.0',
 'plotly>=5.24.1,<6.0.0',
 'poetry2setup>=1.1.0,<2.0.0',
 'pyarrow>=17.0.0,<18.0.0',
 'requests>=2.32.3,<3.0.0',
 'shapely>=2.0.6,<3.0.0',
 'smart-open>=7.0.4,<8.0.0']

setup_kwargs = {
    'name': 'dagster-university',
    'version': '0.1.0',
    'description': '',
    'long_description': '## Dagster University: Dagster + dbt\n\nThis is the **starter** version of the [Dagster](https://dagster.io/) project made to accompany Dagster University\'s [Dagster + dbt course](https://courses.dagster.io/courses/dagster-dbt).\n\n> **Looking for the finished project for the Dagster + dbt course?** Use the [`module/dagster-and-dbt` branch](https://github.com/dagster-io/project-dagster-university/tree/module/dagster-and-dbt).\n\n## Getting started\n\nFirst, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.\n\n```bash\npip install -e ".[dev]"\n```\n\nDuplicate the `.env.example` file and rename it to `.env`. Then, fill in the values for the environment variables in the file.\n\nThen, start the Dagster UI web server:\n\n```bash\ndagster dev\n```\n\nOpen http://localhost:3000 with your browser to see the project.\n\n## Development\n\n### Adding new Python dependencies\n\nYou can specify new Python dependencies in `setup.py`.\n\n### Unit testing\n\nTests are in the `dagster_university_tests` directory and you can run tests using `pytest`:\n\n```bash\npytest dagster_university_tests\n```\n\n### Schedules and sensors\n\nIf you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.\n\nOnce your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.\n\n## Deploy on Dagster Cloud\n\nThe easiest way to deploy your Dagster project is to use Dagster Cloud.\n\nCheck out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.\n# dagster-and-dbt-2\n',
    'author': 'Mikkel Grønning',
    'author_email': 'mikkel@groenning.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.12,<3.13',
}


setup(**setup_kwargs)

