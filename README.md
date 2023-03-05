# konran
A repository for the 2023 UNIHACK Hackathon for the participating team Konran

## Inspiration

Does the term *Terms of Services*, *Privacy Statement*, *Data Policy* and such confuses you? Keen to understand what kind of data your favourite platform collects from you, including what they are allowed to do with it? Us too!

Our team wanted to address the issue of users not reading privacy policies due to the convoluted language used. We have developed a web app/chrome extension to help users summarise different platform’s privacy policy into an easily digestible format.

## What it does

KONRAN uses an AI model to summarise privacy statements into bullet points of information. A typical user’s experience with KONRAN is as simple as this 4 simple steps:

1. Users input the URL of the privacy statement site they want KONRAN to summarise
2. KONRAN’s backend scripts validate and scrape the site if applicable data is found.
3. KONRAN’s AI summarise the scraped privacy statement into key points
4. KONRAN presents the summarised points back to the user in an easily digestible format.

## How to run

Download the dependency:
```
pip install -r requirements.txt
```

To run KONRAN:
```
cd app
flask --app app run
```


## How we built it

Our project contain both frontend and backend components. The scripts, packages, and APIs we used 
in this project are as follows:

### Frontend

- **HTML and CSS** are used to define the structure and aesthetic of the Web and Chrome extension. It hosts a form that sends URL data to the backend side.
- **JavaScript** is used in a control script to pass URL data as requests to the backend and pass summarised data to the main HTML part.

### Backend

- **Flask** is a Python library acting as intermediary between the frontend and backend elements of the app.
- **BeautifulSoup** is a Python library used to mainly for web-scraping. KONRAN use BeautifulSoup to scrape relevant privacy-related data found in the user's input URL and pass it to the OpenAI API to be summarised.
- **OpenAI** Konran use OpenAI's API to call `text-davinci-003` to summarise the text chunks scraped by BeautifulSoup as JSON text.
- **JSON** is a Python library used to handle JSON text data.
- **request** is a Python library used by BeautifulSoup to extract HTML element from the user's input URL.
- **validation** is a Python library used in our validation script to validate whether user's input URL is valid or not.

## Challenges we ran into

The main challenge we ran into was prompt designs. We had to spent time fine-tuning how much information to summarise without rendering the information too vague but also not keeping it too detailed which would make the user not want to read it making the whole concept useless.

We also still struggle with getting the desired output from the model as aforementioned some websites have privacy policies that the OpenAI model we are using struggle to process to a result we want.

We also ran into some issues with Git: we all had varying amounts of experience with GIt and had different ways of how we used it (some people used git through terminal/command line, some used git through a given IDE, and the rest used a standalone git interface app such as Sourcetree or Github desktop). It took time for the team to get into the Git workflow but we found the struggle to be quite rewarding.

## Accomplishments that we're proud of

One aspect of this project that we're proud of is that this is the first time us friends have worked together on a project and apart from a few minor hiccups (with things such as version control on git) we created this functional prototype all within 3 days.

Privacy concern is also an issue close to our team's heart and we're proud that KONRAN can contribute to alleviate this issue.

## What we learned

For a few of us it was our first hackathon which taught us this whole concept of coming up with an idea and working with a new team in a short span of time. We learnt a plethora of different things. From project management to how to effectively learn new code and put it into practice in a short amount of time.

As is the nature of nearly all projects that involve people with different specialities and areas of expertise, some of us had no experience with front end and others had no experience with backend. We got together and delegated our tasks given our preferences and skill sets which helped us initially get this project off the ground. We learnt how to work together as a team - even though our group is made up of good friends, this is the first time we are all working together on something. We managed to work out most problems as a group but still faced a few inevitable headaches when we tried to bring all the parts of our project together which taught us some invaluable lessons on what to do in certain situations when faced with group work in the future.

All of us had to learn something new at some point during this Hackathon. Whether it being a new library or API we were working with or a whole new programming language all together. We had to learn how to navigate documentation more efficiently and not just understand the code we were writing at a superficial level.

## What's next for KONRAN

Future version of KONRAN will be faster and smarter. We've identified many bottlenecks in our scripts that can be edited for efficiency and are looking into fine-tuning the AI model to create better responses. We're also looking into designing alternative prompts that allow the AI to focus on specific section of the privacy policy to obtain only specific information (ex. What data are collected? How can the service use my data?).

________________________

(To be continue.)

### Policy Ranking
web name: 109

web url: 731