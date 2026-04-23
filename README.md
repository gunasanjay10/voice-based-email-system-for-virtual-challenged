# voice-based-email-system-for-virtual-challenged

##  Project Overview

The **Voice-Based Email System** is an AIML-based application that allows users to send emails using voice commands.
This system is especially useful for **visually challenged users** or anyone who prefers hands-free interaction.

The project uses **Natural Language Processing (NLP)** techniques to convert voice input into structured email data such as recipient, subject, and message.

---

## Features

* Voice input using browser speech recognition
* NLP-based processing of commands
* Automatic email sending using SMTP
* Extracts:

  * Recipient (Email ID)
  * Subject
  * Message
  * Smart email reconstruction:

  * Converts “at” → `@`
  * Converts “dot” → `.`
  * Lightweight and easy to run

---

## Technologies Used

* **Python**
* **Flask**
* **HTML / JavaScript**
* **SMTP (Email Protocol)**
* **Natural Language Processing**

---

## Project Structure

```
voice_email_project/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### Clone the repository

```
git clone <your-repo-link>
cd voice_email_project
```

### Install dependencies

```
pip install -r requirements.txt
```

### Configure Email

Edit `app.py`:

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

Use **Gmail App Password**, not your normal password.

---

## Run the Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```
## How to Use
Click **Start Voice** and speak clearly:

```
Send email to hariharan sakthivel 18 at gmail dot com subject hello message how are you
```
## Output Example
* **To:** [hariharansakthivel18@gmail.com](mailto:hariharansakthivel18@gmail.com)
* **Subject:** hello
* **Message:** how are you
## AIML Concept Used
This project uses **Natural Language Processing (NLP)** to:

* Tokenize user speech
* Identify keywords (to, subject, message)
* Convert unstructured voice into structured data
## Challenges & Solutions
| Problem                 | Solution                     |
| ----------------------- | ---------------------------- |
| Voice misrecognition    | Keyword-based NLP            |
| Incorrect email capture | Email reconstruction logic   |
| Message confusion       | Subject & message separation |
| Gmail security issues   | App Password authentication  |

## Unique Features
* Smart email parsing from voice
* Structured command processing
* Real-time working system
* Improved accuracy over basic voice email systems
## Future Enhancements
* 🤖 AI-based intent detection (without keywords)
* 🌐 Multi-language support (Tamil + English)
* 🔊 Voice feedback system
* 📱 Mobile application
## Conclusion
This project demonstrates how **AI and NLP** can be used to build an intelligent voice-controlled system for email communication, improving accessibility and usability.
##  Author
* Hema Bava

---
