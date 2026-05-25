from setuptools import find_packages, setup

setup(
    name="mlproject",
    version="0.0.1",
    author="Ayush",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "flask",
        "catboost",
        "xgboost",
        "dill",
        "gunicorn"
    ]
)