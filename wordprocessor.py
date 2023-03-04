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

def generate_summary(full_text):
    prompt = ""
    prompt += full_text


# Set up the model and prompt
model_engine = "text-davinci-003"
#model_engine = "davinci"

prompt23462 = """
Summarize how this company uses your data into short concise bullet points.

This Twitch Privacy Notice applies to your use of www.twitch.tv, and any other websites, applications, services, or live (in-person) events provided, owned, or operated by Twitch Interactive, Inc. (with its affiliates, âTwitchâ) that link to this Privacy Notice (collectively, the âTwitch Servicesâ). Twitch values the privacy of users, subscribers, publishers, members, and others who visit and use the Twitch Services (collectively or individually, âyouâ or âusersâ) and wants you to be familiar with how we collect, use, and disclose personal information from and about you. By visiting www.twitch.tv, setting up your Twitch account, or using the Twitch Services, you are accepting the practices described in this Privacy Notice, to the extent permitted by law.
"""

prompt = """
Summarise the following privacy notice, taking note of key information regarding data collection, tracking, how personal information is used, what can third parties access, and user rights.

[Privacy policy][Trust navigation][Getting started][Privacy][Data requests][Compliance][Security][Data management][Legal]Effective date: 5 January 2023

This Privacy Policy describes how Slack collects, uses and discloses information associated with an identified or identifiable individual (referred to in this Privacy Policy as ‘Personal Data’) and what choices you have around this activity. If you have any questions, please don’t hesitate to contact us.

When we refer to ‘Slack’, we mean Slack Technologies, LLC or Slack Technologies Limited, as explained in more detail in the ‘Identifying the data controller and processor’ section below.

[Table of contents:][Applicability of this Privacy Policy]This Privacy Policy applies to Slack’s online workplace productivity tools and platform, including the associated Slack mobile and desktop applications (collectively, the ‘Services’), Slack.com and other Slack websites (collectively, the ‘Websites’) and other interactions (e.g. customer service enquiries, user conferences, etc.) that you may have with Slack. If you do not agree with this Privacy Policy, then do not access or use the Services, Websites or any other aspect of Slack’s business. For the avoidance of doubt, this is the only privacy policy that applies to Slack.

This Privacy Policy does not apply to any third-party applications or software that integrate with the Services through the Slack platform (‘Third-Party Services’), or any other third-party products, services or businesses who will provide their services under their own terms of service and privacy policy. In addition, a separate agreement governs delivery, access and use of the Services (the ‘Customer Agreement’), including the processing of data such as messages, files or other content submitted through Services accounts (collectively, ‘Customer Data’). The organisation (e.g. your employer or another entity or person) that entered into the Customer Agreement (the ‘Customer’) controls its instance of the Services (its ‘Workspace’) and any associated Customer Data. If you have any questions about specific Workspace settings and privacy practices, please contact the Customer whose Workspace you use. If you have an account, you can check http://slack.com/account/team for the contact information of your workspace owner(s) and administrator(s). If you have received an invitation to join a Workspace but have not yet created an account, you should request assistance from the Customer that sent the invitation.

California notice of collection of personal information: We collect the information described below under ‘Information we collect and receive’ for the business and commercial purposes described below under ‘Information use’. To learn more about exercising your California privacy rights, please review the ‘California privacy rights’ section below.

[Information we collect and receive]Slack will collect and receive information through operating the Services and Websites, and through other interactions with Slack. Such information will include Customer Data and other information and data (‘Other Information’) in a variety of ways:

Generally, no one is under a statutory or contractual obligation to provide any Customer Data or Other Information (collectively “Information”). However, certain Information is collected automatically and if some Information, such as Workspace setup details, is not provided, we may be unable to provide the Services.

[How we process your information and our legal bases for doing so]Customer Data will be used by Slack in accordance with a Customer’s instructions, including to provide the Services, any applicable terms in the Customer Agreement, a Customer’s use of Services functionality and as required by applicable law. Slack is a processor of Customer Data and the Customer is the controller. The Customer may, for example, use the Services to grant and remove access to a Workspace, assign roles and configure settings, access, modify, export, share and remove Customer Data, and otherwise apply its policies to the Services.

Slack uses Other Information to operate our Services, Websites and business. More specifically, Slack uses Other Information for the following purposes:

Compliance with a legal obligation:  Slack processes Other Information when we comply with a legal obligation including, for example, to access, preserve or disclose certain information if there is a valid legal request from a regulator, law enforcement or others. For example, a search warrant or production order from law enforcement to provide information in relation to an investigation, such as your profile picture or IP address.


						We use Workspace and account information, usage information, cookie information, Third-Party Services information, contact information, third-party data, audio and video metadata, and additional information provided to Slack for compliance with a legal obligation.


Legitimate interests:  We rely on our legitimate interests or the legitimate interests of a third party where they are not outweighed by your interests or fundamental rights and freedoms (‘legitimate interests’).


						We use Workspace and account information, usage information, cookie information, Third-Party Services information, contact information, third-party data, audio and video metadata, and additional information provided to Slack for the following legitimate interests:


We use Workspace and account information, Third-Party Services information, third-party data and additional information provided to Slack for the following legitimate interests:

We use Workspace and account information and usage information for the following legitimate interests:

We use Workspace and account information, usage information, cookie information, Third-Party Services information, third-party data and additional information provided to Slack for the following legitimate interests:

[How we share and disclose information]This section describes how Slack may share and disclose Information, as described in the section entitled ‘Information we collect and receive’ above. Customers determine their own policies and practices for the sharing and disclosure of Information to third parties. Slack does not control how a Customer or any third party chooses to share or disclose Information.

[Data retention]Slack will retain Customer Data in accordance with a Customer’s instructions (including to perform any applicable terms in the Customer Agreement and through the Customer’s use of Services functionality) and as required by applicable law. The Customer may customise its retention settings and, depending on the Services subscription, apply those customised settings at the Workspace level, channel level or other level. The Customer may also apply different settings to messages, files or other types of Customer Data. The deletion of Customer Data and other use of the Services by the Customer may result in the deletion and/or de-identification of certain associated Other Information. For more detail, please review the Help Centre or contact the Customer.
						Slack may retain Other Information pertaining to you for as long as necessary for the purposes described in this Privacy Policy (such as to provide the Services, including any optional features that you use, and to provide customer support). This may include keeping your Other Information after you have deactivated your account for the period of time needed for Slack to pursue legitimate business interests, conduct audits, comply with (and demonstrate compliance with) legal obligations, resolve disputes and enforce our agreements.


[Security]Slack takes security of data very seriously. Slack works hard to protect Information that you provide from loss, misuse and unauthorised access or disclosure. These steps take into account the sensitivity of the Information that we collect, process and store, and the current state of technology. Slack has received internationally recognised security certifications. To learn more about current practices and policies regarding security and confidentiality of the Services, please visit our Security practices. Given the nature of communications and information processing technology, Slack cannot guarantee that Information during transmission through the Internet or while stored on our systems or otherwise in our care will be absolutely safe from intrusion by others. When you click a link to a third-party site, you will be leaving our site, and we don’t control or endorse what is on third-party sites.

[Age limitations]Slack does not allow use of our Services and Websites by anyone younger than 16 years old, to the extent prohibited by applicable law. If you learn that anyone younger than 16 has unlawfully provided us with personal data, please contact us and we will take steps to delete such information.

[Changes to this Privacy Policy]Slack may change this Privacy Policy from time to time. Laws, regulations and industry standards evolve, which may make those changes necessary, or we may make changes to our services or business. We will post the changes to this page and encourage you to review our Privacy Policy to stay informed. If we make changes that materially alter your privacy rights, Slack will provide additional notice, such as via email or through the Services. If you disagree with the changes to this Privacy Policy, you should deactivate your Services account. Contact the Customer if you wish to request the removal of Personal Data under their control.

[International data transfers]Slack may transfer your Personal Data to countries other than the one in which you live, including transfers to the United States. To the extent that Personal Data is transferred abroad, Slack will ensure compliance with the requirements of the applicable laws in the respective jurisdiction in line with Slack’s obligations.

In particular, we offer the following safeguards if Slack transfers Personal Data from jurisdictions with differing data protection laws:

[Data Protection Officer]To communicate with our Data Protection Officer, please email dpo@slack.com.

[Identifying the Data Controller and Processor]Data protection law in certain jurisdictions differentiates between the ‘controller’ and ‘processor’ of information. In general, the Customer is the controller of Customer Data. In general, Slack is the processor of Customer Data and the controller of Other Information. Different Slack entities provide the Services in different parts of the world.Slack Technologies Limited, an Irish company based in Dublin, Ireland, is the controller of Other Information and a processor of Customer Data relating to Authorised Users who use Workspaces established for Customers outside of the US and Canada.Slack Technologies, LLC, a US company based in San Francisco, California, is the controller of Other Information and a processor of Customer Data relating to Authorised Users who use Workspaces established for Customers in the US and Canada.

[Your rights]Individuals in the European Economic Area, the United Kingdom, Brazil and across the globe have certain statutory rights in relation to their personal data. Subject to any exemptions provided by law, you may have the right to request access to your personal information, as well as to seek to update, delete or correct this information. You can do this using the settings and tools provided in your Services account. If you cannot use the settings and tools, contact the Customer who controls your workspace for additional access and assistance. Please check https://slack.com/account/settings for Customer contact information.

To the extent that Slack’s processing of your Personal Data is subject to the General Data Protection Regulation or other applicable laws requiring a legal basis for processing Personal Data, such as the UK Data Protection Act and the Brazilian General Data Protection Act (Lei Geral de Proteção de Dados), Slack primarily relies on its legitimate interests, described above, to process your Personal Data. Where we rely on legitimate interests to process your Personal Data, you can object to that processing by contacting us as described in the ‘Contacting Slack’ section below. In response to your objection, we will stop processing your information for the relevant purposes unless we have compelling grounds in the circumstances or the processing is necessary in the context of legal claims. Slack may also process Other Information that constitutes your Personal Data for direct marketing purposes, and you have a right to object to Slack’s use of your Personal Data for this purpose at any time.

[Your California privacy rights]This section provides additional details about the personal information that we collect about California consumers and the rights afforded to them under the California Consumer Privacy Act or ‘CCPA’, as amended by the California Privacy Rights Act or ‘CPRA’.

California law requires that we detail the categories of personal information that we collect and disclose for certain ‘business purposes’, such as to service providers that assist us with securing our services or marketing our products, and to such other entities as described in earlier sections of this Privacy Policy. In addition to the information provided above in the ‘Information we collect and receive’ section, we collect the following categories of personal information from you, your employer, data analytics providers, data brokers and Third-Party Services for our business purposes:Identifiers/contact information;Commercial information;Internet or electronic network activity information;Financial information;Geolocation information;Professional or employment-related information;Audio and visual data;In limited circumstances where allowed by law, information that may be protected under California or United States law; andInferences drawn from any of the above categories.

We collect this information for the business and commercial purposes described in the ‘How we process your information and our legal bases for doing so’ section above. We share this information as described in the ‘How we share and disclose information’ section above. Slack does not sell (as such term is defined in the CCPA or otherwise) the personal information that we collect (and will not sell it without providing a right to opt out). We may also share personal information (in the form of identifiers and Internet activity information) with third-party advertisers for the purposes of targeting advertisements on non-Slack websites, applications and services. In addition, we may allow third parties to collect personal information from our sites or services if those third parties are authorised service providers who have agreed to our contractual limitations as to their retention, use and disclosure of such personal information, or if you use our sites or services to interact with third parties or direct us to disclose your personal information to third parties.

Subject to certain limitations, the CCPA provides California consumers the right to request to know more details about the categories or specific pieces of personal information that we collect (including how we use, disclose or may sell this information), to delete their personal information, to opt out of any ‘sales’, to know and opt out of sharing of personal information for delivering advertisements on non-Slack websites, and to not be discriminated against for exercising these rights.

California consumers may make a request pursuant to their rights under the CCPA by contacting us at privacy@slack.com or by filling in this form. We will verify your request using the information associated with your account, including the email address. Government identification may be required. Consumers can also designate an authorised agent to exercise these rights on their behalf. Authorised agents must submit proof of authorisation.

[Data Protection Authority]Subject to applicable law, you also have the right to (i) restrict Slack’s use of Other Information that constitutes your Personal Data and (ii) lodge a complaint with your local data protection authority. If, however, you believe that we have not been able to assist with your complaint or concern, and you are located in the European Economic Area or the United Kingdom, you have the right to lodge a complaint with the competent supervisory authority. If you work or reside in a country that is a member of the European Union or that is in the EEA, you may find the contact details for your appropriate data protection authority on the following website. If you are a resident of the United Kingdom you may contact the UK supervisory authority, the Information Commissioner’s Office.

[Contacting Slack]Please also feel free to contact Slack if you have any questions about this Privacy Policy or Slack’s practices or if you are seeking to exercise any of your statutory rights. Slack will respond within a reasonable timeframe. You can contact us at privacy@slack.com or at our postal address below:

For Customers and Authorised Users who use Workspaces established for Customers in the US and Canada:

Slack Technologies, LLC50 Fremont StreetSan Francisco, CA 94105United States

or

For Customers and Authorised Users who use Workspaces established for Customers outside the US and Canada:

Slack Technologies LimitedLevel 1, Block ANova Atria NorthSandyford Business DistrictDublin 18Ireland

[Try Slack with your team for free]Change region

Selecting a different region will change the language and content of slack.com.

[Americas][Europe][Asia Pacific]
"""

