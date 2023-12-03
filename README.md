# Haiku Generator and Analyzer Project README

## Abstract
This project combines the worlds of Artificial Intelligence and poetry by creating a haiku generator. Using Rob Gonsalves' Deep Haiku Llama 2 model as a foundation, we trained our dataset to generate haikus. The project involves a blend of technologies including Google Colab, Flask server, and a Streamlit app, creating an AI-powered tool that crafts haikus in the traditional 5-7-5 syllable structure, a mixture of technology and the linguistic arts.

## Data Description
Our dataset, sourced from Kaggle ([Haiku Dataset 1](https://www.kaggle.com/datasets/bfbarry/haiku-dataset) and [Haiku Dataset 2](https://www.kaggle.com/datasets/hjhalani30/haiku-dataset)), comprises a diverse collection of haikus. It contains a comprehensive collection of haikus, providing a rich foundation for training the AI model. This dataset was integral in training the model to understand and generate haikus adhering to the traditional structure and thematic elements.

## Algorithm Description
The core algorithm of this project is based on the Deep Haiku Llama 2 model developed by Rob Gonsalves. This model has been specially fine-tuned to generate rhythmic prose, particularly haikus. The algorithm processes the dataset through several steps, including punctuation addition, keyword extraction, quality filtering, and syllable counting, ensuring the generation of high-quality haikus.

## Tools Used
- **LlamaCPP Model**: Employed for haiku generation in Google Colab.
- **Flask**: Serves as the backend server, handling requests for haiku generation.
- **ngrok**: Provides a public URL to access the Flask app over the internet.
- **Streamlit**: Used to create a user-friendly interface for interacting with the Flask server, allowing users to input topics and receive haikus along with sentiment analysis and word cloud visualization.
- **Google Colab**: Provides a cloud-based environment for running the LlamaCPP model due to GPU constraints.

## Work Done
- **LlamaCPP Model Initialization and Haiku Generation**: Configured the LlamaCPP model in Google Colab for generating haikus on various topics.
- **Flask Web Server**: Developed a Flask app with an endpoint `/generate_haiku` to produce haikus based on user inputs.
- **ngrok Configuration**: Enabled internet access to the Flask app through a public URL.
- **Streamlit Application**: Created a user interface for users to request haikus, featuring sentiment analysis and word cloud visualization.

## Ongoing Tasks and Constraints
- **Quality Assessment and Prompt Tuning**: Continuously working on improving the quality of the haikus through prompt optimization.
- **Streamlit App Enhancements**: Enhancing the UI/UX of the Streamlit application and refining features like sentiment analysis and word cloud visualization.
- **GPU Resource Constraints**: Currently running the project on Google Colab due to limited GPU resources, affecting scalability and performance.

## GitHub Repository
The complete code and documentation for this project are available at [HaikuGenerator on GitHub](https://github.com/priteshshah96/HaikuGenerator).

## Acknowledgements
Special thanks to Kaggle for providing the datasets that were instrumental in training our model. Also, a note of gratitude to Rob Gonsalves for his foundational work on the [Deep Haiku project](https://github.com/robgon-art/DeepHaiku) and his contributions to the field.
