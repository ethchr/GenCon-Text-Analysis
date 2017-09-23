# GenCon-Text-Analysis
I'm going to use Python/R to conduct textual analysis of sermons given at the semi-annual LDS general conferences. 

## Purpose
I want to learn how to do textual analysis, but so far in my academic research I haven't found a valid reason to do so. This will provide the opportunity to learn the skills and also may show cool insights into the evolution of LDS preaching over time.

This will be a way for me to mark down how I did everything and what I learned.

Note that currently, I am using this readme file as notes about what I need to figure out. I will soon separate those notes into a separate file to clean this one up. 

##  Steps
1. Download the data
  * This is where I am right now. My goal through the end of September is to learn how to web scrape at least the conference addresses that are hosted at lds.org/general-conference/conference?lang=eng. These are from April 1971 to the present (this is currently 94 conferences with at least 20 or so sermons per conference, so I am dealing with a potential corpora of ~2000 unique documents). 
     * There is a corpus created by a BYU linguistics professor that contains discourses as far back as 1850. I can't download from this source, but I believe I can recreate it at least as far as 1930 or so through other digital sources, and maybe 1900 through print (this would be somewhat risky). 
  * I need to learn how to tell Python where to start scraping on the page. Unlike other web datasources I have used, these websites are quite complex and there is a lot of extraneous coding that I need to ignore. 
2. Organize and clean the data
  * The lds.org data files will come full of what I believe is extraneous XML coding (I should ask Wes if this is true). I need to remove it. 
  * Something that I need to decide on is what to do with pictures. I don't think they are repetitively used enough to matter tracking them, but it could be fun to see when they started being used, etc. 
  * I need to tokenize the texts to some extent for textual analysis.
  * I also need to somehow create a database of the talks themselves. Afterall, a significant detail about this is that I want to see diffs between years, speakers, etc.
      * What this probably entails is doing the text analysis at the document level and then putting that information in a dataframe where each talk is an observation. 
      * I want the relationships between the various speakers as well (This will take time if I want to see everything they did, so lets just start with figuring out who was in the quorum with them and when). I may need to create a relationship dataframe for each conference (the brute force method), or some sort of relationship query - check who was an X in YYYY year.
      * I should ask Clark to set up some sort of SQL server for me so that I can store this on that server and get SQL practice at the same time. 
      
3. Analysis
 * I have a huge list of topics to look at, including: the use of passive voice, scriptures quoted, quotation of other GAs, quotations of nonmembers, topic trends (emergency preparedness?), etc. Will detail more once I actually have the data haha. 
4. Reporting
 * The first reporting I will probably do is simple word bubbles, which can be done for free elsewhere but I want to learn how to do them.
 * later reporting should include graphs of various sorts, this will be my practice with datavis.
