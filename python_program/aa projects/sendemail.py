import smtplib
connection = smtplib.SMTP('smtp.gmail.com', 587)

connection.ehlo()
connection.starttls()
connection.login('sachin1005singh@gmail.com', 'singh27071999@')
connection.sendmail('sachin1005singh@gmail.com','rakeshkumar1618072@gmail.com','Subject :use of python module\n\n this is use of python ')
connection.quit()
