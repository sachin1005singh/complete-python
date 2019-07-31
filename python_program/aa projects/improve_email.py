import smtplib , webbrowser

# checking valid email id
def get_mail():
    servicesAvailable = ['hotmail','gmail','yahoo', 'outlook']

    while True:

        mail_id  = input("E-mail :")
        if  '@' in mail_id and '.com' in mail_id:

            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos +1 : dotcom_pos]
            if sp in servicesAvailable:
                 return mail_id, sp
                 break

            else:
                print("we don't provide service for  " +sp)
                print("we provide service only for : hotmail / outlook, yahoo , gmail")
                continue

        else:
            print("invalid E-mail retype again ")
            continue

# different provider

def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return 'smtp.gmail.com'
    elif serviceProvider ==  'outlook' or serviceProvider == 'hotmail' :
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'yahoo':
        return 'smtp.mail.yahoo.com'

        
print(" Welcome you can send an E-mail through this program")
print("Please enter your E-mail and password :")
e_mail, serviceProvide = get_mail()
password = input("password :")

while True:
    try: 
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail, password)

    except:
        if serviceProvider == 'gmail':
            print(" Login unsuccessful, there are two possible reasons  :")
            print("1.  ) you typed wrong username or password")
            print("2. ) you are using Gmail there is an option in gmail 'allow less secure app ' ")
            print(" Do you want us to open a webpage from where you enable this option of less secure app")
            answer = input(" yes or no ? : ")


            if answer == "yes" or answer == "y":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")

            else:
                print(" we won't open webpage for you , you can got to 'https://myaccount.google.com/lesssecureapps' ")
                print("Please retype your E-mail and password also ")
                e_mail, serviceProvider = get_mail()
                password = input("Password :")
                continue

        else:
            print(" we won't open webpage for you , you can got to 'https://myaccount.google.com/lesssecureapps' ")
            print("Please retype your E-mail and password also ")
            e_mail, serviceProvider = get_mail()
            password = input("Password :")
            continue
    else:
        print("login successful ")
        break


        
         