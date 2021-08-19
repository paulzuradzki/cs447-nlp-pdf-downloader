from get_nlp import GetNLPContents as nlp
import os
import concurrent.futures

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
for section, links in links_dict.items():
    print("Downloading:")
    for file in links[:1]:
        print(file)
        nlp.download_file(file, target_dir=section)

print("Complete.")