import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import os


TWILIO_SID = 'AC46e2b1fb32a6811696abc3277092947e'
TWILIO_AUTH_TOKEN = 'e792079f26f9ec318b584d6068ab28d4'
TWILIO_PHONE_NUMBER = '+16575346472'


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'use yours own@gmail.com'
EMAIL_PASSWORD = generate your own//'

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


def load_numbers():
    """Load email addresses or phone numbers from numbers.txt"""
    if os.path.exists('numbers.txt'):
        with open('numbers.txt', 'r') as f:
            items = [line.strip() for line in f if line.strip()]
        return items
    else:
        messagebox.showerror("Error", "numbers.txt not found!")
        return []


def load_message():
    """Load message from message.txt and display in GUI"""
    if os.path.exists('message.txt'):
        with open('message.txt', 'r') as f:
            message = f.read()
        message_text.delete(1.0, tk.END)
        message_text.insert(tk.END, message)
    else:
        messagebox.showinfo("Info", "message.txt not found. Write a new message.")


def save_message():
    """Save the message from GUI to message.txt"""
    message = message_text.get(1.0, tk.END).strip()
    if message:
        with open('message.txt', 'w') as f:
            f.write(message)
        messagebox.showinfo("Success", "Message saved to message.txt")
    else:
        messagebox.showerror("Error", "Message is empty!")


def send_sms():
    """Send SMS to all numbers in numbers.txt"""
    numbers = load_numbers()
    if not numbers:
        return
    with open('message.txt', 'r') as f:
        message = f.read().strip()
    if not message:
        messagebox.showerror("Error", "No message to send!")
        return

    for number in numbers:
        try:
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=number
            )
            print(f"SMS sent to {number}")
        except Exception as e:
            print(f"Failed to send to {number}: {e}")
    messagebox.showinfo("Success", f"SMS sent to {len(numbers)} numbers!")


def send_email():
    """Send email to all addresses in numbers.txt"""
    emails = load_numbers()
    if not emails:
        return
    with open('message.txt', 'r') as f:
        message_body = f.read().strip()
    if not message_body:
        messagebox.showerror("Error", "No message to send!")
        return

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        for email in emails:
            msg = MIMEText(message_body)
            msg['Subject'] = 'Bulk Message'  # You can customize the subject
            msg['From'] = EMAIL_USER
            msg['To'] = email
            server.sendmail(EMAIL_USER, email, msg.as_string())
            print(f"Email sent to {email}")

        server.quit()
        messagebox.showinfo("Success", f"Email sent to {len(emails)} addresses!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send emails: {e}")


# GUI Setup
root = tk.Tk()
root.title("Bulk SMS/Email Sender")
root.geometry("500x400")

# Message Text Area
tk.Label(root, text="Write your message:").pack(pady=5)
message_text = tk.Text(root, height=10, width=50)
message_text.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Load Message from File", command=load_message).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Save Message to File", command=save_message).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Send SMS", command=send_sms).grid(row=1, column=0, padx=5)
tk.Button(button_frame, text="Send Email", command=send_email).grid(row=1, column=1, padx=5)

root.mainloop()
