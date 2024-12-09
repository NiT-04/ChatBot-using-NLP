# ChatBot-using-NLP

# Intelligent Chatbot with NLP

## Overview  
This project demonstrates the creation of an intelligent chatbot using Natural Language Processing (NLP). The chatbot interprets user intents and provides contextually appropriate responses based on predefined patterns and rules. It integrates the `nltk` library for NLP tasks, `scikit-learn` for ML operations, and `streamlit` for an interactive user interface.

---

## Key Features  
- Recognizes various user intents such as greetings, farewells, and expressions of gratitude.  
- Delivers accurate and meaningful responses based on user queries.  
- Keeps track of the conversation history, allowing users to revisit past interactions.  
- Developed in Python, utilizing robust NLP and machine learning libraries.  

---

## Technology Stack  
- **Python**  
- **NLTK** for natural language understanding.  
- **Scikit-learn** for classification and other ML tasks.  
- **Streamlit** for creating a web-based user interface.  
- **JSON** for managing intents data.  

---

## Setup and Installation  

### Step 1: Clone the Repository  
```bash  
git clone <your-repository-url>  
cd <your-project-directory>  
```  

### Step 2: Create a Virtual Environment (Recommended)  
```bash  
python -m venv venv  
source venv/bin/activate  # For Windows: `venv\Scripts\activate`  
```  

### Step 3: Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Step 4: Download Required NLTK Data  
Run the following code in Python:  
```python  
import nltk  
nltk.download('punkt')  
```  

---

## How to Use  

### Running the Chatbot  
Start the application by executing the command:  
```bash  
streamlit run app.py  
```  

Once launched, interact with the chatbot via the web interface. Simply type your queries in the input box and receive instant responses.  

---

## About Intents Data  
The chatbot’s responses are guided by the `intents.json` file, which includes tags, patterns, and corresponding responses. Modify this file to add new intents or refine existing ones to suit your requirements.  

---

## Conversation Logs  
The application saves all interactions in a `chat_log.csv` file, which you can access to review past conversations. The "Conversation History" feature is available via the sidebar for convenience.  

---

## Contributing  
We welcome contributions! If you have ideas for improvement or want to add new features, please submit an issue or create a pull request in the repository.  

---

## Licensing  
This project is distributed under the MIT License. For details, refer to the [LICENSE](LICENSE) file in the repository.  

---

## Special Thanks  
- **NLTK** for foundational NLP tools.  
- **Scikit-learn** for machine learning functionality.  
- **Streamlit** for the interactive web-based interface.  
