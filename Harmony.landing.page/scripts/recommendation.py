import random

def generate_recommendations(genre_artists, genre, artists):
    recommendations = []
    for artist in artists:
        similar_artists = [a for a in genre_artists[genre] if a != artist]
        recommendations.extend(random.sample(similar_artists, min(2, len(similar_artists))))
    return recommendations
