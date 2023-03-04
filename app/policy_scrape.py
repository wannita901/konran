from bs4 import BeautifulSoup
import requests
import re

def strips(items):
    '''
    Strip newline characters and convert list of strings item to lowercase
    '''
    new_items = [x.lower().strip() for x in items]
    return new_items

def authenticate_page(soup):
    '''
    Search for pre-defined tags in web headers to decide whether it is a suitable page or not
    '''

    # Import list of tags
    with open("tags.txt", "r", encoding="utf-8") as file:
        tags = file.readlines()
    tags = strips(tags)

    # Scrape site headers
    headers_all = soup.find_all(re.compile('^h[1-2]$'))
    headers = []
    for header in headers_all:
        headers.extend(header)
    headers = strips(headers)
    headers = [header.split() for header in headers]
    # flatten list of lists into 1-dimension list
    headers = list(set([i for sublist in headers for i in sublist]))

    for tag in tags:
        if tag in headers:
            return True

def scrape_policy(URL):
    '''
    Scrape policy page content if it qualifies as a policy page
    '''
    page = requests.get(URL)

    scraped_txt = str()

    soup = BeautifulSoup(page.text, "html.parser")

    ## If tag is found in headers, mine texts
    if authenticate_page(soup):
    
        # No Headers Method
        '''
        for item in soup.find_all("p"):
            results_test.write(item.text+"\n\n")
        '''

        # With Headers Method
        for element in soup.find_all():
            if element.name == 'p':
                scraped_txt = scraped_txt + element.text + "\n"
            elif element.name in ['h1', 'h2', 'h3', 'h4','h5','h6']:
                scraped_txt = scraped_txt + "[" + element.text + "]"
    else:
        pass
    
    return scraped_txt

if __name__ == "__main__":
    # URL = "https://www.twitch.tv/p/en/legal/privacy-notice/"
    URL = "https://www.apple.com/legal/privacy/en-ww/"
    # URL = "https://slack.com/intl/en-au/trust/privacy/privacy-policy"

    print(scrape_policy(URL))