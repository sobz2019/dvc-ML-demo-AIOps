from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="sobz2019",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sobz2019/dvc-ML-demo-AIOps",
    author_email="sobz87@gmail.com",
    packages=["src"],
    python_requires=">=3.10",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)