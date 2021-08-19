"""script.py

Uses GetNLPContents module to collect URLs for PDF downloads. 
Downloads each PDF into corresponding folder: lectures, hws, other

"""
from get_nlp import GetNLPContents as nlp
import os
import concurrent.futures
import logging
from time import perf_counter

# toggle to False to disable multi-threading. Benchmarks:
    # threaded: Duration: 13.35 seconds. 0.22 minutes.
    # non-threaded: Duration: 164.01 seconds. 2.73 minutes.
THREADED = True

t0 = perf_counter()
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
logging.info("Start script.")

# make directory if it does not exist to store PDFs by section
for section in ['lectures', 'hws', 'other']:
    if not os.path.exists(section):
        os.mkdir(section)

# get links to download and store in dict
base_url = r'https://courses.grainger.illinois.edu/cs447/fa2020/'
nlp = nlp.GetNLPContents(base_url)

# structure: {'lectures': [url string...], 'hws': [...], 'other': [...]}
links_dict = nlp.gather_download_links()

# each key in dict is a list of URLs
# download PDF from each URL and place in target dir

n_threads = 10
for section, links in links_dict.items():
    logging.info("Downloading:")
    if THREADED:
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
            executor.map(nlp.download_file, links, [section]*n_threads)
    else:
        for file in links:
            nlp.download_file(file, target_dir=section)

t1 = perf_counter()
logging.info("Duration: {:.2f} seconds. {:.2f} minutes.".format(t1-t0, (t1-t0)/60))
logging.info("End script.")