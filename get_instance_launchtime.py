import requests
import json


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
    return dates

def sort_by_oldest(dates):
    return dates


def main():
    dates = []
    dates = get_dates(dates)

if __name__ == "__main__":
    main()