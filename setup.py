from setuptools import setup, find_packages

setup(
    name="mlflow_reports",
    version="1.0.0",
    author="Andre Mesarovic",
    description="MLflow Report Tools",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/amesar/mlflow-reports",
    project_urls={
        "Bug Tracker": "https://github.com/amesar/mlflow-reports/issues",
        "Documentation": "https://github.com/amesar/mlflow-reports/",
        "Source Code": "https://github.com/amesar/mlflow-reports/"
    },
    python_requires = ">=3.8",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=[
        "mlflow-skinny>=2.4.0",
        "mdutils",
        "wheel"
    ],
    extras_require= { "tests": [ "mlflow", "pytest","pytest-html>=3.2.0", "shortuuid>=1.0.11" ] },
    license = "Apache License 2.0",
    keywords = "mlflow ml ai",
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    entry_points = {
        "console_scripts": [
            "get-run = mlflow_reports.data.get_run:main"
        ]
    }
)