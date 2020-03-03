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
    return response

def get_dates(instance_info_dict,dates):
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
        naive = x[1].replace(tzinfo=None)
        naive = naive.date()
        print(type(naive))
        x[1]=int((today-naive.days))
    return dates

def sort_by_oldest(dates):
    
    return(sorted(dates, key = lambda x: x[1],reverse = True)) 
    


def main():
    dates = []
    instance_info_dict = get_instances()
    dates = get_dates(instance_info_dict,dates)
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