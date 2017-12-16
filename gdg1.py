import smtplib
import csv

with open('email.csv', 'r') as csv_file:
    csv_reader =csv.reader(csv_file)

    for line in csv_reader:
        receiver=line[1]
        print(receiver)
        content = 'Hey there, You are invited to Devfest 2017 event by GDG VIT'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('archismanpython@gmail.com', 'qwerty12345!')
        mail.sendmail('archismanpython@gmail.com',receiver, content)
        mail.close()

