[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/svthalia/miniconcrexit-tutorial?quickstart=1)

# Hello, concrexit!

Welcome to the mini-version of [concrexit](http://github.com/svthalia/concrexit). 
This is a small Django project that is used as a tutorial for new developers to get familiar with the actual [concrexit codebase](http://github.com/svthalia/concrexit).

This project contains a virtually empty website for Thalia. It is a starting point for 
new developers, to try adding a feature quickly, without the distraction and intimidation 
of a large codebase.

There is an example issue that you can try to implement in this project. It is a realistic
issue that could even one day be implemented in the real concrexit. You can find the issue
here: [#1](https://github.com/svthalia/miniconcrexit-tutorial/issues/1).


## Usage

> To get set up very easily, without installing anything on your computer, you can use GitHub Codespaces. Press below to open a codespace for this project.
> 
> [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/svthalia/miniconcrexit-tutorial?quickstart=1)
>
> This will give you a full development environment with a proper Python version, Poetry, and the repository cloned. You should then continue at `poetry shell` below.


The Technicie can help explain better, but here are some things you can do to get this
project running on your own computer. First ensure you have Python and 
[Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) installed.
Then:

```
# If you haven't cloned this yet:
git clone git@github.com:svthalia/miniconcrexit-tutorial.git

# To install the dependencies:
poetry install

# Open a shell where the dependencies are installed:
poetry shell

# To create or update the database:
python website/manage.py migrate

# To create a (super)user:
python website/manage.py createsuperuser

# To run the server:
python website/manage.py runserver
```


## What I did to set up this project

> You do not have to do this yourself, this is just for reference.

```bash
mkdir miniconcrexit-tutorial
cd miniconcrexit-tutorial
git init

poetry init
poetry add Django
poetry add django-bootstrap5
poetry add --group dev black
poetry install

poetry shell

mkdir website
cd website
django-admin startproject miniconcrexit .
```
