import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="random_writer",
    version="0.0.1",

    description="CDK Python example utilizing Lambda, CWEvent and Dynamodb",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Sam Keen",

    package_dir={"": "random_writer"},
    packages=setuptools.find_packages(where="random_writer"),

    install_requires=[
        "aws-cdk.cdk",
        "aws-cdk.aws-events",
        "aws-cdk.aws-events-targets",
        "aws-cdk.aws-lambda",
        "aws-cdk.aws-dynamodb"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
