import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postgis_unaccent",
    version="0.1",
    author="Andres Goyburu",
    author_email="andres@girolabs.com",
    description="PostgreSQL connector for Django that facilitates use of unaccent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angoybu/postgis-unaccent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
    ],
    install_requires=["Django>=2.0", "psycopg2>=2.6"],
)
