===========
sensor
===========

What is this?
=============

**The Problem**: Whenever I needed an up-to-date template to start a new Python project (module, package, etc.) in, I'd start it from scratch each time.  *This package is meant to be an (updated) template to use for Python modules/packages.*

How Do I Use This?
==================

First...
--------
There's a number of hard-coded "sensor"s in this project, so you'll need to...

- Rename "sensor" with the name of your package
- Find-Replace all uses of "sensor" with the name of your package in this project

Then...
-------
In your terminal,

1. Install Poetry::

    pip install poetry

2. In the root, create the poetry venv::

    poetry install

3. Initialize the repo::

    invoke init

4. Use the Poetry Shell to open the project in VSCode::

    poetry shell
    code .

**Important Note**: When committing to git, pre-commit may format your code and say the commit failed; simply re-add the files and run the commit again and it should pass. This is intended behavior for pre-commit.  You may remove pre-commit at your own risk with the commands::

    pre-commit uninstall

(Optional) Some Other Things You Can Do
----------------------------------------

For many optional things, we use Invoke_ to call basic commands.  See the docs and the ``tasks.py`` file in the root directory for more information on Invoke.

- To Remove the Vertical Line that's at Column 88 for VSCode, remove the "Editor Rules" line in ``.vscode/settings.json``

- To Remove / Modify the Github Actions file, delete / edit the ``.github\workflows\sample-github-action.yml`` file.

- To run tests, you can use the VSCode test tab on the left-hand side (looks like a beaker)
    - To run testing + coverage, on the terminal::

        invoke test

- To run Sphinx, use the command::

    invoke docs

- To configure Tox, check out its section in ``pyproject.toml`` and run::

    tox
    # or `invoke tox`

- If you want to Dockerize anything, I've included a ``Dockerfile`` for using Poetry and Python, a ``docker-entrypoint.sh`` for exec, and a basic ``docker-compose`` file for composition


What does this include?
=======================
- Venv and Build Tools
    - Poetry_ allows us to easily manage a venv and build our things quickly.

- Linting and Formatting
    - Pylint_ is a code analysis tool
    - Black_ is an uncompromising formatter
    - flake8_ is a style guide enforcement tool which encludes McCabe (complexity checker)
    - mypy_ is a static type checker (enforces type hints)
    - pydocstyle_ is a docstring linter
    - isort_ sorts imports

- Testing Integration
    - Pytest_ for testing and Pytest-Cov_ for coverage
    - Tox_ for venv management and testing

- Documentation
    - Sphinx_ with Sphinx-AutoAPI_ to generate things automatically

- CLI
    - Invoke_ allows for easy CLI creation

- Containerization
    - Docker_ and docker-compose to create containers if needed

What's this XYZ Config file?
============================
- ``pyproject.toml``: The new standard for Python configuation
    - **There's a lot you can edit, so check it out**
- ``.flake8``: Because of `this frustrating thread <https://github.com/PyCQA/flake8/issues/234>`_
- ``.pre-commit-config``: Required my ``pre-commit``, read more `here <https://pre-commit.com/#intro>`_
- ``poetry.lock``: A poetry file which contains specifics about what's installed.  Poetry generates this when you install it
- ``.vscode/``: A folder for custom vscode configurations
- ``Dockerfile``, ``docker-entrypoint.sh``, ``docker-compose.yaml``: These are all Docker-related files, all optional unless you'd like to use Docker
- ``.github/workflows/sample-github-action.yml`` is a sample for `Github Actions`_ which currently runs tox (and therefore Pytest), but can be configured to run whatever you'd like
- ``tasks.py`` is used by Invoke_ to create CLI commands, check out the link below to create your own


What Still Needs Work?
======================
- **Currently, it seems that Pylint is potentially causing VSC to be extremely slow when linting, lagging minutes behind typing.  I'm looking into solutions for this but have disabled it for now.**
- Better Pytest examples.

.. _Black: https://github.com/psf/black/
.. _Docker: https://www.docker.com/
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _Github Actions: https://github.com/features/actions
.. _Invoke: https://docs.pyinvoke.org/en/stable/index.html
.. _isort: https://pycqa.github.io/isort/
.. _mypy: http://mypy-lang.org/
.. _Poetry: https://python-poetry.org/docs/basic-usage/
.. _pydocstyle: http://www.pydocstyle.org/en/stable/
.. _PyLint: https://pylint.org/
.. _Pytest-Cov: https://pytest-cov.readthedocs.io/en/latest/
.. _Pytest: https://docs.pytest.org/en/6.2.x/
.. _Sphinx-AutoAPI: https://github.com/readthedocs/sphinx-autoapi
.. _Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _Tox: https://tox.wiki/en/latest/
