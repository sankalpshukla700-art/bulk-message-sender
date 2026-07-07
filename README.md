# bulk-message-sender
# 📩 Bulk Message Sender

A Python-based automation tool that enables users to send personalized messages to multiple recipients efficiently. The application simplifies repetitive messaging tasks by allowing users to import recipient details, customize message templates, and automate the sending process through a clean and user-friendly interface.

> **Disclaimer:** This project is intended for educational purposes and for sending messages only to recipients who have consented to receive them. Users are responsible for complying with the terms of service of the messaging platform they use.

---

# ✨ Features

* 📤 Send messages to multiple recipients automatically
* 📄 Import recipient details from CSV or Excel files (if supported)
* ⚡ Fast and efficient bulk messaging
* 🖥️ Simple Python-based interface
* 📊 Real-time sending progress
* 💻 Cross-platform support (Windows, macOS, and Linux)

---

# 🏗️ How It Works

1. Launch the Python application.
2. Import or enter the list of recipient phone numbers or contacts.
3. Write the message you want to send.
4. The application processes the recipient list one by one.
5. Each message is sent automatically while displaying the sending status.
6. A completion report is generated after all messages have been processed.

```text
        User
          │
          ▼
   Bulk Message Sender
          │
          ▼
  Load Contact List
          │
          ▼
 Process Each Recipient
          │
          ▼
 Send Personalized Message
          │
          ▼
 Display Sending Status
```

---

# 🛠️ Technologies Used

* Python 3
* Selenium (if browser automation is used)
* Pandas
* Tkinter / Custom GUI
* CSV Processing
* Web Automation Libraries

---

# 📦 Installation

## Clone the Repository

```bash
git clone https://github.com/sankalpshukla700-art/bulk-message-sender.git
cd bulk-message-sender
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Use

### Step 1

Clone or download this repository.

### Step 2

Install all required Python packages.

```bash
pip install -r requirements.txt
```

### Step 3

Run the application.

```bash
python app.py
```

> If your project uses a different entry file (for example `main.py` or `sender.py`), replace `app.py` with the correct filename.

### Step 4

* Import your contact list.
* Enter or load your message template.
* Start the sending process.

### Step 5

Monitor the progress until all messages have been sent successfully.

---

# 📂 Project Structure

```text
bulk-message-sender/
│
├── app.py
├── requirements.txt
├── contacts/
├── templates/
├── static/
├── screenshots/
└── README.md
```

---

# 🚀 Future Improvements

* Message scheduling
* Media and file attachments
* Contact validation
* Multi-language support
* Delivery reports
* Dark mode
* Cloud deployment
* User authentication

---

# 👨‍💻 Author

**Sankalp Shukla**

If you found this project useful, please consider giving it a ⭐ on GitHub.
