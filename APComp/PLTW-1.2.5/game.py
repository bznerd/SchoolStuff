import math
import physics
from time import time
import random

#Game object
class Game:
    #Initialize game object
    #Tick speed ms, vel m/s, gravity m/s^2, angle_rate degrees/s
    #Sets lots of parameters and makes variables
    def __init__(self, tick_speed=20, launch_velocity=350, gravity=(0,-75), angle_rate=18, height_range=(50,460)):
        self.tick_speed = tick_speed
        self.launch_velocity = launch_velocity
        self.gravity = gravity
        self.angle_rate = angle_rate
        self.height_range = height_range

        self.angle = 0 
        self.goals = 0
        self.goal_height = 0
        self.in_flight = False
        self.ball_pos = (-300,-210)
        self.ball_vel = (0,0)
        self.game_mode = "notset"
        self.time = time() 
        self.timer_limit = 30
        self.times_up = None
        self.scored = None
        self.missed = None

    #Begin a launch setting the flag and initial velocity
    def start_launch(self):
        self.in_flight = True
        self.ball_vel = physics.mult((math.cos(physics.deg_to_rad(self.get_angle())), math.sin(physics.deg_to_rad(self.get_angle()))), self.launch_velocity)

    #Reset for a new launch
    def reset(self):
        self.in_flight = False
        self.ball_pos = (-300, -210)
        self.angle = 25
        self.time - time()
        self.gen_goal()

    #Begin the timer for timed mode
    def start_timer(self):
        self.time = time()

    #Returns time since timer started
    def get_time_elapsed(self):
        return round(time() - self.time, 1)

    #Generate a goal at a random height
    def gen_goal(self):
        self.goal_height = random.randint(self.height_range[0]/10, self.height_range[1]/10)*10

    #Returns the current goal height
    def get_goal(self):
        return self.goal_height

    #Get the current score
    def get_score(self):
        return self.goals

    #Times up binding
    def set_times_up(self, func):
        self.times_up = func

    #Scored binding
    def set_scored(self, func):
        self.scored = func

    #Missed binding
    def set_missed(self, func):
        self.missed = func
    
    #Update step, does physics, collision checks, and game management
    def update_step(self):
        if self.game_mode == "timed":
            if self.time + self.timer_limit < time():
                self.times_up()

        if self.in_flight:
            self.physics_step()
            if self.collision_check():
                self.goals += 1
                self.scored()
                self.reset()

            if self.bounds_check():
                self.missed()
                self.reset()
        
        else:
            self.aim_update()

    #Update the aim using the given update rate
    def aim_update(self):
        self.angle = (self.angle + self.angle_rate/(1000/self.tick_speed))%100

    #Get the current goal angle (uses a double width range for up and down directions, so this function returns the real angle)
    def get_angle(self):
        return (self.angle + -2* (self.angle//50) * (self.angle%50))

    #Returns the current position of the ball
    def get_ball_pos(self):
        return self.ball_pos

    #Sets the game mode
    def set_game_mode(self, mode):
        self.game_mode = mode 

    #Returns the current game mode
    def get_game_mode(self):
        return self.game_mode

    #Checks if the ball has collided with the goal
    def collision_check(self):
        if self.ball_pos[0] >= 370 and self.ball_pos[1] >= self.goal_height-300 and self.ball_pos[1] <= self.goal_height-160:
            return True
        return False

    #Checks if the ball is out of bounds
    def bounds_check(self):
        if self.ball_pos[0] > 420 or self.ball_pos[1] < -250: return True
        return False

    #Computes a physcis step
    def physics_step(self):
        self.ball_pos, self.ball_vel = physics.step(self.ball_pos, self.ball_vel, self.gravity, 1/self.tick_speed)
