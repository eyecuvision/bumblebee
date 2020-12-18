import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__author__ = "Oguz Vuruskaner"

setuptools.setup(
    name="not-a-bumblebee", 
    version="0.0.1",
    author="Oguz Vuruskaner",
    author_email="ovuruska@outlook.com",
    description="Handling data in computer vision applications before augmentation layer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eye-C-U/bumblebee",
    package_data={
        "eyecu":[
            "./src/__init__.py"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)