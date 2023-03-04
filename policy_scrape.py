from bs4 import BeautifulSoup
import requests

URL = "https://www.twitch.tv/p/en/legal/privacy-notice/"
URL_APPLE = "https://www.apple.com/legal/privacy/en-ww/"
URL_SLACK = "https://slack.com/intl/en-au/trust/privacy/privacy-policy"
page = requests.get(URL_SLACK)

results_test = open("result.txt", "w+", encoding="utf-8")

soup = BeautifulSoup(page.text, "html.parser")

# No Headers Method

'''
for item in soup.find_all("p"):
    results_test.write(item.text+"\n\n")
'''

# With Headers Method
for element in soup.find_all():
    if element.name == 'p':
        results_test.write(element.text + "\n\n")
    elif element.name in ['h1', 'h2', 'h3', 'h4','h5','h6']:
        results_test.write("[" + element.text + "]")



results_test.close()