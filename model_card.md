# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
 
Name: CyberViber

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

CyberViber picks the top 5 songs from a small catalog that best match a user's stated genre, mood, and energy preferences. It doesn't learn over time — you tell it what you like and it scores every song against that. It's a classroom project, not a real app.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Every song gets a score. Genre match is worth the most (2 pts), then mood (1 pt). Energy, valence, and acousticness each add a small bonus based on how close the song is to what you want — a perfect match gives full points, a bad match gives near zero. The songs are sorted by score and the top 5 are shown, each with a short reason explaining why it was picked.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

18 songs in `data/songs.csv` — started with 10, added 8 more. Covers genres like pop, lofi, rock, metal, jazz, EDM, hip-hop, folk, and r&b. Moods include happy, chill, intense, sad, and romantic. Coverage is uneven though — lofi has 3 songs, most others have just 1. Genres like Latin, reggae, and blues aren't represented at all.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

Works well when the user's genre is well-covered in the catalog. High-Energy Pop and Chill Lofi both gave results that felt right immediately. Every result comes with a reason, so it's easy to see why a song was picked. Very different profiles (lofi vs. metal) never overlap in their results, which makes sense.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest issue is **catalog imbalance**. Lofi has 3 songs, metal has 1. So a lofi user gets 3 strong matches while a metal user gets 1 and then the system falls back to other genres. The algorithm isn't broken — the data just doesn't cover every genre equally. Users with niche tastes get worse results even though the scoring treats everyone the same way.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Tested three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Metal. Checked whether the top 5 results matched what a real listener would expect.

Pop and Lofi both felt right. Surprising moment: "Storm Runner" (rock) snuck into the Pop top 5 with no genre or mood match — just a high energy score. Shows that one strong signal can override everything else in a small catalog.

Metal was the most revealing. "Iron Will" scored nearly perfect, but spots 2–5 were all rock, EDM, and pop. The algorithm did its job — the catalog just didn't have enough metal songs to fill the list.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

- Add more songs per genre so every genre has fair coverage.
- Block songs with no genre match from appearing in the top 5.
- Let users set an energy range instead of one exact number.
- Add variety so the top 5 don't all sound identical.
- Support multiple favorite genres or moods in one profile.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

A recommender is basically just a set of rules someone decided on. Weighting genre at 2.0 is a choice, not a fact, someone else could weigh it differently and also be right. The most surprising thing was that the unfairness came from the data, not the code. When Spotify doesn't "get" a niche genre, it might not be a bad algorithm, there just might not be enough of that music in the system.
