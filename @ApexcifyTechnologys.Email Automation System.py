import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender credentials
sender_email = "rashidmughal153@gmail.com"
password = "xulp llbz sepx xlhe"


#==================== List of 20 predefined emails=======================
recipient_emails = [
    "rashidmughul2000@gmail.com", "rashid2@gmail.com", "rashid3@gmail.com", 
    "rashid4@gmail.com.com", "rashid5@gmail.com", "rashid@gmail.com",
    "rashid7@gmail.com.com", "rashid8@gmail.com.com", "rashid9@gmail.com",
    "rashid10@gmail.com.com", "rashid11@gmail.com", "rashid12@gmail.com",
    "rashid13@gmail.com", "rashid14@gmail.com", "rashid15@gmail.com",
    "rashid15@gmail.com", "rashid@gmail.com", "rashid18@gmail.com",
    "rashid19@gmail.com", "rashid20@gmail.com"
]


#======================== Email content===================================
subject = "Important Update"
body = "Hello, this is a test email sent to multiple recipients using Python."

#========================= SMTP server setup==============================
smtp_server = "smtp.gmail.com"
port = 587

#========================== Connect and send emails=========================
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  #--------------------- Secure connection
    server.login(sender_email, password)

    for recipient in recipient_emails:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Sent email to {recipient}")

    print("All Emails sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()