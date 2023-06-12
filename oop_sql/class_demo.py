

"""
Author: David Luby
Date: 6/8/2023
Purpose:
    This program is a refresher of class in Python. It features basic
    class definition and manipulation, inheritance, and polymorphism.
"""


class fluid():

    # class attribute - consistent across instances
    state = 'liquid'

    # instance attributes - unique to each instance
    def __init__(self, position, velocity, temperature, pressure):
        self.position = position    # initial position
        self.velocity = velocity    # initial velocity
        self.temperature = temperature  # intiial temperature
        self.pressure = pressure    # initial pressure

    # class method - consistent functions across instances
    def update_position(self, time_step):
        self.position = self.position + self.velocity * time_step
        return self.position    # return statement works like a function here
    

class water(fluid):

    # class attributes
    density = 1000  # kg/m^3
    specific_heat = 4.2 # kj/(kg*k)
    temp_freezing = 0   # celcius
    temp_boiling = 100  # celcius


fluid_inst = fluid(0, 5, 25, 1000)
fluid_inst.update_position(5)
print()
print('Fluid state and position: ', fluid_inst.state, fluid_inst.position)


water_inst = water(0, 5, 25, 1000)
water_inst.update_position(5)
print()
print('Water state, specific heat, and position: ', water_inst.state, water_inst.specific_heat, water_inst.position)



class Team:

    def __init__(self, team_name, city, sport):
        self.team_name = team_name    # team name
        self.city = city    # team location 
        self.sport = sport  # team sport


class Player(Team):

    # instance attributes must contain ALL arguments from parent AND child
    def __init__(self, team_name, city, sport, player_name, height,position):
        # then the parent instance attributes must be called
        super().__init__(team_name, city, sport)
        self.player_name = player_name    # player name
        self.height = height    # height in inches
        self.position = position    # player position

    def print_information(self):
        return print(f'{self.player_name} is a {self.position} for the {self.city} {self.team_name}')


star_player = Player('Celtics', 'Boston', 'Basketball', 'Jayson Tatum', 82, 'PF')
print()
star_player.print_information()