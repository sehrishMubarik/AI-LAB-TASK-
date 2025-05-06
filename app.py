from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')

intents = [
    "hello",
    "hi",
    "my name is [name]",
    "i am applying for bs program",
    "i want to apply for cs department",
    "i have done intermediate with 85%",
    "i have done bachelor with 3.5 cgpa",
    "how to apply",
    "i want to know about admission",
    "i'm interested in bba",
    "i want to study in ee",
    "how can i join your university"
]

responses = [
    "Hello! Welcome to ABC University Admission Chatbot. What’s your name?",
    "Hi there! What’s your name?",
    "Nice to meet you! What program are you applying for? (BS, MS, PhD)",
    "Great! Which department are you interested in? (e.g., CS, BBA, EE)",
    "Please provide your previous qualification and GPA/Percentage.",
    "Thanks. You’re eligible to apply. Visit our admission portal for next steps.",
    "Based on your qualification, you're eligible. Visit our official website to apply.",
    "To apply, please visit the university’s admission portal and complete the application form.",
    "Admissions are open. Please check our website for details and deadlines.",
    "Nice! What is your previous qualification?",
    "Electrical Engineering is a great choice. Please provide your academic background.",
    "You can join by applying online through our admissions portal."
]

intent_embeddings = model.encode(intents)
dimension = intent_embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(np.array(intent_embeddings))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    
    input_embedding = model.encode([user_input])
    _, indices = faiss_index.search(np.array(input_embedding), k=1)
    response_index = indices[0][0]
    response = responses[response_index]

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
