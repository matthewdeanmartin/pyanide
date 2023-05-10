from mypyc.build import mypycify
from setuptools import setup

setup(
    name="pyanide",
    packages=["pyanide"],
    ext_modules=mypycify(
        [
            "--disallow-untyped-defs",  # Pass a mypy flag
            "pyanide",
        ]
    ),
)
