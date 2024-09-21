import numpy as np
import tensorflow as tf
from tensorflow.keras import *
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping

# Sample data (replace with your actual data)
reviews = ["This product is amazing!",#1
    "The quality is terrible.",#0
    "I'm really satisfied with this purchase.",#1
    "Worst product ever, complete waste of money.",#0
    "Highly recommend this product to everyone.",#1
    "Not satisfied with the quality of the product.",#0
    "Couldn't be happier with my purchase.",#1
    "Terrible experience, would not recommend to anyone.",#0
    "Amazing value for the price.",#1
    "Product arrived damaged, very disappointed.",#0
    "This product exceeded my expectations!"]#1
labels = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # 1 for positive, 0 for negative

# Tokenization and padding
vocab_size = 1000
embedding_dim = 16
max_length = 20
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(reviews)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(reviews)
padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# Model definition
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim),  # Removed input_length parameter
    LSTM(32),  # Reduced LSTM units
    BatchNormalization(),  # Batch normalization layer
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Model training
num_epochs = 20  # Increase epochs if needed
history = model.fit(padded, labels, epochs=num_epochs, validation_split=0.2, callbacks=[early_stopping])

# Example prediction
test_reviews = ["This product is great!",
                "I am very dissappointed with this purchase."]
test_sequences = tokenizer.texts_to_sequences(test_reviews)
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

predictions = model.predict(test_padded)
for i in range(len(test_reviews)):
    if predictions[i] >= 0.5:
        print(test_reviews[i], "--> Positive")
    else:
        print(test_reviews[i], "--> Negative") 