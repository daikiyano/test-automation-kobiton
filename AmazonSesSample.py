
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class EmailService():
# Replace sender@example.com with your "From" address. 
# This address must be verified.
    def send_result_mail(seif,data,kobitonSessionId):
            SENDER = 'daikitech0123@gmail.com'  
            SENDERNAME = 'Sender Name'

            # Replace recipient@example.com with a "To" address. If your account 
            # is still in the sandbox, this address must be verified.
            RECIPIENT  = 'daikitech0123@gmail.com'

            # Replace smtp_username with your Amazon SES SMTP user name.
            USERNAME_SMTP = os.environ.get("USERNAME_SMTP")

            # Replace smtp_password with your Amazon SES SMTP password.
            PASSWORD_SMTP = os.environ.get("PASSWORD_SMTP")

            # (Optional) the name of a configuration set to use for this message.
            # If you comment out this line, you also need to remove or comment out
            # the "X-SES-CONFIGURATION-SET:" header below.
            # CONFIGURATION_SET = "ConfigSet"

            # If you're using Amazon SES in an AWS Region other than US West (Oregon), 
            # replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP  
            # endpoint in the appropriate region.
            HOST = os.environ.get("HOST")
            PORT = os.environ.get("PORT")

            # The subject line of the email.
            SUBJECT = '【KOBITON】the results of Automation Test with Python'

            # The email body for recipients with non-HTML email clients.
            BODY_TEXT = ("【KOBITON】the results of Automation Test with Python")

            # The HTML body of the email.
            BODY_HTML = data
            #  """<html>
            # <head></head>
            # <body>
            # <h1>Amazon SES SMTP Email Test</h1>
            # <p>This email was sent with Amazon SES using the
            #     <a href='https://www.python.org/'>Python</a>
            #     <a href='https://docs.python.org/3/library/smtplib.html'>
            #     smtplib</a> library.</p>
            # </body>
            # </html>
            #             """

        # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = SUBJECT
            msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
            msg['To'] = RECIPIENT
            # Comment or delete the next line if you are not using a configuration set
            # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(BODY_TEXT, 'plain')
            part2 = MIMEText(BODY_HTML, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)

            # Try to send the message.
        
            try:  
                server = smtplib.SMTP(HOST, PORT)
                server.ehlo()
                server.starttls()
                #stmplib docs recommend calling ehlo() before & after starttls()
                server.ehlo()
                server.login(USERNAME_SMTP, PASSWORD_SMTP)
                server.sendmail(SENDER, RECIPIENT, msg.as_string())
                server.close()
            # Display an error message if something goes wrong.
            except Exception as e:
                print ("Error: ", e)
            else:
                print ("Email sent!")