
import json
import openai

def summarize_notice(full_txt: str) -> str:
    """
    This func takes in a privacy policy as a string and returns a bullet point summary of this given
    privacy policy in JSON form
    :param full_txt: a given privacy policy
    :return: returns a summary returned in JSON form.
    """

    # Define OpenAI API Key
    # Note: Remove the actual API key before pushing to GitHub
    openai.api_key = ""

    # Define which model to use
    model_engine = "text-davinci-003"

    # Create prompt - merge the given policy text with a command to give OpenAI
    prompt = """Summarize how this company uses your data into short concise bullet points.
    
    """ + full_txt

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0,
    )

    # Save the response
    response = completion.choices[0].text

    # Split up the response's separate bullet points into a list of strings
    str_lst = []
    last_break = 0
    for i in range(len(response)):
        if response[i] == '•':
            str_lst.append(response[last_break:i])
            last_break = i

    # Delete all the standalone new line strings that show up in the list
    for i in range(len(str_lst) - 1, -1, -1):
        if str_lst[i] == '\n':
            del str_lst[i]

    # Split up the individual strings within the list and remove all the bullet points and new lines.
    for i in range(len(str_lst)):
        splitstr = str_lst[i].split()
        for j in range(len(splitstr) - 1, -1, -1):
            if splitstr[j] == '•' or splitstr[j] == '\n':
                del splitstr[j]
        combined_str = ' '.join([str(item) for item in splitstr])
        str_lst[i] = combined_str

    # Create the dictionary and fill it with the bullet points
    str_dct = {}
    for i in range(len(str_lst)):
        str_dct.update({"Data Privacy": str_lst})

    # Convert the dictionary to json
    y = json.dumps(str_dct)
    return y

# Example below
'''
txt = "This Twitch Privacy Notice applies to your use of www.twitch.tv, and any other websites, applications, services, or live (in-person) events provided, owned, or operated by Twitch Interactive, Inc. (with its affiliates, âTwitchâ) that link to this Privacy Notice (collectively, the âTwitch Servicesâ). Twitch values the privacy of users, subscribers, publishers, members, and others who visit and use the Twitch Services (collectively or individually, âyouâ or âusersâ) and wants you to be familiar with how we collect, use, and disclose personal information from and about you. By visiting www.twitch.tv, setting up your Twitch account, or using the Twitch Services, you are accepting the practices described in this Privacy Notice, to the extent permitted by law."
resp = summarize_notice(txt)

print(txt)
print(resp)
'''