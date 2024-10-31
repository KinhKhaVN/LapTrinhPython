import json



students = [
    {"name": "Kinh Kha",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "hobbies": ["reading", "traveling", "coding"],
    "education": {
        "undergrad": "Physics",
        "grad": "Computer Science"
    }},
    
    {"name": "Thanh Ngan",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "hobbies": ["reading", "traveling", "coding"],
    "education": {
        "undergrad": "Physics",
        "grad": "Computer Science"
    }}
]

with open("input.json", "r") as fin:
    data = json.load(fin)

with open("output.json", "w") as fout:
    json.dump(students, fout, indent = 4, separators=(", ", ": "))

