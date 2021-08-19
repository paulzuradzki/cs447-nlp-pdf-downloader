import requests
from bs4 import BeautifulSoup
import re
import os
from typing import Dict, List

class GetNLPContents:
    """Class for downloading PDFs from NLP course site."""    

    def __init__(self, base_url):
        self.base_url = base_url
        self.html_doc = requests.get(self.base_url).text
        
    def gather_download_links(self) -> Dict[str, List]:

        soup = BeautifulSoup(self.html_doc, 'html.parser')

        a_tags = soup.find_all("a")
        pdf_links = [a_tag['href'] for a_tag in a_tags if '.pdf' in str(a_tag)]


        links_dict = {'lectures': [], 'hws': [], 'other': []}

        for link in pdf_links:     
            # if match_obj is not None, append to list
            # convert relative paths to full URLs
                # ex, from: './slides/lecture01.pdf'
                # to: base_url + './slides/lecture01.pdf'

            # ignore Jurafsky textbook chapters (full text download available)
            if (match_obj := re.search('.*(jurafsky)|(martin/slp/updates).*', 
                                       link.lower())):
                continue

            # capture lecture{N} slides (and minecraft.pdf)
            elif (match_obj := re.search('.*\./slides.*', link.lower())):
                rel_url = match_obj.group(0).replace('./', '')
                links_dict['lectures'].append(self.base_url + rel_url)

            # cath homework slides
            elif (match_obj := re.search('.*hw.*', link.lower())):
                rel_url = match_obj.group(0).replace('./', '')
                links_dict['hws'].append(self.base_url + rel_url)

            # everything else goes to 'other' (mostly optional reading)
            else:
                links_dict['other'].append(link)

        return links_dict
        
    @staticmethod
    def download_file(url, target_dir=''):  
        """Downlaods file given URL."""
        
        print(url)        
        response = requests.get(url)

        # ex: 'https://courses.grainger.illinois.edu/cs447/fa2020/slides/lecture01.pdf'
        # => 'lecture01.pdf'
        filename = url.split('/')[-1]
        filepath = os.path.join(target_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)
            
            
