from time import time
from solve_scp import *  
from data_structures import * 

# Функція для друку розкладу
def print_schedule(solution: Schedule):
    for day in week_schedule:  # Прохід по дням тижня
        print("\n" + "=" * 100)
        print(f"{week_schedule[day].upper()}")
        for time in time_schedule:  # Прохід по часових слотах
            print("\n\n" + time_schedule[time])
            for c in classrooms:  # Прохід по аудиторіям
                print(f"\n{c}", end="\t\t")
                for i in range(len(solution.lessons)):  # Перевірка та вивід занять
                    if (solution.times[i].weekday == day and
                        solution.times[i].time == time and
                        solution.classrooms[i].room == c.room):
                        print(solution.lessons[i], end="")



# Запуск програми
if __name__ == "__main__":
    solution = run_mrv()
    print_schedule(solution)
