#-- ################################################################
#--   ______   ________
#--  /      \ /        |  Title:      Github Parser
#-- /$$$$$$  |$$$$$$$$/   Author:     Ahmad M.
#-- $$ |__$$ |    /$$/    Date:       231018
#-- $$    $$ |   /$$/     Params:     github links
#-- $$$$$$$$ |  /$$/      Descrip:    sometimes repos are build in a way
#-- $$ |  $$ | /$$/                   that makes it hard to clone them.
#-- $$ |  $$ |/$$/                    this might be the solutin
#-- $$/   $$/ $$/         Notes:      only works for 1-level depth right now
#-- ################################################################
print("Welcome to A7's Github parser !")
#-- ################################################################
print("Importing libraries and setting up procedures...")
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get
import re, os, wget
#-- ################################################################
link = rawinput("Please enter a link...")
# link = "https://github.com/blackvitriol/ROSCOG/tree/master/ROSCOG_Nao"

foldername = link.split('/')[-1]
os.mkdir(foldername)
os.chdir(foldername)
#-- ################################################################
# 1. Get a soup of all files and folders available on the root page of given link
def get_a_soup(link):
    response = get(link)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    soup = str(html_soup.find_all('span', class_ = 'css-truncate css-truncate-target'))
    print(soup)
    return soup

soup = get_a_soup(link)
#-- ################################################################
# 2. Find all files and folders in the soup, create a hierarchy tree.
#def find_links_in_soup(soup):

list_of_links = re.findall('href=(.+?)id', soup)

for link in list_of_links:
    link = link.strip('" ')
    print("Found link:",link)

    # For files in root folder:
    os
    if '.' in link:
        file = link.split('/')[-1]
        raw = "https://github.com"+link
        raw = raw.replace('blob','raw')
        print("It is a file at", raw, "and has been downloaded.")
        wget.download(raw)

    # For folders:
    else:
        foldername = link.split('/')[-1]
        raw = main+'/'+foldername
        os.mkdir(foldername)
        print("It is a folder at", raw, "and has been created.")


        #print("Now browsing folder and creating tree:")


# return list_of_links

#-- ################################################################
# 3. Download the tree of files and folders.
# downloader(list_of_links)

#-- ################################################################
# Intended order of development & functionality.
# Limitations: folder names should not contain dots
# link = ""
# soup=get_a_soup(link)
# list_of_links=find_links_in_soup(soup)
# downloader(list_of_links)
