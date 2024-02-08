from genre_artists import genre_artists
from user_input import get_user_input
from recommendation import generate_recommendations

def main():
    genre, artists = get_user_input(genre_artists)
    recommendations = generate_recommendations(genre, artists)
    print("\nBased on your input, here are some recommendations for you:")
    for idx, artist in enumerate(recommendations, 1):
        print(f"{idx}. {artist}")

if __name__ == "__main__":
    main()

