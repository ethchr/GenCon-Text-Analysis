##Imports that I need to pull the data:
import requests
from bs4 import BeautifulSoup

##Okay, this bit all works. url is a conference page with links, and url1 is a specific talk with text.
#These are just me working through the process, I will need to run some sort of loop on conference page links to get each individual talk.
url = 'https://www.lds.org/general-conference/2017/04?lang=eng'
url1 = 'https://www.lds.org/general-conference/2017/04/gathering-the-family-of-god?lang=eng'
r = requests.get(url)
r1 = requests.get(url1)
html = r.text
html1 = r1.text

#I don't know if "lxml" is the best choice, honestly its the default. Seems to work okay.
soup = BeautifulSoup(html, "lxml")
soup1 = BeautifulSoup(html1, "lxml")

soup.title
soup1.title
#Okay, so we see that each one has actually got the page we wanted.

talktiles = soup.find_all("div", class_="lumen-tile lumen-tile--horizontal lumen-tile--list")
len(talktiles)
#I was having problems earlier not capturing every talk link, this says I got it right.

#This ignores the talktiles object and just finds literally every link on the page. Given that it mixes mp3,mp4, text, and menu links, I'm not really sure that this is a good approach. Still, it gives a sense for the links on the page.
for link in soup.find_all('a'):
    print(link.get('href'))

prefix = "www.lds.org"
#All of the talk links need to have this prefix added before being used to scrape text.

####The code below is based on some demos, but it doesn't work yet for me.
#talksurls = {}
#for element in talktiles:
#    talksurls[element.a.get_text()]
#for element in talktiles:
#    talksurls[element.a.get_text()]["link"] = prefix + element.a["href"]
#for item in talksurls.keys():
#    print(item + ": " + "\n\t" + "link: " + talksurls[item]["link"] + "\n\n")
#### Ideally, that would give me a dictionary with each url I need from that conference.


############Just reading in the text:
print(soup1.get_text())
#This gets the text, and a whole lot more. Including conference (but NOT session), speaker, speaker's title, talk title, and topic tags assigned to talk on lds.org. The problem is that it includes a ton of extra stuff. So I'll need to pare away all the other stuff to get just the text, but at the same time dive into the other stuff to get those other parts. Will be a little tricky but we'll see.

#####Trying to save from ATOM back up to the github

#####It Worked
