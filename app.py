from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL = "YOUREMAIL@gmail.com"
PASSWORD = "YOUR PASSWORD"

# ✅ SEND EMAIL
def send_email(to_email, subject, message):
    try:
        msg = MIMEText(str(message), "plain", "utf-8")
        msg['Subject'] = subject
        msg['From'] = EMAIL
        msg['To'] = to_email.strip()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print("EMAIL ERROR:", e)
        return False


# 🧠 NLP PROCESS (FINAL FIX)
def process_text(text):
    words = text.lower().split()

    to_email = None
    subject = ""
    message = ""

    email_parts = []
    capture_email = False

    # -------- EMAIL --------
    for word in words:
        if word == "to":
            capture_email = True
            continue

        if capture_email:
            if word in ["subject", "message"]:
                break

            if word == "at":
                email_parts.append("@")
            elif word == "dot":
                email_parts.append(".")
            else:
                email_parts.append(word)

    if email_parts:
        to_email = "".join(email_parts).replace(" ", "")

    # -------- SUBJECT --------
    if "subject" in words:
        s_idx = words.index("subject")

        if "message" in words:
            m_idx = words.index("message")
            subject = " ".join(words[s_idx+1:m_idx])
        else:
            subject = " ".join(words[s_idx+1:])

    # -------- MESSAGE --------
    if "message" in words:
        m_idx = words.index("message")
        message = " ".join(words[m_idx+1:])
    else:
        message = ""

    # defaults
    if not subject:
        subject = "Voice Email"
    if not message:
        message = "No message"

    return to_email, subject, message


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/send', methods=['POST'])
def send():
    try:
        text = request.form['text']
        print("User said:", text)

        to_email, subject, message = process_text(text)

        print("TO:", to_email)
        print("SUBJECT:", subject)
        print("MESSAGE:", message)

        if not to_email:
            return jsonify({
                "status": "error",
                "msg": "Recipient not detected. Speak clearly.",
                "to": "N/A",
                "subject": "N/A"
            })

        success = send_email(to_email, subject, message)

        if not success:
            return jsonify({
                "status": "error",
                "msg": "Email sending failed",
                "to": to_email,
                "subject": subject
            })

        return jsonify({
            "status": "success",
            "to": to_email,
            "subject": subject,
            "message": message
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "msg": str(e),
            "to": "N/A",
            "subject": "N/A"
        })


if __name__ == "__main__":
    app.run(debug=False)