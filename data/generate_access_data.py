import csv
import random
from datetime import datetime, timedelta
import os
os.environ['TZ'] = 'Asia/Kolkata'

def generate_random_timestamp(start_date, end_date):
    time_diff = end_date - start_date
    random_time = start_date + timedelta(seconds=random.randint(0, time_diff.total_seconds()))
    return random_time

def generate_user_id():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))

dictionary = {
    'valid_actions': ['Login', 'View','Access'],
    'invalid_actions':['Edit','Delete'],
    'valid_resources': ['Dashboard', 'Reports', 'Documents'],
    'invalid_resources':['Financials', 'Admin Panel'],
    'statuses': ['Success', 'Unauthorized'],
}

csv_file_path = 'data/user_actions.csv'
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 3)

data = []

for _ in range(1, 2001):
    compliant = [True] * 55 + [False] * 45
    compliant_choice = random.choice(compliant)
    time_stamp = generate_random_timestamp(start_date, end_date)
    if compliant_choice:
        status = 'Success'
        action = random.choice(dictionary['valid_actions'])
        resource = random.choice(dictionary['valid_resources'])
        compliant_status = True
    else:
        status = random.choice(['Success', 'Unauthorized','Unauthorized', 'Unauthorized'])
        action = random.choice(dictionary['invalid_actions']*2+dictionary['valid_actions'])
        resource = random.choice(dictionary['invalid_resources'])
        compliant_status = False
    user_id = generate_user_id()

    data.append([user_id, time_stamp, action, resource, status, compliant_status])

sorted_data = sorted(data, key=lambda x: x[1])
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ['User ID', 'Timestamp', 'Action', 'Resource', 'Status', 'Compliant']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)

print(f"Log data stored in {csv_file_path}")
