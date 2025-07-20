class Person:
    def __init__(self, name, factor = 1.0):
        self.name = name
        self.factor = factor
        self.pref_days = []
        self.assigned_shifts = 0
        self.total_shifts = 0

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
shift_requirements = {
    "Shift 1": 2,
    "Shift 2": 1,
}'''

import calendar

def get_workdays(year, month,holiday):
    _, num_days = calendar.monthrange(year, month)
    return [day for day in range(1, num_days + 1) if calendar.weekday(year, month, day) not in holiday]  # Mon-Fri

def assign_shifts(people, year, month,requirements):
    workdays = get_workdays(year, month,[4])
    for p in people:
        p.total_shifts += p.assigned_shifts
        p.assigned_shifts = 0

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