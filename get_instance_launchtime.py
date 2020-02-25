import json
import datetime
from datetime import date
from datetime import datetime
import boto3


def get_instances():

    boto3.setup_default_session(profile_name='int')
    client = boto3.client('ec2')
    response = client.describe_instances()
    print(response)
    return 

def get_dates(dates):
    with open('instance_info.json', 'r') as f:
        instance_info_dict = json.load(f)
    for y in range(0,len(instance_info_dict['Reservations'])):
        for instance in instance_info_dict['Reservations'][y]['Instances']:
            id=''
            date=''
            for key in instance.items():
                if key[0] == 'InstanceId':
                    id = key[1]
                if key[0] == 'LaunchTime':
                    date = key[1]
            if id and date != '':
                dates.append([id,date])  
    
    return dates



def how_old(dates):
    today = date.today()
    for x in dates:
        temp = datetime.strptime(x[1],'%Y-%m-%dT%H:%M:%S.%fZ').date()
        x[1]=int((today-temp).days)
    return dates

def sort_by_oldest(dates):
    
    return(sorted(dates, key = lambda x: x[1],reverse = True)) 
    


def main():
    dates = []
    get_instances()
    dates = get_dates(dates)
    print('\n')
    print(dates)
    dates = how_old(dates)
    print('\n')
    print(dates)
    dates = sort_by_oldest(dates)
    print('\n')
    print(dates)

if __name__ == "__main__":
    main()