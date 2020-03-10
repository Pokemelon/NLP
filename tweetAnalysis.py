#Analyzing hashtag popularity in tweets ans showing it in a barplot

tweets = ["I love #berlin, it's the best city to live in! #berlin #traveling #adventure", 
"Coming to this town was the best desicion I have ever made! Thanks @marty123 #berlin #travel #clubbing",
"They didn't let us into #berghain, no reason! Told you so @marty123! #clubbing #berlin"]
 
# Import the necessary modules

from nltk import re
import nltk
import matplotlib
import matplotlib.pyplot as plt



#indentify all hashtags 
hashpattern = r"#\w+"

hashtags = []

for t in tweets:
	hashtags.extend(re.findall(hashpattern, t))
	
#counting and displaying the freqency of the hashtags

freq = nltk.FreqDist(hashtags)

for key,val in freq.items():
 
    print (str(key) + ':' + str(val))
	
#display the freqency of the hashtags on a chart
plt.hist(hashtags)
plt.show()