import math

#Math util functions
def add(*coords):
    total = [0 for x in range(len(coords[0]))]
    for pair in coords:
       total = [total[x] + pair[x] for x in range(len(total))] 
    return tuple(total)

def mult(coords, scalar):
    return tuple([coord * scalar for coord in coords])

def translation(vel, time_step):
    translate = []
    for dimension in vel:
        translate.append(dimension * time_step)
    return tuple(translate)

def acceleration(accel, time_step):
    delta_v = []
    for dimension in accel:
        delta_v.append(dimension * time_step)
    return tuple(delta_v)

#Compute a physics step with position velocity, accelerations, and time increment
def step(pos, vel, accel, time_step):
    initial_vel = vel
    end_vel = add(vel, acceleration(accel, time_step))

    step_vel = mult(add(initial_vel, end_vel), 1/2)
    
    end_pos = add(pos, translation(step_vel, time_step))
    
    return end_pos, end_vel

def deg_to_rad(deg):
    return deg/180 * math.pi
