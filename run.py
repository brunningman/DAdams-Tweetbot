'''
Douglas Adams Tweetbot
This program at it's base level will scrape goodreads.com or similar 
for Douglas Adams quotes, shuffle them around with a Markov chain,
device and output < 144 character tweets.

Bonus for Trump formatting option
'''

from mrkov_chain.cc_markov import MarkovChain
import fetch_data
from bs4 import BeautifulSoup