##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import random
import smtplib

import pandas
import datetime as dt


# 2. Check if today matches a birthday in the birthdays.csv
my_mail = "cmagnetinbox@gmail.com"
password = "magnet123"

today = (dt.datetime.now().month, dt.datetime.now().day)

file = pandas.read_csv("birthdayss.csv")

new_dict = {(rows["month"], rows.day): rows for (index, rows) in file.iterrows()}
print(new_dict)

if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/{random.randint(1, 3)}.txt"
    with open(file_path, "r") as birthday:
        contents = birthday.read()
        contents.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n {contents}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.







