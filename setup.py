import setuptools

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package metadata
__version__ = "0.0.0"

REPO_NAME = "Chicken-disease-classification"
AUTHOR_USER_NAME = "bhavith1993"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "bhavithnkr@gmail.com"

# Setup function
setuptools.setup(
    name=SRC_REPO, # Package name
    version=__version__,  # Version
    author=AUTHOR_USER_NAME, # Author name
    author_email=AUTHOR_EMAIL,  # Author email
    description="A small python package for CNN app",  # Short description
    long_description=long_description, # Long description read from README.md
    long_description_content="text/markdown", # Content type of long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the repository
    package_dir={"": "src"}, # Root package directory
    packages=setuptools.find_packages(where="src")   # Packages to include
)