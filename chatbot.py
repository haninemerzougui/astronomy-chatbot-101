import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

with open(r'C:\Users\HP\Desktop\stra\text.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')

sentences = sent_tokenize(data)

def preprocess(sentence):
    words = word_tokenize(sentence)
    
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]
    
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return words

def get_most_relevant_sentence(query):
    query = preprocess(query)
    
    max_similarity = 0
    most_relevant_sentence = ""
    
    for sentence in sentences:
        sentence_words = preprocess(sentence)
        similarity = len(set(query).intersection(sentence_words)) / float(len(set(query).union(sentence_words)))
        
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = sentence
            
    return most_relevant_sentence

def chatbot(query):
    response = get_most_relevant_sentence(query)
    return response

def main():
    st.title("Space Exploration Chatbot")
    st.write("Ask me anything about space exploration!")
    
    question = st.text_input("Your question:")
    
    if st.button("Submit"):
        response = chatbot(question)
        st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
