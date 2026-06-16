# 🤖 AI FAQ Chatbot.

An intelligent chatbot application that answers frequently asked questions using natural language processing and machine learning. This project includes both a desktop GUI version and a web-based interface.

## 🌟 Features

- **Intelligent FAQ Matching**: Uses TF-IDF vectorization and cosine similarity to find the best matching answers
- **Wikipedia Fallback**: When FAQ knowledge isn't sufficient, the bot pulls information from Wikipedia
- **Dual Interface**: 
  - Desktop application with Tkinter GUI
  - Web-based interface with HTML/CSS/JavaScript
- **Natural Language Processing**: Preprocesses user queries with stopword removal and text normalization
- **Real-time Responses**: Instant feedback for user queries with a clean conversation interface

## 📁 Project Structure

```
chatbot-for-FAQ/
├── chatbot.py          # Desktop GUI chatbot (Python/Tkinter)
├── index.html          # Web-based chatbot interface
├── script.js           # Frontend chatbot logic
├── style.css           # Styling for web interface
├── faq.csv             # FAQ dataset (questions & answers)
└── README.md           # This file
```

## 🛠️ Tech Stack

- **Backend**: Python 3.x
- **Desktop GUI**: Tkinter
- **Frontend**: HTML5, CSS3, JavaScript
- **NLP Libraries**: NLTK, scikit-learn, pandas, Wikipedia API

## 📋 Requirements

### Desktop Version (chatbot.py)
```
tkinter (usually included with Python)
pandas
wikipedia
nltk
scikit-learn
```

### Web Version (index.html)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Getting Started

### Desktop Application

1. **Install dependencies**:
   ```bash
   pip install pandas wikipedia nltk scikit-learn
   ```

2. **Prepare FAQ data**:
   - Create a `faq.csv` file with columns: `question` and `answer`
   - Example:
     ```
     question,answer
     What is AI?,Artificial Intelligence is the simulation of human intelligence processes by machines.
     What is India?,India is a country in South Asia.
     ```

3. **Run the chatbot**:
   ```bash
   python chatbot.py
   ```

### Web Application

1. Simply open `index.html` in your web browser
2. Start chatting with the bot!
3. The bot responds with predefined answers based on keywords

## 💡 How It Works

### Desktop Version
1. **Data Loading**: Reads FAQ dataset from `faq.csv`
2. **Preprocessing**: Converts user input to lowercase, removes special characters, and filters stopwords
3. **Vectorization**: Uses TF-IDF to convert text into numerical vectors
4. **Similarity Matching**: Calculates cosine similarity between user query and FAQ questions
5. **Response Generation**: 
   - If similarity score > 0.3, returns the best matching FAQ answer
   - Otherwise, attempts to fetch info from Wikipedia
   - If that fails, returns a default error message

### Web Version
- Client-side JavaScript handles pattern matching
- Responds with predefined answers based on keyword detection
- Simple and fast, suitable for static FAQ content

## 📊 Language Composition

- **Python**: 41.1%
- **CSS**: 27.2%
- **JavaScript**: 19.1%
- **HTML**: 12.6%

## 🎯 Use Cases

- Customer support automation
- FAQ answering systems
- Educational chatbots
- Information retrieval assistants
- Frequently Asked Questions handling

## 🔧 Customization

### Adding More FAQs
Edit `faq.csv` to add new question-answer pairs:
```csv
what is machine learning?,Machine learning is a subset of AI that enables systems to learn from data.
```

### Adjusting Similarity Threshold
In `chatbot.py`, modify the threshold (currently 0.3):
```python
if highest_score > 0.3:  # Change this value
```

### Styling
Modify `style.css` to customize the web interface appearance

## 📝 Notes

- The web version uses simple keyword matching, while the desktop version uses advanced NLP
- Ensure `faq.csv` exists in the same directory as `chatbot.py`
- NLTK stopwords will download automatically on first run
- Wikipedia access requires an internet connection for the fallback feature

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Created by pranay3318

---

**Happy Chatting! 🚀**
