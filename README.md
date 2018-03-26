# GenCon-Text-Analysis
I'm going to use Python/R to conduct textual analysis of sermons given at the semi-annual LDS general conferences.

## Purpose
I want to learn how to do textual analysis, but so far in my academic research I haven't found a valid reason to do so. This will provide the opportunity to learn the skills and also may show cool insights into the evolution of LDS preaching over time.

This will be a way for me to mark down how I did everything and what I learned.

Note that currently, I am using this readme file as notes about what I need to figure out. I will soon separate those notes into a separate file to clean this one up.

##  Steps
1. Download the data
  * I have downloaded all of the talks from April 1971 - April 2017 that are hosted on lds.org. I have a total of 3736 documents. This is enough for my immediate purposes, but eventually I plan to use the conference reports hosted on archive.org to go back to 1880. There is also a periodicals section on archive.org that could provide extra data.
  * All of the metadata that I have is in the file `talktitles.csv`. This is not quite enough info, I don't have which session it was, position in the session, I have to extrapolate the conference month and year from the URL. I also don't know the title of the author, that's included in the metadata on each url, but it has eluded me so far. But this file has enough info to get me started, and if I go back to get more metadata, I shouldn't need to redo any of those files.

2. Organize and clean the data
  * First Priority: I need to clean the data. For most of my purposes, I need to delete any footnotes in the text as well as the footnotes themselves. I might need to delete quotations as well(but should probably be the step after footnotes). I feel like this is easier in R than Python. I should probably resave them as "cleaned" versions.
  * I need to decide which articles to exclude and how. My thoughts are to use the titles to remove anything with "Church Auditing", "Statistical Report", or "Sustaining of Church Officers" (that last one might be titled a little fuzzy over time).
  * I need to figure out how to do "triples"
  * I need to tokenize the texts to some extent for textual analysis.
  * I also need to somehow create a database of the talks themselves.
  * Afterall, a significant detail about this is that I want to see diffs between years, speakers, etc.
      * What this probably entails is doing the text analysis at the document level and then putting that information in a dataframe where each talk is an observation.
      * I want the relationships between the various speakers as well (This will take time if I want to see everything they did, so lets just start with figuring out who was in the quorum with them and when). I may need to create a relationship dataframe for each conference (the brute force method), or some sort of relationship query - check who was an X in YYYY year.
      * I need to think about storing this in an actual database rather than just on my computer in files.

3. Analysis
 * I have a huge list of topics to look at, including: the use of passive voice, scriptures quoted, quotation of other GAs, quotations of nonmembers, topic trends (emergency preparedness?), etc. Will detail more once I actually have the data haha.
 * Pictures? Not included in my texts, but I could grab them later.
 * Neural network of triples to replace naive markov-chain for twitterbot.
4. Reporting
 * The first reporting I will probably do is simple word bubbles, which can be done for free elsewhere but I want to learn how to do them.
 * later reporting should include graphs of various sorts, this will be my practice with datavis.
 *
