# ParseNLPContents

### Purpose
This is a web scraper/downloader for CS 447 NLP site contents.

### Install Dependencies
* `git clone` this repo
```
git clone <>
```
* Navigate to directory of the repository.
* Create a virtual environment and activate it.
```
python3 -m venv venv
source venv/bin/activate
```
* Install third-party packages.
```
pip install -r ./requirements.txt 
```

### Usage
* Execute `script.py`
```
python script.py
```
* PDFs will be placed into three new directories located in the project repository: `lectures`, `hws`, and `other` (optional readings). 

### File structure
There is a main script runner called `script.py` in the top-level directory, which uses a class in `./parse_nlp/ParseNLPContents.py`.


