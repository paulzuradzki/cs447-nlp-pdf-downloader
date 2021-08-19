# ParseNLPContents

### Purpose
* This is a downloader for CS 447 NLP site contents.
* Target URL: https://courses.grainger.illinois.edu/cs447/fa2020/

### How it works
* Use the `requests` library to gather the HTML of the target URL via the response.text attribute.
* Use `BeatifulSoup` library for parsing the HTML text to gather links to downloadable PDFs.
* Append the relative PDF links to the base URL so we have a collection of URLs to download.
* Use `requests` again to download each file via requests.get()
    * Mult-threading offers signifanct speed up but may download files out of order
    * If you're picky about things like file "Modified Date" to align with ordering of the file name, set the `script.py` toggle to `THREADED=False`.
* Use the response.content (contnet => byte representation of file in memory) and write out the contents to a file using standard Python file I/O using "write-bytes" mode. ex: `with open('', 'wb') ...`
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
___
### Note on web scraping ethics
This script is intended for a one-time or occasional ad hoc download to automate what a user would do manually to retrieve course content. "Automating the automation" by running the script at high frequency probably puts a burden on the server; that is not intended use.