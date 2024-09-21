import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def detect_sentiment(input_text):
    # Initialize VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Analyze sentiment of the input text
    sentiment_score = sia.polarity_scores(input_text)
    
    # Determine sentiment label based on compound score
    if sentiment_score['compound'] >= 0.05:
        sentiment_label = 'positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment_label = 'negative'
    else:
        sentiment_label = 'neutral'
    
    return sentiment_label

def classify_words(input_text):
    # Define lists of useful (good) and unuseful (bad) words
    good_words = ['credible', 'reliable', 'trustworthy', 'accurate', 'factual', 'valid', 'confirmed']
    bad_words = ['fake', 'false', 'misleading', 'unverified', 'hoax', 'deceptive', 'bogus']
    
    # Tokenize the input text into words
    words = input_text.lower().split()
    
    # Initialize lists to store detected useful and unuseful words
    detected_good_words = []
    detected_bad_words = []
    
    # Detect sentiment of the input text
    sentiment = detect_sentiment(input_text)
    
    # Classify each word based on sentiment
    for word in words:
        # Check if the word is in the list of good words
        if word in good_words and sentiment == 'positive':
            detected_good_words.append(word)
        # Check if the word is in the list of bad words
        elif word in bad_words and sentiment == 'negative':
            detected_bad_words.append(word)
    
    return detected_good_words, detected_bad_words

# Take input from the user
input_text = input("Enter the text: ")

# Classify words as useful (good) or unuseful (bad)
good_words, bad_words = classify_words(input_text)

# Display the classified useful and unuseful words
print("Useful (Good) Words:", good_words)
print("Unuseful (Bad) Words:", bad_words)
