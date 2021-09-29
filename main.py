from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file


# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)


class Car:
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    def start(self):
        print(self.doors)
        print("I started")


porsche = Car()
porsche.color = "Red Sexy Red"
porsche.start()
