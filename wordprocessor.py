'''
# code from taylor
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
'''

import openai

# Define OpenAI API key
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
#model_engine = "davinci"

prompt = '''
Summarize how this company uses your data into short concise bullet points.

This Twitch Privacy Notice applies to your use of www.twitch.tv, and any other websites, applications, services, or live (in-person) events provided, owned, or operated by Twitch Interactive, Inc. (with its affiliates, âTwitchâ) that link to this Privacy Notice (collectively, the âTwitch Servicesâ). Twitch values the privacy of users, subscribers, publishers, members, and others who visit and use the Twitch Services (collectively or individually, âyouâ or âusersâ) and wants you to be familiar with how we collect, use, and disclose personal information from and about you. By visiting www.twitch.tv, setting up your Twitch account, or using the Twitch Services, you are accepting the practices described in this Privacy Notice, to the extent permitted by law.
'''
# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0,
)

response = completion.choices[0].text
print(response)