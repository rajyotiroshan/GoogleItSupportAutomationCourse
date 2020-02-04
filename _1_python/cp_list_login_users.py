#helper function
def get_event_date(event):
    return event.date
#return machines: a dictionary of set where key->machine set->user currently login
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type = "login":
            machines[event.machine].add(event.user)
        elif event.user in machines[event.machine] and event.type = "logout":
            machines[event.machines].remove(event.user)
    return machines
#print machines/generate report
def generate_report(machines):
    for machine, user in machines.items():
        for machine, users in machines.items():
            if len((users)) > 0:
                user_list = ", ".join(users)
                print("{}: {}".format(machine, user_list))
