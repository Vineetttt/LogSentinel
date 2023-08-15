import csv
import random
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


dictionary = {
    'ips':[
        '192.168.1.1',
        '192.168.1.2',
        '192.168.1.3'
    ],
    'dev_request': ['GET', 'POST','PUT'],
    'analyst_request':['GET'],
    'admin_request':['GET', 'POST','PUT', 'DELETE'], 
    'endpoint':[
        '/api/v1/products',
        '/api/v1/orders',
        '/api/v1/inventory',
    ],
    'admin_endpoint':[
        '/api/v1/payments',
        '/api/v1/dashboard',
        '/api/v1/configuration',
    ] ,
    'statuscode': ['303', '404', '500', '403', '502', '304','200','401','200','200','200'], 
    'usertype': ['developer','analyst','admin'],
    'ua' : ['Firefox/84.0',
            'Android/84.0',
            'Chrome/87.0',
            'Edge/89.0',
            'Opera/73.0',
            'Safari',
            'iPhone; CPU OS 12_4_9',
        ],
}

csv_file_path = 'data/data.csv'
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 5)

data = []

for _ in range(1, 10001):
    compliant = [True] * 90 + [False] * 10
    compliant_choice = random.choice(compliant)
    time_stamp = generate_random_timestamp(start_date, end_date)
    ua = random.choice(dictionary['ua'])
    sc = random.choice(dictionary['statuscode'])
    res = str(int(random.randint(1,1000)))
    if compliant_choice:
        ip = random.choice(dictionary['ips'])
        ut = random.choice(dictionary['usertype'])
        if ut == 'admin':
            endpoint = random.choice(dictionary['admin_endpoint'])
            rt = random.choice(dictionary['admin_request'])
        elif ut == 'developer':
            endpoint = random.choice(dictionary['endpoint'])
            rt = random.choice(dictionary['dev_request'])
        else:
            endpoint = random.choice(dictionary['endpoint'])
            rt = random.choice(dictionary['analyst_request'])      
    else:
        ip = random.choice([fak.ipv4()]*995 + dictionary['ips']*5)
        ut = random.choice(['develOper','analyst','admiin','deve1oper','devloper','analyzt','aadmin','developer','analyst'])
        endpoint = random.choice(dictionary['admin_endpoint']*2 + dictionary['endpoint'])
        rt = random.choice(dictionary['admin_request']*2+dictionary['dev_request']+dictionary['analyst_request'])

    data.append([ip, time_stamp,ut,ua,endpoint,rt,sc,res,compliant_choice])

sorted_data = sorted(data, key=lambda x: x[1])
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ['IP Address', 'Timestamp', 'User Type','User Agent','Endpoint','Request Type','Status Code', 'Response Time','Compliant']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)


print(f"Log data stored in {csv_file_path}")