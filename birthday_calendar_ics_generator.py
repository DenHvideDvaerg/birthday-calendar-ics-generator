import csv  
import datetime  
from ics import Calendar, Event  
  
def read_birthdays_from_csv(file_path, csv_deliiter, date_format):  
    birthdays = []  
  
    with open(file_path, newline='') as csvfile:  
        reader = csv.DictReader(csvfile, delimiter=csv_deliiter)  
        for row in reader:  
            birthdays.append({  
                'name': row['name'],  
                'birthdate': datetime.datetime.strptime(row['birthdate'], date_format).date(),  
                'note': row.get('note', '')  
            })  
  
    return birthdays  
  
def create_birthday_events(birthdays, max_age):  
    events = []  
  
    for person in birthdays:  
        birthdate = person['birthdate']  
          
        for i in range(0, max_age):  
            event = Event()  
            if i == 0:  
                event.name = f"{person['name']} was born today"  
            else:  
                event.name = f"{person['name']} turns {i} today"  
            event.begin = birthdate.replace(year=birthdate.year + i)  
            event.make_all_day()  
            if person['note']:  
                event.description = person['note']  
  
            events.append(event)  
  
    return events  
  
def create_ical_file(events, file_name):  
    calendar = Calendar(events=events)  
    with open(file_name, 'w') as f:  
        f.writelines(calendar)  
  
if __name__ == '__main__':  
    csv_file = 'birthdays.csv'  
    ical_file = 'birthdays.ics'  
    max_age = 100  
    csv_deliiter = ';'
    date_format = '%d/%m/%Y'

    birthdays = read_birthdays_from_csv(csv_file, csv_deliiter, date_format)  
    events = create_birthday_events(birthdays, max_age)  
    create_ical_file(events, ical_file)  
