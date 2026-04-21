from sklearn.feature_extraction.text import TfidfVectorizer

# Read the input text
with open("data/sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words="english")

# Fit and transform the text
tfidf_matrix = vectorizer.fit_transform([text])

# Get words and their scores
feature_names = vectorizer.get_feature_names_out()
scores = tfidf_matrix.toarray()[0]

# Pair words with scores and sort them
keywords = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)

# Save results to file
with open("outputs/keywords_tfidf_output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("Extracted TF-IDF keywords:\n\n")
    for word, score in keywords[:10]:
        output_file.write(f"{score:.4f} - {word}\n")

# Print results in terminal
print("Extracted TF-IDF keywords:\n")
for word, score in keywords[:10]:
    print(f"{score:.4f} - {word}")

print("\nResults saved in: outputs/keywords_tfidf_output.txt")
