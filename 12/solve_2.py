import copy 
import time

# state = [
#     {'posX': -1, 'posY': 0, 'posZ': 2, 'velX': 0, 'velY': 0, 'velZ': 0 },
#     {'posX': 2, 'posY': -10, 'posZ': -7, 'velX': 0, 'velY': 0, 'velZ': 0 },
#     {'posX': 4, 'posY': -8, 'posZ': 8, 'velX': 0, 'velY': 0, 'velZ': 0 },
#     {'posX': 3, 'posY': 5, 'posZ': -1, 'velX': 0, 'velY': 0, 'velZ': 0 }
# ]

state = [
    {'posX': -8, 'posY': -10, 'posZ': 0, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': 5, 'posY': 5, 'posZ': 10, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': 2, 'posY': -7, 'posZ': 3, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': 9, 'posY': -8, 'posZ': -3, 'velX': 0, 'velY': 0, 'velZ': 0 }
]

# state = [
    # {'posX': -19, 'posY': -4, 'posZ': 2, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': -9, 'posY': 8, 'posZ': -16, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': -4, 'posY': 5, 'posZ': -11, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 1, 'posY': 9, 'posZ': -13, 'velX': 0, 'velY': 0, 'velZ': 0 }
# ]


print("Starting moon sim...")
initState = copy.deepcopy(state)
stepCount = 0
t0 = time.perf_counter()
while(True):

    # Add gravity to velocities
    # Change only [i], not [ii]
    for i in range(len(state)):
        for ii in range(len(state)):
            if i == ii: continue
            if state[i]['posX'] > state[ii]['posX']: state[i]['velX'] -= 1
            elif state[i]['posX'] < state[ii]['posX']: state[i]['velX'] += 1
            if state[i]['posY'] > state[ii]['posY']: state[i]['velY'] -= 1
            elif state[i]['posY'] < state[ii]['posY']: state[i]['velY'] += 1
            if state[i]['posZ'] > state[ii]['posZ']: state[i]['velZ'] -= 1
            elif state[i]['posZ'] < state[ii]['posZ']: state[i]['velZ'] += 1

    # Add velocities to positions
    for i in range(len(state)):
        state[i]['posX'] += state[i]['velX']
        state[i]['posY'] += state[i]['velY']
        state[i]['posZ'] += state[i]['velZ']
    
    stepCount += 1

    # Check for init repeat
    hasMatch = True
    for i in range(len(state)):
        hasMatch = hasMatch and state[i]['posX'] == initState[i]['posX'] and state[i]['posY'] == initState[i]['posY'] and state[i]['posZ'] == initState[i]['posZ'] and state[i]['velX'] == initState[i]['velX'] and state[i]['velY'] == initState[i]['velY'] and state[i]['velZ'] == initState[i]['velZ']
    if hasMatch: break

    if(stepCount % 1000000 == 0):
        t1 = time.perf_counter()
        print(f"    step={stepCount}: elapsed={t1-t0:0.3f} sec")



print(f"Steps until return: {stepCount}")
t1 = time.perf_counter()
print(f"Elapsed={t1-t0:0.3f} sec")


