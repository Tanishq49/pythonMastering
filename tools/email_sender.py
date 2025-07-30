import yagmail

# Initialize the SMTP client
yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')

# Send the email
yag.send(
    to='antimabhandari9@gmail.com',
    subject='Hello from Python',
    contents='This is a test email sent using yagmail!'
)

print("✅ Email sent successfully!")
