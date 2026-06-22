import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page Title
st.title("🤖 FAQ Chatbot")
st.write("Ask questions about AI, Python, GitHub, Streamlit, and more.")

# Sidebar
st.sidebar.title("Topics")
st.sidebar.write("Artificial Intelligence")
st.sidebar.write("Machine Learning")
st.sidebar.write("Python")
st.sidebar.write("GitHub")
st.sidebar.write("Streamlit")

# FAQ Dataset
faqs = {
    "What is AI?":
    "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",

    "What are the types of AI?":
    "The main types of AI are Narrow AI, General AI, and Superintelligence.",

    "What is Machine Learning?":
    "Machine Learning allows systems to learn from data and improve their performance without being explicitly programmed.",

    "What is Deep Learning?":
    "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",

    "What is NLP?":
    "Natural Language Processing enables computers to understand and process human language.",

    "What is Computer Vision?":
    "Computer Vision enables machines to interpret and understand images and videos.",

    "What is Python?":
    "Python is a popular programming language known for its simplicity and versatility.",

    "What is GitHub?":
    "GitHub is a platform for version control and collaboration using Git.",

    "What is Streamlit?":
    "Streamlit is a Python framework used to build interactive web applications quickly.",

    "What is Data Science?":
    "Data Science involves extracting insights and knowledge from data using scientific methods and algorithms.",

    "What is Generative AI?":
    "Generative AI creates new content such as text, images, audio, and code.",

    "What is a Neural Network?":
    "A Neural Network is a computational model inspired by the human brain.",

    "What is Supervised Learning?":
    "Supervised Learning is a machine learning approach that learns from labeled data.",

    "What is Unsupervised Learning?":
    "Unsupervised Learning finds patterns and relationships in unlabeled data.",

    "What is Reinforcement Learning?":
    "Reinforcement Learning is a machine learning technique where an agent learns through rewards and penalties."
}

# User Input
user_question = st.text_input("Ask your question:")

# Ask Button
if st.button("Ask"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        questions = list(faqs.keys())

        vectorizer = TfidfVectorizer()

        faq_vectors = vectorizer.fit_transform(questions)

        user_vector = vectorizer.transform([user_question])

        similarities = cosine_similarity(
            user_vector,
            faq_vectors
        )

        best_match_index = similarities.argmax()

        score = similarities[0][best_match_index]

        if score > 0.15:

            best_question = questions[best_match_index]

            st.info(f"Matched FAQ: {best_question}")

            st.write(f"Similarity Score: {score:.2f}")

            st.success(faqs[best_question])

        else:
            st.warning(
                "Sorry, I couldn't find a suitable answer for your question."
            )