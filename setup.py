from setuptools import setup, find_packages

setup(
    name="SGC",
    version="1.1.0",
    author="Jinyong Park",
    author_email="phillip1998@korea.ac.kr",
    description="Graph neural network model for prediction of experimental molecular property reflecting Solvatochromic group contribution approach",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/phillip1998/SGC",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
"numpy>=1.23",
"pandas>=2.0",
"scikit-learn>=1.3",
"scipy>=1.10",
"matplotlib>=3.7",
"seaborn>=0.12",
"torch>=2.2",
"rdkit==2024.3.6",
"jupyter>=1.0",
"ipykernel>=6.25",
"notebook>=7.0",
"tqdm>=4.66",
"joblib>=1.3",
"pydantic>=2.10,<3.0",
"dgl",
"D4CMPP==1.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
)