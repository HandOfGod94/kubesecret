from setuptools import find_packages, setup

from kubesecret import __version__

setup(
    name="kubesecret",
    version=__version__,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kubesecret = kubesecret.kubesecret:execute",
        ],
    },
    author="Gahan Rakholia",
    author_email="gahan94rakh@gmail.com",
    description="A small wrapper around fzf and kubectl to view kube secrets with preview",
    url="https://github.com/handofgod94/kubesecret",
    python_requires=">=3.6",
)
