import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tokapi-client",
    version="0.0.3",
    author="Somjik",
    description="Simple http client for TokApi rapid-api tiktok mobile API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mtokapi/tokapi-client",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["client"],
    include_package_data=True,
    install_requires=['requests']
)
