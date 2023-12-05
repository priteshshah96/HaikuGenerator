import streamlit as st
import requests
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_haiku_from_colab(topic):
    colab_url = 'http://a47b-34-27-248-21.ngrok-free.app/generate_haiku'
    params = {'topic': topic}
    response = requests.get(colab_url, params=params)
    return response.json()['haikus']

def generate_wordcloud(text):
    if not text or text.isspace():
        return None
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    plt.figure(figsize=(7,5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt

def count_syllables(word):
    vowels = "aeiouy"
    num_vowels = 0
    last_was_vowel = False
    for wc in word:
        found_vowel = False
        for v in vowels:
            if v == wc and last_was_vowel is False:
                found_vowel = True
                last_was_vowel = True
                num_vowels += 1
                break
        if not found_vowel:
            last_was_vowel = False

    if word.endswith("e"):
        num_vowels -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        num_vowels += 1
    if num_vowels == 0:
        num_vowels = 1
    return num_vowels

def check_haiku_structure(haiku):
    lines = haiku.split(' / ')
    if len(lines) != 3:
        return False, "A haiku must have exactly three lines."

    syllable_counts = []
    for line in lines:
        words = TextBlob(line).words
        line_syllables = sum(count_syllables(word) for word in words)
        syllable_counts.append(line_syllables)

    if syllable_counts == [5, 7, 5]:
        return True, "This is a 5-7-5 haiku."
    else:
        return False, f"Haiku structure not 5-7-5. Detected syllable structure: {syllable_counts}"

def app():
    st.title('Haiku Generator and Analyzer')

    # Initial Message
    placeholder = st.empty()
    placeholder.text("We don't read and write poetry because it's cute. We read and write poetry because...")
    
    topic = st.text_input("Enter a topic for the Haiku:", "")

    if st.button('Generate Haiku'):
        placeholder.empty()  # Remove the initial message

        with st.spinner("Generating Haiku..."):
            haikus = get_haiku_from_colab(topic)

        for haiku in haikus:
            st.write(haiku)

            # Check Haiku Structure
            is_haiku, structure_message = check_haiku_structure(haiku)
            st.write(f"Haiku Structure Check: {structure_message}")

            analysis = TextBlob(haiku)
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity
            # Categorize sentiment
            if polarity > 0.1:
                sentiment = "Positive"
            elif polarity < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            
            st.write(f"Sentiment Analysis: {sentiment} (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")

            st.write("Word Cloud:")
            fig = generate_wordcloud(haiku)
            if fig:
                st.pyplot(fig)

if __name__ == "__main__":
    app()
