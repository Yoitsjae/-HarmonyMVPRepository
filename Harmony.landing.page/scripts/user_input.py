def get_user_input(genre_artists):
    print("Welcome to Harmony! Let's find some great music for you.")
    while True:
        genre = input("Please enter your favorite music genre: ").lower()
        if genre in genre_artists:
            break
        else:
            print("Sorry, that genre is not supported. Please try again.")

    artists = []
    print("Now, please enter the names of five artists you enjoy listening to.")
    for i in range(5):
        artist = input(f"Artist {i+1}: ")
        artists.append(artist)
    return genre, artists

