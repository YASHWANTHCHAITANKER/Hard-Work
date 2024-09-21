# import nltk
# import sys
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.util import mark_negation
# import csv

# # Download necessary NLTK resources
# nltk.download('punkt')

# # Load words and their sentiments from the CSV file
# def load_sentiment_words(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         return {row['word']: row['sentiment'] for row in reader}

# # Load your dataset
# sentiment_words = load_sentiment_words('word_sentiment.csv')  # Replace with your actual filename

# # Function to determine sentiment of a word
# def get_word_sentiment(word):
#     return sentiment_words.get(word, 'undefined')  # Default to 'undefined' if word is not found

# # Function to analyze sentiment of a sentence
# def analyze_sentiment(sentence):
#     words = word_tokenize(sentence.lower())
#     words = mark_negation(words)
#     sentiment = [(word, get_word_sentiment(word)) for word in words]
#     return sentiment

# # Example usage
# print("Enter text (press Enter to exit):")
# while True:
#     text = input().strip()
#     if not text:
#         break
#     sentiment_analysis = analyze_sentiment(text)
#     print("Word\t\tSentiment")
#     for word, sentiment in sentiment_analysis:
#         print(f"{word}\t\t{sentiment}")


def load_sentiment_words(filename):
    sentiment_words = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split(',')
            for i in range(0, len(words), 2):
                if i + 1 < len(words):
                    sentiment_words[words[i]] = words[i + 1]
    return sentiment_words

def analyze_sentiment(sentence, sentiment_words):
    words = sentence.strip().split()
    print("Word            Sentiment")
    for word in words:
        sentiment = sentiment_words.get(word, "undefined")
        print(f"{word:<16}{sentiment}")

# Load sentiment words from CSV
sentiment_words = load_sentiment_words('word_sentiment.csv')

# Take input from the user
user_input = input("Enter text: ")

# Perform sentiment analysis
analyze_sentiment(user_input, sentiment_words)

