import math

ball_state = {'pos': (0,1.5), 'vel': (9.39, 0)}
time_range = (0, 1)
time_step = 0.01
record_interval = 0.02
gravity = (0,-10)
drag_C = .7
paper_mass = 4.5/1000
paper_area = 4/100

def add(*coords):
    total = [0 for x in range(len(coords[0]))]
    for pair in coords:
       total = [total[x] + pair[x] for x in range(len(total))] 
    return tuple(total)

def mult(coords, scalar):
    return tuple([coord * scalar for coord in coords])

def tuple_round(in_tuple, places):
    return tuple([round(item, places) for item in in_tuple])

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

def drag(velocity, cd, mass, area, p=1.29):
    accel = []
    for vel_component in velocity:
        drag_force = cd * area * (p * vel_component**2)/2 * -1 if vel_component >= 0 else 1
        accel.append(drag_force/mass)
    return tuple(accel)

def compute_step(state, time_step):
    initial_velocity = state['vel'] 
    #print(f"Velocity: {state['vel']} Drag: {acceleration(drag(state['vel'], drag_C, paper_mass, paper_area), time_step)}")
    state['vel'] = add(state['vel'], acceleration(gravity, time_step)) #, acceleration(drag(state['vel'], drag_C, paper_mass, paper_area), time_step))
    step_velocity = mult(add(initial_velocity, state['vel']), 1/2)
    state['pos'] = add(state['pos'], translation(step_velocity, time_step))
    return state 

time = time_range[0] 
states = [[time, tuple_round(ball_state['pos'], 8), tuple_round(ball_state['vel'], 8)]]
for x in range(int((time_range[1]-time_range[0])/time_step)):
    time = round(time + time_step, 8)
    ball_state = compute_step(ball_state, time_step)
    if x%(int(record_interval/time_step)) == int(record_interval/time_step)-1:
        states.append([time, tuple_round(ball_state['pos'], 8), tuple_round(ball_state['vel'], 8)])

for item in states:
    print(item)
