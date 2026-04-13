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

ARTIST_REPEAT_PENALTY = 1.0
GENRE_REPEAT_PENALTY = 0.5


def apply_diversity_penalty(
    song: Dict,
    score: float,
    reasons: List[str],
    selected_artists: set,
    selected_genres: set,
) -> Tuple[float, List[str]]:
    """Reduces a song's score if its artist or genre is already in the selected results."""
    reasons = list(reasons)
    if song["artist"] in selected_artists:
        score -= ARTIST_REPEAT_PENALTY
        reasons.append(f"artist repeat penalty (-{ARTIST_REPEAT_PENALTY:.1f})")
    if song["genre"] in selected_genres:
        score -= GENRE_REPEAT_PENALTY
        reasons.append(f"genre repeat penalty (-{GENRE_REPEAT_PENALTY:.1f})")
    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, then greedily selects the top k using diversity-aware re-ranking.
    Each round, artist/genre penalties are applied to remaining candidates whose
    artist or genre is already represented in the selected list.
    """
    # Score all songs up front
    scored = [(song, *score_song(user_prefs, song)) for song in songs]

    selected = []
    selected_artists: set = set()
    selected_genres: set = set()
    remaining = list(scored)

    for _ in range(min(k, len(remaining))):
        best_idx = -1
        best_score = float("-inf")
        best_reasons: List[str] = []

        for i, (song, base_score, base_reasons) in enumerate(remaining):
            adj_score, adj_reasons = apply_diversity_penalty(
                song, base_score, base_reasons, selected_artists, selected_genres
            )
            if adj_score > best_score:
                best_score = adj_score
                best_idx = i
                best_reasons = adj_reasons

        song = remaining[best_idx][0]
        selected.append((song, best_score, ", ".join(best_reasons)))
        selected_artists.add(song["artist"])
        selected_genres.add(song["genre"])
        remaining.pop(best_idx)

    return selected
