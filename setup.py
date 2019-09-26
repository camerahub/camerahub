import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="photodb",
    version="0.0.0",
    description="App for cataloguing vintage cameras, lenses, films, negatives & prints",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/djjudas21/photodb-django",
    author="Jonathan Gazeley",
    author_email="photodb@jonathangazeley.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["photodb"],
    include_package_data=True,
    install_requires=[
        "Django==2.2.4",
        "pytz==2019.2",
        "sqlparse==0.3.0",
        "django-admin-tools==0.8.1",
        "django-fluent-dashboard==1.0.1",
        "django-money==0.15",
        "django-choices==1.7.0",
        "django-favicon==0.1.3",
    ],
#    entry_points={
#        "console_scripts": [
#            "realpython=reader.__main__:main",
#        ]
#    },
)