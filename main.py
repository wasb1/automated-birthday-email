import smtplib
import datetime as dt
import random
import pandas as pd

now = dt.datetime.now()
now_day = now.day
now_month = now.month

list_of_letters = ["./letter_templates/letter_1.txt",
                   "./letter_templates/letter_2.txt",
                   "./letter_templates/letter_3.txt"]

df = pd.read_csv("./birthdays.csv")

# if the row of the following conditions is not empty, then:
if not df[(df["day"] == now_day) & (df["month"] == now_month)].empty:
    birthday_person = df[(df["day"] == now_day) & (df["month"] == now_month)]
    birthday_person_name = birthday_person["name"].values[0]
    birthday_person_email = birthday_person["email"].values[0]

    random_letter = random.choice(list_of_letters)

    with open(random_letter, "r") as letter:
        letter_to_list = letter.readlines()

        if letter_to_list[0] == "Dear [NAME],\n":
            letter_to_list[0] = "Dear " + birthday_person_name + ",\n"

        elif letter_to_list[0] == "Hey [NAME],\n":
            letter_to_list[0] = "Hey " + birthday_person_name + ",\n"

        list_to_letter = "".join(letter_to_list)

    with open(random_letter, "w") as letter:
        letter.write(list_to_letter)

    with open(random_letter, "r") as letter:
        letter_text = letter.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,
                             password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person_email,
                                msg=f"Subject: Birthday Wishes\n\n{letter_text}"
                                )
