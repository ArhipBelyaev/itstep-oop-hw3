import random


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Auto:
    brands_of_car = {
        'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'ZAZ': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Auto.brands_of_car))
        self.fuel = Auto.brands_of_car[self.brand]['fuel']
        self.strength = Auto.brands_of_car[self.brand]['strength']
        self.consumption = Auto.brands_of_car[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('Car cant move')
            return False


class Bike:
    brands_of_bike = {
        'Kellys': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'GIANT': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Merida': {'fuel': 70, 'strength': 150, 'consumption': 8},
        'Scott': {'fuel': 80, 'strength': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Bike.brands_of_bike))
        self.fuel = Bike.brands_of_bike[self.brand]['fuel']
        self.strength = Bike.brands_of_bike[self.brand]['strength']
        self.consumption = Bike.brands_of_bike[self.brand]['consumption']


class Job:
    job_list = {
        'Java developer': {'salary': 50, 'sadness': 10},
        'Python developer': {'salary': 40, 'sadness': 3},
        'C++ developer': {'salary': 45, 'sadness': 25},
        'Rust developer': {'salary': 70, 'sadness': 1},
    }

    def __init__(self):
        self.job_title = random.choice(list(Job.job_list))
        self.salary = Job.job_list[self.job_title]['salary']
        self.sadness = Job.job_list[self.job_title]['sadness']


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None, bike=None):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.bike = bike

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto()

    def get_bike(self):
        self.bike = Bike()

    def get_job(self):
        if self.car.drive():
            self.job = Job()
        else:
            self.to_repair()

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def shopping(self, goal):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                goal = 'fuel'
            else:
                self.to_repair()
                return
        if goal == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif goal == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif goal == 'sweets':
            print('I bought sweets')
            self.money -= 15
            self.satiety += 2
            self.happiness += 10

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.happiness -= self.job.sadness
        self.satiety -= 4

    def chill(self):
        self.happiness += 10
        self.home.mess += 5

    def clean_home(self):
        self.happiness -= 5
        self.home.mess = 0

    def status(self, day):
        day_str = f'Today is the {day} day of {self.name}\'s life'
        print(f'{day_str:=^50}', '\n')
        human_info = f'{self.name}\'s info'
        print(f'{human_info:^50}', '\n')
        print(f'money: {self.money}')
        print(f'satiety: {self.satiety}')
        print(f'happiness: {self.happiness}')
        home_info = 'Home info'
        print(f'{home_info:^50}', '\n')
        print(f'food: {self.home.food}')
        print(f'mess: {self.home.mess}')
        car_info = f'{self.car.brand}\'s info'
        print(f'{car_info:^50}', '\n')
        print(f'fuel: {self.car.fuel}')
        print(f'strength: {self.car.strength}')
        bike_info = f'{self.bike.brand}\'s info'
        print(f'{bike_info:^50}', '\n')
        print(f'fuel: {self.bike.fuel}')
        print(f'strength: {self.bike.strength}')

    def is_alive(self):
        if self.happiness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False
        else:
            return True

    def live_a_day(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car: {self.car.brand}')
        if self.bike is None:
            self.get_bike()
            print(f'I bought a bike: {self.bike.brand}')
        if self.job is None:
            self.get_job()
            print(f'I am going to get a job {self.job.job_title} with salary {self.job.salary}')
        self.status(day)
        dice = random.randint(1, 6)
        if self.satiety < 20:
            print('Ill go to eat')
            self.eat()
        elif self.happiness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            print('Start working!')
            self.work()
        elif self.car.strength < 15:
            print('Gonna repair my car')
            self.to_repair()
        elif dice == 1:
            print('Lets chill!')
            self.chill()
        elif dice == 2:
            print('Start working!')
            self.work()
        elif dice == 3:
            print('Cleaning time!')
            self.clean_home()
        elif dice == 4:
            print('Time for sweets')
            self.shopping('sweets')
        elif dice == 5:
            print('I am going to ride a bike')
            self.ride_bike()
        elif dice == 6:
            print('I am going to repair my bike')
            self.repair_bike()
        return True

    def ride_bike(self):
        if self.bike.strength > 0:
            self.bike.strength -= 1
            self.satiety -= 2
        else:
            print('Bike is broken. Gonna repair it.')
            self.repair_bike()

    def repair_bike(self):
        self.bike.strength += 100
        self.money -= 30


nick = Human(name='Nick')

for day in range(1, 8):
    if not nick.live_a_day(day):
        break
