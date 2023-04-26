import setuptools



setuptools.setup(
    name="packagepy", # Replace with your own username
    version="0.0.1",
    author="farin.s",
    author_email="farinshaikh13@gmail.com",
    description="A small example package",
    long_description="test package",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