prompt2 = """
Summarise the privacy notice even further while not removing key concrete content. Write bullet points for the following topics:  data collection, tracking, how personal information is used, what can third .parties access, and user rights.

PRIVACY NOTICE: 
Slack collects and receives information through operating the Services and Websites, and through other interactions with Slack. This information includes Customer Data and Other Information. Slack uses this information to operate its Services, Websites and business. Customer Data is used by Slack in accordance with a Customer’s instructions, including to provide the Services, any applicable terms in the Customer Agreement, a Customer’s use of Services functionality and as required by applicable law. Other Information is used for legitimate interests, compliance with legal obligations, and direct marketing purposes. Slack shares and disclies this information as described in the Privacy Policy. Slack also takes security of data seriously and has received internationally recognised security certifications. Individuals in the European Economic Area, the United Kingdom, Brazil and across the globe have certain statutory rights in relation to their personal data. California law requires that Slack detail the categories of personal information that it collects and discloses for certain ‘business purposes’. California consumers have the right to request to know more details about the categories or specific pieces of personal information that we collect, to delete their personal information, to opt out of any ‘sales’, to know and opt out of sharing of personal information for delivering advertisements on non-Slack websites, and to not be discriminated against for exercising these rights. Contact Slack at privacy@slack.com if you have any questions or to exercise your rights.

"""

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt2,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

import json
x = {
    "data policy" : ["text", "test"],
    "point2" : "text"
}

y = json.dumps(x)

#print(y)