# Reflection: Profile Output Comparisons

## High-Energy Pop vs. Chill Lofi

These two profiles sit at opposite ends of the energy spectrum (0.88 vs. 0.38), and the outputs reflect that completely. High-Energy Pop surfaces driving, danceable tracks with high valence, while Chill Lofi pulls slow, acoustic, low-energy songs. What makes sense here is that energy is doing the heavy lifting for differentiation — even within the same genre a high-energy song and a low-energy song feel like totally different listening experiences, and the proximity scoring correctly separates them. It makes sense that no song appears in both top-5 lists because the energy ranges barely overlap.

## Chill Lofi vs. Deep Intense Metal

Both profiles get a strong #1 result (Library Rain / Midnight Coding at 4.92, Iron Will at 4.98), but the depth of same-genre matches drops off sharply for Metal. Chill Lofi has three lofi songs in the catalog, so positions 1–3 are all solid genre matches. Metal has only one, so positions 2–5 come from rock, EDM, and pop. This comparison illustrates that the *algorithm* behaves identically for both users — it rewards genre matches with +2.0 in both cases — but the *experience* diverges because the dataset is imbalanced. The lofi user is being served by catalog coverage, not by a better algorithm.

## High-Energy Pop vs. Deep Intense Metal

Both profiles target high energy (0.88 and 0.96), but the mood and genre signals pull them in different directions. High-Energy Pop wants happy + genre-matched pop; Deep Intense Metal wants intense + genre-matched metal. The interesting overlap is that "Gym Hero" (pop, intense, energy 0.93) appears in the Metal top 5 — it matches the mood and energy but not the genre. This shows that when genre coverage is thin, mood and energy proximity can carry a song across genre lines. For a real listener this would likely feel wrong ("why is a pop song in my metal playlist?"), which points to a future improvement: adding a hard genre filter as a minimum threshold rather than just a bonus.
