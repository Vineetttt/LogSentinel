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

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%b/%Y:%I:%M:%S %z', prop)


dictionary = {
    'ips':[
        '192.168.1.1',
        '192.168.1.2',
        '192.168.1.3',
        '192.168.1.4',
        '192.168.1.5',
        '192.168.1.6',
    ],
    'request': ['GET', 'POST', 'PUT', 'DELETE'], 
    'endpoint':[
        '/api/v1/users',
        '/api/v1/products',
        '/api/v1/orders',
        '/api/v1/inventory',
        '/api/v1/payments',
        '/api/v1/analytics',
        '/api/v1/dashboard',
        '/api/v1/configuration',
    ], 
    'statuscode': ['303', '404', '500', '403', '502', '304','200','401'], 
    'username': ['james', 'adam', 'eve', 'alex', 'smith', 'bella', 'david', 'angela', 'millie', 'hilary','jamie','emma'],
    'ua' : ['Firefox/84.0',
            'Android/84.0',
            'Chrome/87.0',
            'Edge/89.0',
            'Opera/73.0',
            'Safari',
            'iPhone; CPU OS 12_4_9',
        ],
    'referrer' : ['-',fak.uri()*10]}

csv_file_path = 'data.csv'
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 3, 1)

data = []

for _ in range(1, 100001):
    compliant = [True] * 90 + [False] * 10
    compliant_choice = random.choice(compliant)
    if compliant_choice:
        ip = random.choice(dictionary['ips'])
        ua = random.choice(dictionary['ua'])
    else:
        ip = fak.ipv4()
        us = fak.user_agent()
            
    date_time = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    request = random.choice(dictionary['request'])
    endpoint = random.choice(dictionary['endpoint'])
    status_code = random.choice(dictionary['statuscode'])
    response_size = str(int(random.gauss(5000, 50)))
    referrer = random.choice(dictionary['referrer'])
    data.append([ip, date_time, request, endpoint, status_code, response_size, ua, referrer, compliant_choice])

sorted_data = sorted(data, key=lambda x: x[1])
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ['IP Address', 'Date/Time', 'Request', 'Endpoint', 'Status Code', 'Response Size', 'User Agent', 'Referrer', 'Compliant']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)


print(f"Log data stored in {csv_file_path}")