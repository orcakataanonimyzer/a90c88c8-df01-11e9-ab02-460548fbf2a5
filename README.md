# Pillar Kata: word search

This project is an implementation of the
[kata-word-search](https://github.com/PillarTechnology/kata-word-search)
repository written in Python 3. Below you will find instructions on how to set
up the development environment, run the tests, build the documentation,
install/uninstall the program, and how to tear down the development environment.

# Quick-start Guide

If you just want to run the software and don't care about running the tests or
making changes to the code, follow the steps below.

Clone the repository with:
```
git clone https://github.com/david-graves/pillar-kata-word-search.git
cd pillar-kata-word-search
```
Create, and activate, the virtual environment (to avoid any conflicts with your
global installation of Python.

```bash
make env
source env/bin/activate
```
Use `which python` to confirm that the python binary being referenced in your
path is the one from the virtual environment. Lastly, install the application
using `pip`.

```bash
pip install .
```
The `wordsearch` module will install to the virtual environment, and it can be
executed with the following command.

```bash
./env/bin/wordsearch <FILE>
```
Note: There are sample puzzles in the `data/` directory that can be used with
the application, including the one that is mentioned in the requirements
[here](https://github.com/PillarTechnology/kata-word-search).

To see the help menu and usage, pass the `-h` or `--help` option.

```bash
./env/bin/wordsearch --help
```

# Setup and Installation

A Makefile is included in the project to simplify setup. To ensure that the
application is running in a clean environment (and, so that installing its
dependencies does not conflict with the ones that are installed globally on your
machine), you'll need to create the virtual environment for the project.

This can be accomplished by running the following make command from the root of
the repository.
```bash
make env
```
This creates an `env/` directory containing the necessary files for the
environment. It needs to be activated before it can be used. This can be
accomplished by sourcing the `env/bin/activate` file, as is shown below.
```bash
source env/bin/activate
```
The Makefile also contains an `init` task that will invoke `pip` and install the
necessary dependencies for the project.
```bash
make init
```
Once the dependencies are installed, run the tests to ensure that the
application is working as expected. A `test` task is supplied in the Makefile,
so just run the following make command.
```bash
make test
```
Lastly, there are few ways to install and run the application, but perhaps the
easiest is to simply run it from the root of the repository with:
```bash
python -m wordsearch <FILE>
```
Alternatively, you may install it using the `setup.py` file that is included in
the project:
```bash
pip install -e .
```
The `-e` flag makes it so changes made to the source code are immediately
reflected in the installed application. To learn more about this option, please
see [this
article](http://codumentary.blogspot.com/2014/11/python-tip-of-year-pip-install-editable.html)
about the `--editable` option in `pip`.

# Uninstall

If you installed the application using `pip` as instructed in the *Setup and
Installation* section, then you can uninstall using `pip`. This assumes that the
virtual environment is still active. If it is not, be sure to `source` the
activation file before running any of these commands.
```bash
pip uninstall wordsearch
```
If you would like to keep the application installed in the virtual environment,
but want to deactivate the environment, then run the following command:
```bash
deactivate
```
# Documentation

The documentation for this project is written in RST format, and an HTML version
can be generated based on the docstring in each module, class, method, and 
function. To generate the documentation, follow these steps:
```bash
cd docs
make html
```
Once the documentation generates, open the `build/html/index.html` file in a
web-browser to view.
