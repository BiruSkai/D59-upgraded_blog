import smtplib, os
from dotenv import load_dotenv

load_dotenv("D:\project coding 1.1.2024\.env.txt")
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


class NotificationManager:

    def send_email(self, name, email, phone, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: WebDev Python\n\n"
                    f"Name of sender: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}".encode("utf-8")
            )