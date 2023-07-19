from datetime import date
from models.event import Event

event1 = Event('codeclan open week', date.fromisoformat('2023-07-19'), "castle terrace", 5, 'A welcome day at the campus', False) 
event2 = Event('codeclan graduation', date.fromisoformat('2023-10-20'), "castle terrace", 24, 'A party for our graduates', False) 

events=[event1, event2]

def add_new_event(event):
    events.append(event)

