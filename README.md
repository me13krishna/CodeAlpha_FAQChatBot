# CodeAlpha FAQ ChatBot

A simple Streamlit-based FAQ chatbot that matches user questions against a curated FAQ dataset using TF-IDF vectorization and cosine similarity.

## Overview

This project demonstrates a lightweight question-answering workflow:

- The user enters a question in the chat interface.
- The app compares the question against a list of predefined FAQ prompts.
- The closest match is selected using cosine similarity.
- If the match score is high enough, the corresponding answer is shown.

## Features

- Streamlit web interface
- FAQ matching with TF-IDF and cosine similarity
- Beginner-friendly Python codebase
- Built-in FAQ topics around AI, ML, Python, GitHub, and Streamlit

## Tech Stack

- Python
- Streamlit
- scikit-learn

## How It Works

The app converts all FAQ questions into vectors using TF-IDF. When a user asks a question, the app transforms the input into the same vector space and calculates similarity scores. The best matching FAQ is returned if it crosses the similarity threshold.

## Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
streamlit run app.py
```

## Project Structure

- `app.py` - Main Streamlit application
- `README.md` - Project description and setup instructions
- `requirements.txt` - Required Python packages

## Example Topics

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Computer Vision
- Python
- GitHub
- Streamlit

## Notes

The chatbot is FAQ-based, so it works best when the input question is similar to one of the predefined FAQ entries. For more flexible responses, you can extend it with NLP or an LLM-based approach.
