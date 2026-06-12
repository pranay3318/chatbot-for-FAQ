import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
import wikipedia
import nltk
import re

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------
# Download NLTK Resources
# ---------------------------------

nltk.download('stopwords')

# ---------------------------------
# Load FAQ Dataset
# ---------------------------------

faq_data = pd.read_csv("faq.csv")

questions = faq_data["question"].tolist()
answers = faq_data["answer"].tolist()

# ---------------------------------
# NLP Preprocessing
# ---------------------------------

stop_words = set(stopwords.words("english"))

def preprocess(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# ---------------------------------
# Prepare FAQ Questions
# ---------------------------------

processed_questions = [
    preprocess(q)
    for q in questions
]

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)

# ---------------------------------
# Chatbot Logic
# ---------------------------------

def get_answer(user_query):

    query = preprocess(user_query)

    query_vector = vectorizer.transform(
        [query]
    )

    similarity = cosine_similarity(
        query_vector,
        faq_vectors
    )

    highest_score = similarity.max()

    if highest_score > 0.3:

        index = similarity.argmax()

        return answers[index]

    # Wikipedia fallback

    try:

        result = wikipedia.summary(
            user_query,
            sentences=2
        )

        return result

    except wikipedia.exceptions.DisambiguationError:

        return "Please be more specific."

    except wikipedia.exceptions.PageError:

        return "I couldn't find information about that."

    except:

        return "Sorry, I could not understand."

# ---------------------------------
# Send Message Function
# ---------------------------------

def send_message():

    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_area.insert(
        tk.END,
        f"You: {user_text}\n\n"
    )

    response = get_answer(user_text)

    chat_area.insert(
        tk.END,
        f"Bot: {response}\n\n"
    )

    chat_area.see(tk.END)

    entry.delete(0, tk.END)

# ---------------------------------
# GUI
# ---------------------------------

root = tk.Tk()

root.title("AI FAQ Chatbot")

root.geometry("800x600")

root.configure(bg="#101820")

title = tk.Label(
    root,
    text="🤖 AI FAQ Chatbot",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#101820"
)

title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#1E293B",
    fg="white"
)

chat_area.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

entry = tk.Entry(
    root,
    font=("Arial", 14)
)

entry.pack(
    fill=tk.X,
    padx=10,
    pady=10
)

send_btn = tk.Button(
    root,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    command=send_message
)

send_btn.pack(pady=10)

entry.bind(
    "<Return>",
    lambda event: send_message()
)

root.mainloop()