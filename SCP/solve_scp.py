from random import randint
from copy import copy

from data_structures import *


def run_mrv():
    return backtrack(mrv, init_domains(), Schedule([], [], []))


# Ініціалізує домени для кожного уроку
def init_domains():
    domain = {}
    buf = []
    buf_lecture = []
    # Створює доменні елементи для кожного дня, часового слоту та аудиторії
    for day in week_schedule.keys():
        for time_slot in time_schedule.keys():
            for room in classrooms:
                buf.append(DomainEl(day, time_slot, room))
                if room.is_big:
                    buf_lecture.append(DomainEl(day, time_slot, room))
    # Призначає домени для уроків
    for i in range(len(lessons)):
        if lessons[i].is_lecture:
            domain[i] = copy(buf_lecture)
        else:
            domain[i] = copy(buf)
    return domain

# Оновлює домени після вибору уроку
def update_domain(domain, lesson, day, time, room):
    for key in domain:
        buf = []
        for d in domain[key]:
            if not (d.day == day and d.time == time and d.room == room) and not ( # ОБМЕЖЕННЯ
                d.day == day
                and d.time == time
                and (
                    lessons[key].teacher == lesson.teacher
                    or set(map(str, lessons[key].group)) & set(map(str, lesson.group))
                )
            ):
                buf.append(d)
        domain[key] = buf

    return domain

# MRV для вибору уроку
def mrv(domain):
    min_len = len(week_schedule) * len(classrooms) * len(time_schedule) * 2
    ind = list(domain.keys())[0]
    for key, value in domain.items():
        if len(value) < min_len:
            min_len = len(value)
            ind = key
    return ind

# Функція зворотного відстеження для пошуку рішення
def backtrack(heuristic, domain, schedule):
    if not domain:
        return schedule
    ind = heuristic(domain)
    if ind == -1:
        return None
    for d in domain[ind]:
        sch_copy = copy(schedule)
        sch_copy.times.append(Time(d.day, d.time))
        sch_copy.classrooms.append(d.room)
        sch_copy.lessons.append(lessons[ind])

        dom_copy = copy(domain)
        dom_copy.pop(ind)
        dom_copy = update_domain(dom_copy, lessons[ind], d.day, d.time, d.room)

        res = backtrack(heuristic, dom_copy, sch_copy)
        if res:
            return res

    return None

