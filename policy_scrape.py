from bs4 import BeautifulSoup
import requests

URL = "https://www.twitch.tv/p/en/legal/privacy-notice/"
URL_APPLE = "https://www.apple.com/legal/privacy/en-ww/"
page = requests.get(URL)

results_test = open("result.txt", "w+", encoding="utf-8")

soup = BeautifulSoup(page.text, "html.parser")
for item in soup.descendants:
    if any(tag in repr(item) for tag in ["</p>", "</ul>", "</ol>", "</b>"]):
        results_test.write(item.text+"\n")

results_test.close()