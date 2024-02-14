import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'hello@jurysoftprojects.com'
receiver_email = 'debanjan.d@jurysoft.com'
subject = 'Testing mail'
body = 'Body of testing mail.'
smtp_server = 'mail.jurysoftprojects.com'
smtp_password = 'QINBm[^TG7}('
smtp_port = 587  # or 465 for SSL/TLS

def send_email_html(receivers, html, subject, cc = None, bcc = None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receivers)
    message['Cc'] = ', '.join(cc)
    message['Bcc'] = ', '.join(bcc)
    message['Subject'] = subject
    message.attach(MIMEText(html, 'html'))
    try:
        # Establish a connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # If using TLS

        # Login to your email account
        server.login(sender_email, smtp_password)
        print('login success')

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('mail success')

        # Quit the SMTP server
        server.quit()
    except Exception as e:
        print(e)

def send_email_text(receivers, body, subject, cc = None, bcc = None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receivers)
    message['Cc'] = ', '.join(cc)
    message['Bcc'] = ', '.join(bcc)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        # Establish a connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # If using TLS

        # Login to your email account
        server.login(sender_email, smtp_password)
        print('login success')

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('mail success')

        # Quit the SMTP server
        server.quit()
    except Exception as e:
        print(e)
