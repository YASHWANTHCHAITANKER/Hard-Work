# Importing necessary libraries
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# Load true and fake datasets
true_data = pd.read_csv('true.csv')
fake_data = pd.read_csv('fake.csv')

# Add labels to the datasets
true_data['label'] = 'real'
fake_data['label'] = 'fake'

# Combine the datasets
data = pd.concat([true_data, fake_data], ignore_index=True)

# Preprocess the text data
def preprocess_text(text):
    # Remove URLs, mentions, and hashtags
    text = re.sub(r'http\S+|www\S+|@\S+|#\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

data['text'] = data['text'].apply(preprocess_text)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Initialize a TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # Limit the number of features to 5000

# Transform texts into TF-IDF feature vectors
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Initialize a Linear Support Vector Classifier
classifier = LinearSVC()

# Train the classifier
classifier.fit(X_train_tfidf, y_train)

# Predict labels for test set
predictions = classifier.predict(X_test_tfidf)

# Evaluate the classifier
print(classification_report(y_test, predictions))
