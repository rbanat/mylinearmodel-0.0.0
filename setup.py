"""
    Permet l'installation des packages mylinearmodel et myutils.
"""


from setuptools import setup
setup(
    name = "mylinearmodel",
    version = "0.0.0",
    description = "La librairie mylinearmodel",
    author = "Rizlène Banat",
    packages = ["mylinearmodel", "myutils", "test", "test_myutils"],
    py_modules = ["main"],
    package_dir = {
        "mylinearmodel": "./mylinearmodel",
        "myutils": "./mylinearmodel/myutils",
        "test": "./test",
        "test_myutils": "./test/test_myutils",
        "main": "./main",
    },
    package_data={
        "": ["*.txt"],
    },
    install_requires = ["matplotlib"],
)
