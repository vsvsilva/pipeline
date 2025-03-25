from setuptools import setup, find_packages

setup(
    name="currency_api",
    version="1.0.0",
    description="API para cotação de moedas usando FastAPI",
    author="Vitor",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        "fastapi",
        "requests",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
