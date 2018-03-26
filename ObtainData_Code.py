##Imports that I need to pull the data:
import requests
from bs4 import BeautifulSoup
import os
import time
import csv
#These things need to stay out of the loop
prefix = "https://www.lds.org"
metalist = []
totalcounter = 0


#####https://archive.org/details/conferencereport
##This sucker has EVERY conference report since 1880. And at least most of the time, there's a text file. Praises be.
#This makes things so much easier. Assuming I can trust the text, anyway
#Potential extension: https://archive.org/details/churchhistorylibraryperiodicals
#Old church magazines.
#Once I get into the analysis stage, see this:
#https://github.com/cbail/textnets


#Here's the overarching bit pulling from the all conferences page
#confurllist contains all of the conference specific urls to pull from.
urlm = 'https://www.lds.org/general-conference/conferences?lang=eng'
rm = requests.get(urlm)
htmlm = rm.text

soupm = BeautifulSoup(htmlm, "lxml")
confurllist = []
for t in soupm.find_all("div", class_= "year-line"):
    confurllist.append(prefix + t.find('a')['href'])


#I'm going to try to make it save all the files into a folder
save_path = 'C:/Users/Ethan/Documents/Github/GenCon-Text-Analysis/text_folder/'

#Now I need a loop through confurllist

for url in confurllist:
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    #Urls for the talks in a conference in urllist
    urllist = []
    for t in soup.find_all("div", class_="lumen-tile lumen-tile--horizontal lumen-tile--list"):
        urllist.append(prefix + t.find('a')['href'])
    for talk in urllist:
        url1 = talk
        r1 = requests.get(url1)
        html1 = r1.text
        soup1 = BeautifulSoup(html1, "lxml")
        block = soup1.find('div', class_="body-block")
        totalcounter = totalcounter + 1
        print(totalcounter)
        metalist.append([soup1.title.string, totalcounter, url])
        name_of_file = 'talk' + str(totalcounter)
        completename = os.path.join(save_path, name_of_file + ".txt")
        f = open(completename,"w")
        for par in block.find_all('p'):
            f.write('\n' + par.get_text().encode('cp1252', errors='replace').decode('cp1252'))
        f.close()
    print("You've finished" + str(totalcounter))
    time.sleep(5)

# I have the metadata in the list, I need to export it.
save_path_meta = 'C:/Users/Ethan/Documents/Github/GenCon-Text-Analysis/'
name_of_metafile = 'talktitles'
completenamemeta = os.path.join(save_path_meta, name_of_metafile + ".csv")

with open(completenamemeta, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(metalist)

#This meta data has the title (which is formatted "title - Author")
#I can split this to grab the author
#I don't have the year, conference (actually yes, contained in URL), or session yet.
#In the future, I don't have to write the files out, so I can grab the other
#info much more quickly.
