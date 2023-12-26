import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "TEXT_SUMMARIZER_PROJECT"
AUTHOR_USER_NAME = "MLNats"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nattamkarthik@gmail.com"
URL = f"https://github.com/MLNats/Text_Summarizer_Project"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A Small Python Package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    project_urls = {
        "Bug-Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where= "src")
)
