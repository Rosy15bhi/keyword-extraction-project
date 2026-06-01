import streamlit as st
from rake_nltk import Rake
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

st.title("🔑 Keyword Extraction Project")
st.subheader("Data Mining and Text Analytics – IULM University")

text = st.text_area("Enter your text here:", height=200)

if st.button("Extract Keywords"):
    if text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🟠 RAKE Results")
            rake = Rake()
            rake.extract_keywords_from_text(text)
            phrases = rake.get_ranked_phrases_with_scores()
            for score, phrase in phrases:
                st.write(f"**{score:.2f}** - {phrase}")

        with col2:
            st.markdown("### 🔵 TF-IDF Results")
            vectorizer = TfidfVectorizer(stop_words="english")
            tfidf_matrix = vectorizer.fit_transform([text])
            feature_names = vectorizer.get_feature_names_out()
            scores = tfidf_matrix.toarray()[0]
            keywords = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)
            for word, score in keywords[:10]:
                st.write(f"**{score:.4f}** - {word}")
            