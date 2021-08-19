# ParseNLPContents

### Purpose
* This is a web scraper/downloader for CS 447 NLP site contents.
* Target URL: https://courses.grainger.illinois.edu/cs447/fa2020/
___
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
___
### Usage
* Execute `script.py`
```
python script.py
```
___
### Output file structure
* There is a main script runner called `script.py` in the top-level directory, which uses a class in `./parse_nlp/ParseNLPContents.py`.
* Downloaded PDFs will be placed into three new directories located in the project repository: `lectures`, `hws`, and `other` (optional readings). 


```
hws
├── hw1_2020.pdf
├── hw2.pdf
├── hw3.pdf
└── hw4.pdf
lectures
├── lecture01.pdf
├── lecture02.pdf
├── lecture03.pdf
├── lecture04.pdf
├── lecture05.pdf
├── lecture06.pdf
├── lecture07.pdf
├── lecture08.pdf
├── lecture09.pdf
├── lecture10.pdf
├── lecture11.pdf
├── lecture12.pdf
├── lecture13.pdf
├── lecture14.pdf
├── lecture15.pdf
├── lecture16.pdf
├── lecture17.pdf
├── lecture18.pdf
├── lecture19.pdf
├── lecture20.pdf
├── lecture21.pdf
├── lecture22.pdf
├── lecture23.pdf
├── lecture24.pdf
├── lecture25.pdf
├── lecture26.pdf
├── lecture27.pdf
├── lecture28.pdf
├── lecture29.pdf
└── minecraft.pdf
other
├── BlackburnBos2003Theoria.pdf
├── J02-3001.pdf
├── J04-3003.pdf
├── J04-4002.pdf
├── J05-1004.pdf
├── J07-2003.pdf
├── J08-1001.pdf
├── J08-1002.pdf
├── J10-4002.pdf
├── J90-2002.pdf
├── J93-2004.pdf
├── J95-2003.pdf
├── J97-3002.pdf
├── J98-4004.pdf
├── N03-1017.pdf
├── N07-1051.pdf
├── P03-1054.pdf
├── P97-1003.pdf
├── SteedmanBaldridgeNTSyntax.pdf
├── W18-5408.pdf
├── chap3.pdf
├── esslli3.pdf
└── nnlp.pdf
get_nlp
└── GetNLPContents.py
script.py
readme.md
requirements.txt
venv
└── ...
```