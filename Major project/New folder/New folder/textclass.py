# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.util import mark_negation

# # Download necessary NLTK resources
# nltk.download('punkt')

# # Load positive, negative, and neutral word lists from your dataset
# def load_sentiment_words(filename):
#     with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding explicitly
#         return set(word.strip() for word in file.readlines())

# # Load your dataset
# sentiment_words = load_sentiment_words('tweets.csv')  # Replace 'tweets.csv' with your actual filename

# # Function to determine sentiment of a word
# def get_word_sentiment(word):
#     if word in sentiment_words:
#         if word.startswith('positive'):
#             return 'positive'
#         elif word.startswith('negative'):
#             return 'negative'
#         elif word.startswith('neutral'):
#             return 'neutral'
#     return 'undefined'  # You may choose to handle undefined words differently

# # Function to analyze sentiment of a sentence
# def analyze_sentiment(sentence):
#     words = word_tokenize(sentence.lower())
#     words = mark_negation(words)
#     sentiment = [(word, get_word_sentiment(word)) for word in words]
#     return sentiment

# # Example usage
# text = input("Enter text: ")
# sentiment_analysis = analyze_sentiment(text)
# print("Word\t\tSentiment")
# for word, sentiment in sentiment_analysis:
#     print(f"{word}\t\t{sentiment}")



## method 2

# import nltk
# import sys
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.util import mark_negation

# # Download necessary NLTK resources
# nltk.download('punkt')

# # Load positive, negative, and neutral word lists from your dataset
# def load_sentiment_words(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return set(word.strip() for word in file.readlines())

# # Load your dataset
# sentiment_words = load_sentiment_words('tweets.csv')  # Replace 'tweets.csv' with your actual filename

# # Function to determine sentiment of a word
# def get_word_sentiment(word):
#     if word in sentiment_words:
#         if word.startswith('positive'):
#             return 'positive'
#         elif word.startswith('negative'):
#             return 'negative'
#         elif word.startswith('neutral'):
#             return 'neutral'
#     return 'undefined'  # You may choose to handle undefined words differently

# # Function to analyze sentiment of a sentence
# def analyze_sentiment(sentence):
#     words = word_tokenize(sentence.lower())
#     words = mark_negation(words)
#     sentiment = [(word, get_word_sentiment(word)) for word in words]
#     return sentiment

# # Example usage
# print("Enter text:")
# text = sys.stdin.readline().strip()
# if text:
#     sentiment_analysis = analyze_sentiment(text)
#     print("Word\t\tSentiment")
#     for word, sentiment in sentiment_analysis:
#         print(f"{word}\t\t{sentiment}")
# else:
#     print("No text entered.")


## method dnr

