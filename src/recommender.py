from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs.csv and returns a list of song dicts with numeric fields converted."""
    import csv
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user prefs using genre/mood matching and numerical proximity."""
    score = 0.0
    reasons = []

    # Genre match: +2.0 (strongest categorical signal)
    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: +1.0
    if song.get("mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy proximity: +1.0 × (1 − |Δenergy|)
    if "energy" in user_prefs:
        energy_pts = 1.0 - abs(song["energy"] - user_prefs["energy"])
        score += energy_pts
        reasons.append(f"energy proximity (+{energy_pts:.2f})")

    # Valence proximity: +0.5 × (1 − |Δvalence|)
    if "valence" in user_prefs:
        valence_pts = 0.5 * (1.0 - abs(song["valence"] - user_prefs["valence"]))
        score += valence_pts
        reasons.append(f"valence proximity (+{valence_pts:.2f})")

    # Acousticness proximity: +0.5 × (1 − |Δacousticness|)
    if "acousticness" in user_prefs:
        acoustic_pts = 0.5 * (1.0 - abs(song["acousticness"] - user_prefs["acousticness"]))
        score += acoustic_pts
        reasons.append(f"acousticness proximity (+{acoustic_pts:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song with score_song, sorts by score descending, and returns the top k results."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
