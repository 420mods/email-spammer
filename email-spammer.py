import os, sys, smtplib, getpass

try:
    W = '\033[0m' #white
    R = '\033[31m' #red
    G = '\033[32m' #Green

    os.system("clear")

    server = raw_input('Mail-Server Gmail/Yahoo: ')

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif server == 'yahoo' or server == 'Yahoo':

        smpt_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:
        print(R + "Error this only works on Gmail and Yahoo" + W)
        sys.exit()

        email_user = raw_input("Email: ")
        password = getpass.getpass('Password: ')
        email_to = raw_input('\nTo: ')
        subject = raw_input('Subect: ')
        body = raw_input('Message: ')
        total = input('Amount of messages you want to send: ')

    try:

        server = smtp.SMTP(smtp_server,port)
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,password)

    print("\n\n\n - Target : {} - \n".format(email_to))

        for i in range(1, total+1):

            msg = 'From:' + email_user + '\nSubject:' + subject + '\n' + body

        server.sendmain(email_user,email_to,msg)

            print(G + "\rEmail Sent - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print(R + "\n\n-Proccess Complete-" + W)

        except smtplib.SMTPAutherncationError:
            print(R + "\nError - Authentication Error, are you sure the password and email is correct" + W)
            sys.exit()

        except smtplib.SMTPAuthenticationError:
            sys.exit()