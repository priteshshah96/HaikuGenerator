import streamlit as st
import requests
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_haiku_from_colab(topic):
    colab_url = 'http://7a7a-104-198-100-206.ngrok-free.app/generate_haiku'
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
