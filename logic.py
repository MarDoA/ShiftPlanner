import json
import calendar
class Person:
    def __init__(self, name, total_shifts = 0):
        self.name = name
        self.assigned_shifts = 0
        self.total_shifts = total_shifts
        #todo don't know yet
        self.factor = 1 
        self.pref_days = []

    def __repr__(self):
        return f"{self.name}, shifts count: {self.assigned_shifts})"
'''
#for testing
people = [
    Person("Ali", 1.0),
    Person("Sara", 1.0),
    Person("Youssef", 1.0),
    Person("pep", 1.0),
    Person("lock", 1.0),
    Person("tar", 1.0),
    Person("ther", 1.0),
]
'''
shift_requirements = {
    "0": 2,
    "1": 1,
}

def save(people):
    data = [{"name": p.name, "total_shifts": p.total_shifts} for p in people]
    with open("people.json","w") as f:
        json.dump(data,f,indent=2)

def load():
    with open("people.json","r") as f:
        data = json.load(f)
        people = [Person(d["name"], d["total_shifts"]) for d in data]
        return people

def get_workdays(year, month,holiday):
    _, num_days = calendar.monthrange(year, month)
    return [day for day in range(1, num_days + 1) if calendar.weekday(year, month, day) not in holiday]  # Mon-Fri

def assign_shifts(people, year, month,requirements=shift_requirements):
    workdays = get_workdays(year, month,[4])

    num_of_people = len(people)
    sorted_people = sorted(people, key=lambda p: p.total_shifts)
    schedule = {}
    i=0
    for day in workdays:
        schedule[day] = {}
        for shift_name, required_count in requirements.items():
            assigned = set()
            while len(assigned) < required_count:
                candidate = sorted_people[i % num_of_people]
                i+=1
                if candidate not in assigned:
                    assigned.add(candidate)
                    candidate.assigned_shifts+=1
            schedule[day][shift_name] = list(assigned)
    for p in people:
        p.total_shifts += p.assigned_shifts

    return schedule
    



'''
shifts = assign_shifts(people, 2025, 7,shift_requirements)  # July 2025
for p in people:
    print(p.name)
    print(p.assigned_shifts)

shifts = assign_shifts(people, 2025, 8,shift_requirements)  # July 2025

for p in people:
    print(p.name)
    print(p.assigned_shifts)
shifts = assign_shifts(people, 2025, 9,shift_requirements)  # July 2025

for p in people:
    print(p.name)
    print(p.assigned_shifts)
    shifts = assign_shifts(people, 2025, 10,shift_requirements)  # July 2025

for p in people:
    print(p.name)
    print(p.assigned_shifts)
    shifts = assign_shifts(people, 2025, 11,shift_requirements)  # July 2025

for p in people:
    print(p.name)
    print(p.assigned_shifts) '''