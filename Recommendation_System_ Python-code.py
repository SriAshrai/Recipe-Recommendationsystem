import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

# Step 1: Load the Dataset
def load_data():
    recipes = pd.read_csv('recipes.csv')  # Replace with actual file path
    interactions = pd.read_csv('interactions.csv')  # Replace with actual file path
    return recipes, interactions

# Step 2: Preprocess the Data
def preprocess_data(recipes, interactions):
    recipes.dropna(subset=['ingredients', 'cuisine', 'minutes'], inplace=True)
    interactions.dropna(subset=['recipe_id', 'user_id', 'rating'], inplace=True)
    return recipes, interactions

# Step 3: Content-Based Filtering
def content_based_filtering(recipes, user_preferences):
    recipes['combined_features'] = recipes['ingredients'] + ' ' + recipes['cuisine']
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(recipes['combined_features'])
    similarity_matrix = cosine_similarity(count_matrix)

    user_favorites = recipes[recipes['recipe_id'].isin(user_preferences)]
    favorite_indices = user_favorites.index
    scores = similarity_matrix[favorite_indices].mean(axis=0)

    recommendations = recipes.iloc[np.argsort(-scores)][:10]
    return recommendations

# Step 4: Collaborative Filtering
def collaborative_filtering(interactions):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(interactions[['user_id', 'recipe_id', 'rating']], reader)
    algo = SVD()
    cross_validate(algo, data, cv=3, verbose=False)

    trainset = data.build_full_trainset()
    algo.fit(trainset)

    return algo

# Step 5: Generate Recommendations
def generate_recommendations(user_id, algo, recipes, user_preferences):
    top_n = []
    for recipe_id in recipes['recipe_id']:
        est_rating = algo.predict(user_id, recipe_id).est
        top_n.append((recipe_id, est_rating))

    top_n = sorted(top_n, key=lambda x: x[1], reverse=True)[:10]
    recommended_recipes = recipes[recipes['recipe_id'].isin([x[0] for x in top_n])]
    return recommended_recipes

# Example Queries
def example_query():
    recipes, interactions = load_data()
    recipes, interactions = preprocess_data(recipes, interactions)

    # User Preferences (Example)
    user_preferences = [1, 5, 12]  # Replace with actual recipe IDs the user likes
    user_id = 101

    # Content-Based Filtering
    content_recommendations = content_based_filtering(recipes, user_preferences)

    # Collaborative Filtering
    algo = collaborative_filtering(interactions)
    collaborative_recommendations = generate_recommendations(user_id, algo, recipes, user_preferences)

    return content_recommendations, collaborative_recommendations

if __name__ == "__main__":
    content_recommendations, collaborative_recommendations = example_query()
    print("Content-Based Recommendations:")
    print(content_recommendations)
    print("\nCollaborative Filtering Recommendations:")
    print(collaborative_recommendations)
