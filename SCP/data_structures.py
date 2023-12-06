from collections import namedtuple

# Визначення графіка тижня та часових слотів
week_schedule = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
time_schedule = {
    1: "8:40-10:15",
    2: "10:35-12:10",
    3: "12:20-13:55",
}

# Основні класи даних, використовуючи namedtuple
Classroom = namedtuple("Classroom", "room is_big")
Time = namedtuple("Time", "weekday time")
Teacher = namedtuple("Teacher", "name")
Subject = namedtuple("Subject", "name")
Group = namedtuple("Group", "name")
Lesson = namedtuple("Lesson", "teacher subject group is_lecture per_week")
Schedule = namedtuple("Schedule", "lessons classrooms times")
DomainEl = namedtuple("DomainEl", "day time room")

# Кастомні методи __repr__ для кращого відображення об'єктів
Classroom.__repr__ = lambda c: f"Аудиторія {c.room}"
Teacher.__repr__ = lambda t: f"{t.name.split()[1]}"
Subject.__repr__ = lambda s: f"{s.name.split()[1]}"
Group.__repr__ = lambda g: f"{g.name}"
Lesson.__repr__ = (
    lambda l: f"{l.teacher} | {l.subject} | {l.group} | "
    f"{'Лекція' if l.is_lecture else 'Семінар'} {l.per_week}/week"
)

# Функція для відображення розкладу
def gen_repr(g: Schedule):
    output = ""
    for i in range(len(g.lessons)):
        output += f"{g.lessons[i]},   {g.classrooms[i]},   {g.times[i]}\n"
    return output

# Перевизначення методу __repr__ для Schedule
Schedule.__repr__ = lambda g: gen_repr(g)

# Прикладні дані для створення розкладу
# Список аудиторій
classrooms = [
    Classroom(1, True),
    Classroom(2, True),
    Classroom(3, True),
    Classroom(4, False),
    Classroom(5, False),
    Classroom(6, False),
]

# Створення часових слотів для розкладу
schedule = [
    Time(w, n)
    for w in range(1, len(week_schedule.keys()) + 1)
    for n in range(1, len(week_schedule.keys()) + 1)
]

# Список викладачів
teachers = [
    Teacher(name)
    for name in (
        "0 Teacher1",
        "1 Teacher2",
        "2 Teacher3",
        "3 Teacher4",
        "4 Teacher5",
        "5 Teacher6",
        "6 Teacher7",
        "7 Teacher8",
        "8 Teacher9",
        "9 Teacher10",
        "10 Teacher11",
    )
]

# Список предметів
subjects = [
    Subject(name)
    for name in (
        "0 Subject1",
        "1 Subject2",
        "2 Subject3",
        "3 Subject4",
        "4 Subject5",
        "5 Subject6",
        "6 Subject7",
        "7 Subject8",
        "8 Subject9",
        "9 Subject10",
        "10 Subject11",
    )
]

# Список груп
groups = [
    Group(name)
    for name in (
        "Group1",
        "Group2",
        "Group3",
        "Group4",
        "Group5",
    )
]

# Список уроків
lessons = [
    Lesson(teachers[0], subjects[0], groups[0], False, 1),
    Lesson(teachers[1], subjects[1], groups[0:5], True, 1),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[4], subjects[4], groups[0:5], True, 1),
    Lesson(teachers[5], subjects[4], groups[0], False, 1),
    Lesson(teachers[5], subjects[4], groups[1], False, 1),
    Lesson(teachers[5], subjects[4], groups[2], False, 1),
    Lesson(teachers[6], subjects[4], groups[1], False, 1),
    Lesson(teachers[5], subjects[4], groups[3], False, 1),
    Lesson(teachers[5], subjects[4], groups[4], False, 1),
    Lesson(teachers[6], subjects[4], groups[3], False, 1),
    Lesson(teachers[6], subjects[4], groups[4], False, 1),
    Lesson(teachers[6], subjects[4], groups[1], False, 1),
    Lesson(teachers[7], subjects[4], groups[2], False, 1),
    Lesson(teachers[8], subjects[3], groups[1:3], True, 1),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
]
