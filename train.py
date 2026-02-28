import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv('../data/movies.csv')

# Combine features
movies['combined'] = movies['genre'] + " " + movies['keywords']

# Convert text to vectors
cv = CountVectorizer()
vectors = cv.fit_transform(movies['combined'])

# Calculate similarity
similarity = cosine_similarity(vectors)

# Save model
pickle.dump((movies, similarity), open('../model/recommender.pkl', 'wb'))

print("Model trained and saved!")