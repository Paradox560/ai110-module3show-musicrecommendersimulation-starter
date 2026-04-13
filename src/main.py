"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate
from recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.88,
        "valence": 0.82,
        "acousticness": 0.12,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "valence": 0.58,
        "acousticness": 0.78,
    },
    "Deep Intense Metal": {
        "genre": "metal",
        "mood": "intense",
        "energy": 0.96,
        "valence": 0.32,
        "acousticness": 0.07,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        print(f"\n{'='*50}")
        print(f"Profile: {profile_name}")
        print(f"{'='*50}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        table_rows = []
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            table_rows.append([
                rank,
                song["title"],
                song["artist"],
                f"{score:.2f}",
                explanation,
            ])
        headers = ["#", "Title", "Artist", "Score", "Reasons"]
        print(tabulate(table_rows, headers=headers, tablefmt="rounded_outline"))
        print()


if __name__ == "__main__":
    main()
