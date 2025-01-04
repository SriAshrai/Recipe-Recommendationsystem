Personalized Recipe Recommendation 
System
Objective
The goal of this project is to build a personalized recipe recommendation system that suggests 
recipes based on user preferences, ingredient availability, and cuisine types. The system uses 
both content-based and collaborative filtering techniques to deliver accurate and relevant 
recommendations.
Features
1. Content-Based Filtering
o Leverages recipe ingredients and cuisine types.
o Recommends recipes similar to user-preferred recipes.
2. Collaborative Filtering
o Uses user ratings of recipes.
o Suggests recipes based on similar user preferences.
3. Customization
o Handles dietary restrictions, cooking time, and difficulty levels.
o Incorporates user-specific preferences for tailored recommendations.
4. Scalability
o Designed to handle large datasets of recipes and user interactions.
Dataset
Recipes Dataset
 Contains details about recipes including:
o recipe_id
o name
o ingredients
o cuisine
o minutes (cooking time)
Interactions Dataset
 Records user interactions with recipes:
o user_id
o recipe_id
o rating
Approach
1. Data Preprocessing
 Cleaned and filtered datasets to remove null values.
 Combined multiple features for content-based similarity calculations.
2. Recommendation Algorithms
 Content-Based Filtering:
o Calculated cosine similarity of recipe features.
o Ranked recipes based on similarity to user-preferred recipes.
 Collaborative Filtering:
o Implemented using Singular Value Decomposition (SVD).
o Predicted user ratings for recipes.
3. Example Query
 Demonstrated the system with sample user preferences.
 Returned top 10 recommendations for both content-based and collaborative methods.
How to Run
1. Dependencies:
o Python 3.x
o Libraries: pandas, numpy, scikit-learn, surprise
2. Steps:
o Place the recipes.csv and interactions.csv files in the project directory.
o Run the script using:
python recommendation_system.py
o Review the recommendations in the console output.
Challenges
 Sparse Data:
o Addressed missing ratings by defaulting to average user ratings.
 Scalability:
o Optimized preprocessing for large datasets.
Future Enhancements
 NLP Integration:
o Extract user preferences from textual reviews or feedback.
 Advanced Models:
o Implement neural collaborative filtering or transformer-based models.
 User Interface:
o Develop an interactive dashboard for better user experience.
Example Outputs
Content-Based Recommendations:
Recipe ID Name
101 Spaghetti Bolognese
203 Vegan Buddha Bowl
Collaborative Recommendations:
Recipe ID Name
315 Chicken Tikka
124 Avocado Toast
Contact
For queries or feedback, contact 
[sriashraidevulapally@gmail.com/https://www.linkedin.com/in/sri-ashrai-devulapally-
515789269/]