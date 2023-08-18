import csv
import random
import string
from random import randint, choice
import sys
import time
import faker
from datetime import datetime,timedelta,date
import os
os.environ['TZ'] = 'Asia/Kolkata'
fak = faker.Faker()

def generate_random_timestamp(start_date, end_date):
    time_diff = end_date - start_date
    random_time = start_date + timedelta(seconds=random.randint(0, time_diff.total_seconds()))
    return random_time

def generate_random_username(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

dictionary = {
    'tokens':[
        '874264',
        '567290',
        '927634'
    ],
    'username':[
        "Kris345",
        "Jack87",
        "Bella233"
    ] ,
    'statuscode': ['303', '404', '500', '403', '502', '304','200','401','200','200','200'], 
}

csv_file_path = 'data/token.csv'
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 5)

data = []

for _ in range(1, 2001):
    compliant = [True] * 55 + [False] * 45
    compliant_choice = random.choice(compliant)
    time_stamp = generate_random_timestamp(start_date, end_date)
    sc = random.choice(dictionary['statuscode'])
    if compliant_choice:
        token = random.choice(dictionary['tokens'])
        user = random.choice(dictionary['username'])      
    else:
        token = random.choice([(random.randint(100000, 999999))]*980+dictionary['tokens']*20)
        user = generate_random_username(random.randint(4,10))

    data.append([user, time_stamp,token,sc,compliant_choice])

sorted_data = sorted(data, key=lambda x: x[1])
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ['User','TimeStamp','Token','Status Code','Compliant']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)


print(f"Log data stored in {csv_file_path}")