import datetime as dt
import pandas
import random
import smtplib

my_email = "abdelrahmanalhassan95@yahoo.com"
password = "diqxyksmxbgonbps"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)


birthday = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday.iterrows()}

if today in birthday_dict:

    dice = random.randint(1, 3)
    with open(f"./letter_templates/letter_{dice}.txt") as letters:
        birthday_person = birthday_dict[today]
        contents = letters.read()
        letter = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday!!\n\n{letter}")




