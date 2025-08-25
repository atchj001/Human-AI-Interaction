# Flight Booking Chatbot Prototype

## 📌 Overview
This project is a **flight booking chatbot prototype** developed for the COMP3074 Human-AI Interaction coursework.  
The system demonstrates **interactive Natural Language Processing (NLP)** by combining:

- Intent matching  
- Identity management (user names)  
- Transactional dialogue (flight booking and editing)  
- Information retrieval & Question answering  
- Small talk for natural conversation flow  

The chatbot is designed to simulate a **personalised, human-like conversation** while guiding users through tasks such as booking and editing flights.

---

## 🏗️ Project Structure
The chatbot is modular, with different functionalities implemented in separate files for clarity and easier debugging:

- `main.py` → Core logic and system integration  
- `question_answering.py` → Retrieval-based QA using TF-IDF & cosine similarity  
- `small_talk.py` → Casual conversation and greetings dataset  
- `name_management.py` → Stores, changes, and recalls user names  
- `transaction.py` → Handles flight booking, editing, and confirmation  
- `spellcheck.py` → Corrects typos in user input  
- `question_answering.csv` → Dataset for predefined Q&A pairs  
- `small_talk.csv` → Dataset for casual conversation responses  

---

## ⚙️ Features
- **Question Answering (QA)**  
  - TF-IDF vectorization with stemming  
  - Cosine similarity for matching queries  
  - Error handling when no match is found  

- **Intent Matching**  
  - Priority-based checks (Name → Small Talk → QA)  
  - Simple text matching for booking and editing flights  

- **Name Management**  
  - Stores and recalls user name  
  - Allows renaming at any time  
  - Adds personalization with emojis  

- **Small Talk**  
  - Supports greetings, casual queries, and randomised responses  
  - Helps maintain a natural conversational flow  

- **Flight Booking System**  
  - Book single or return flights  
  - View and edit flight details (e.g., email, dates)  
  - Confirmation messages with positive feedback  

- **Additional Features**  
  - Spell checking of user input  
  - Telling the current time  
  - Detecting if user shares the same name as the system  

---

## 🖥️ Example Usage
- **Start the chatbot** → Enter your name  
- **Book a flight** → "Book a flight to Paris"  
- **Edit details** → "Edit my email"  
- **Small talk** → "Hello", "How are you?"  
- **Ask a question** → "What is AI?"  

---

## ✅ Testing & Evaluation
- **Unit testing**: Ensured individual components (QA, name management, small talk, etc.) work independently  
- **Integration testing**: Verified modules work together in `main.py`  
- **System testing**: Full chatbot conversations tested  
- **Usability testing**: Friends tested interaction flow and suggested improvements  
