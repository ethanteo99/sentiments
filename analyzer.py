import nltk
import sys
from helpers import get_user_timeline

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        self.positives = []
        with open('positive-words.txt') as positive:
            for line in positive:
                if not line.startswith(';'):
                    self.positives.append(line.strip())
        
        self.negatives = []
        with open('negative-words.txt') as negative:
            for line in negative:
                if not line.startswith(';'):
                    self.negatives.append(line.strip())

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
         # split a tweet into a list of words (shorter strings)
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
    
        # initial score is neutral
        score = 0
    
        # iterate over tokens
        for token in tokens:
            # make all tokens lowercase
            token.lower()
    
            # assign each word in text a value (-1, 0, 1)
            if token in self.positives:
                score += 1
            elif token in self.negatives:
                score -= 1
    
        # calculate text's total score
        return score
    
    def checkTweet(self, text):
        
        tweets = get_user_timeline(text, 50)
        if tweets == None:
            sys.exit("Error")    
            
        for tweet in tweets:
            score = 0
            tokenizer = nltk.tokenize.TweetTokenizer()  
            tokens = tokenizer.tokenize(tweet)
            
            for word in tokens:
                if word in self.positives:
                    score += 1
                if word in self.negatives:
                    score -= 1
                
            if score > 0:
                return 1
            elif score < 0:
                return -1
            else:
                return 0
        
        
