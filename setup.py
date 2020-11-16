import os
import shutil
from pathlib import Path
import sys
from setuptools import setup, find_namespace_packages

long_description = """# The EyeOnText Wowool Sample package"""

eot_packages = find_namespace_packages(include=["eot.wowool.samples"])
print(eot_packages)

sdk_version = open("version.txt").read().strip()

# fmt: off
results = setup(
    name="eot-wowool-samples",
    version=sdk_version,
    author="EyeOnText",
    description="The EyeOnText Wowool Sample package",
    long_description=long_description,
    packages=eot_packages,
    python_requires=">=3.8",
    zip_safe=False,
    include_package_data=True,

)