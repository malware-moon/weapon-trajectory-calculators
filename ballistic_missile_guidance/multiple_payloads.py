"""
This script defines a Rocket class that represents the rocket, a Payload class that represents the separate payloads, and a GuidanceSystem class that handles guiding the rocket towards the target. The simulate function updates the guidance system and rocket's position over time, and the main part of the script sets up a rocket, several payloads, a target, and a guidance system, then calls the simulate function to run the simulation.

The rocket's direction is adjusted based on the distance to the target, so that the rocket will slow down as it gets closer to the target. This is just one way to approach the problem, and there may be other methods that work better for different situations.
"""


import math

class Rocket:
    def __init__(self, x, y, velocity, direction):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.direction = direction

    def update_position(self, time_delta):
        self.x += self.velocity * math.cos(self.direction) * time_delta
        self.y += self.velocity * math.sin(self.direction) * time_delta

    def change_direction(self, new_direction):
        self.direction = new_direction

class Payload:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

class GuidanceSystem:
    def __init__(self, rocket, payloads, target):
        self.rocket = rocket
        self.payloads = payloads
        self.target = target

    def update_direction(self):
        target_vector = (self.target[0] - self.rocket.x, self.target[1] - self.rocket.y)
        target_distance = math.sqrt(target_vector[0] ** 2 + target_vector[1] ** 2)
        target_direction = math.atan2(target_vector[1], target_vector[0])
        # adjust the rocket's direction based on the distance to the target
        self.rocket.change_direction(target_direction + 0.01 * target_distance)

def simulate(guidance_system, time_delta, time_limit):
    time = 0
    while time < time_limit:
        guidance_system.update_direction()
        guidance_system.rocket.update_position(time_delta)
        time += time_delta

if __name__ == '__main__':
    rocket = Rocket(0, 0, 10, 0)
    payloads = [Payload(2, 3, 1), Payload(1, 4, 2), Payload(5, 6, 3)]
    target = (10, 10)
    guidance_system = GuidanceSystem(rocket, payloads, target)
    simulate(guidance_system, 1, 20)