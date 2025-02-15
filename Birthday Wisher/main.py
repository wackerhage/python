import smtplib, pandas, datetime as dt
import random

my_email = "teste091996@gmail.com"
password = "vdkdxzjymnasebhu"

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
day = now.day
month_of_year = now.month
year = now.year

for index, row in data.iterrows():
    if month_of_year == data.month.iloc[index] and day == data.day.iloc[index]:
        print(f"Its your birthday, {data.name.iloc[index]}!")
        file_path_letter = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path_letter) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", data.name.iloc[index])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data.email.iloc[index],
                                msg=f"Subject: Its your birthday, {data.name.iloc[index]}!\n{contents}")
