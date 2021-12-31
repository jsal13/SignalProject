"""
Tasks file for `invoke`.

Notes:  Type-Hinting is not able to be used until
https://github.com/pyinvoke/invoke/issues/357 is closed.
"""

import os

from invoke import task


@task
def docs(context):
    """Generate Sphinx documentation."""
    if os.name == "nt":  # if windows...
        context.run(".\\docs\\make.bat html")
    else:
        context.run("cd docs && make html && cd ..")


@task
def test(context):
    """Run Pytest."""
    context.run("pytest --cov=sensor tests/")


@task
def install_precommit(context):
    """Install pre-commit into githooks."""
    context.run("pre-commit install")


@task
def tox(context):
    """Run Tox."""
    context.run("tox")


@task(pre=[install_precommit])
def init(_context):
    """Init the repository.

    - Install pre-commit hooks.
    """
    print("Installing pre-commit...")
