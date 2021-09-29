from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file


# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)


class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4


porsche = Car()
porsche.color = "Red"

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"
