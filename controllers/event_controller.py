from flask import render_template, Blueprint, request
from models.event_list import events, add_new_event
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title= " Event List", events=events)

@events_blueprint.route('/events', methods= ['POST'])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_location = request.form['location']
    event_guests = request.form['guests']
    event_description = request.form['description']
    event_recurring = request.form.get("recurring")
    new_event=Event(event_name, event_date, event_location, event_guests, event_description, event_recurring)

    add_new_event(new_event)
    return render_template('index.jinja', title= " Event List", events=events)

@events_blueprint.route('/events/delete', methods= ['POST'])
def remove_event():
        event_name = request.form['name']
        for event in events:
            if event_name == event.name:
                events.pop(events.index(event))
        return render_template('index.jinja', title= "Event List", events=events)

@events_blueprint.route('/events/deleteindex', methods= ['POST'])
def remove_index():
    events.pop(int(request.form["index"]))
    return render_template('index.jinja', title= "Event List", events=events)




