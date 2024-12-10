import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL setup for nltk downloads
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Define the chatbot function
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response

# App counter
counter = 0

def main():
    global counter
    st.set_page_config(
        page_title="NLP Chatbot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for styling
    st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
    }
    .css-1v3fvcr { 
        background-color: #ffffff00; 
    }
    .stButton>button {
        background-color: #1e3c72;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #2a5298;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🤖 Implementation of Chatbot using NLP")
    st.image("https://via.placeholder.com/800x150.png?text=Welcome+to+NLP+Chatbot", use_column_width=True)

    # Sidebar menu
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.radio("Menu", menu)

    # Home Menu
    if choice == "Home":
        st.markdown("### 💬 Start a Conversation")
        st.write("Type a message below and let the chatbot respond!")

        # Create chat log file if not exists
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        if user_input:
            response = chatbot(user_input)
            st.markdown(f"**Chatbot:** {response}")

            # Log the conversation
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.balloons()
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()

    # Conversation History Menu
    elif choice == "Conversation History":
        st.markdown("### 📜 Conversation History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    st.markdown(f"- **User:** {row[0]}")
                    st.markdown(f"  - **Chatbot:** {row[1]}")
                    st.markdown(f"  - *Timestamp:* {row[2]}")
        else:
            st.write("No conversation history found.")

    # About Menu
    elif choice == "About":
        st.markdown("### ℹ️ About This Chatbot")
        st.write("""
        This chatbot uses **Natural Language Processing (NLP)** and **Logistic Regression** to respond to user inputs.
        It is built using **Streamlit** for an interactive and visually appealing interface.
        """)
        st.image("https://via.placeholder.com/600x300.png?text=About+Chatbot", use_column_width=True)

if __name__ == '__main__':
    main()
