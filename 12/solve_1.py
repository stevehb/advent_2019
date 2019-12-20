

# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>
# state = [
    # {'posX': -1, 'posY': 0, 'posZ': 2, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 2, 'posY': -10, 'posZ': -7, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 4, 'posY': -8, 'posZ': 8, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 3, 'posY': 5, 'posZ': -1, 'velX': 0, 'velY': 0, 'velZ': 0 }
# ]

# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
# state = [
    # {'posX': -8, 'posY': -10, 'posZ': 0, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 5, 'posY': 5, 'posZ': 10, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 2, 'posY': -7, 'posZ': 3, 'velX': 0, 'velY': 0, 'velZ': 0 },
    # {'posX': 9, 'posY': -8, 'posZ': -3, 'velX': 0, 'velY': 0, 'velZ': 0 }
# ]


# <x= -19, y= -4, z=2>
# <x= -9, y= 8, z=-16>
# <x= -4, y= 5, z=-11>
# <x= 1, y= 9, z=-13>
state = [
    {'posX': -19, 'posY': -4, 'posZ': 2, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': -9, 'posY': 8, 'posZ': -16, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': -4, 'posY': 5, 'posZ': -11, 'velX': 0, 'velY': 0, 'velZ': 0 },
    {'posX': 1, 'posY': 9, 'posZ': -13, 'velX': 0, 'velY': 0, 'velZ': 0 }
]


MAX_STEPS = 1000


# for i in range(len(state)):
#     print(f"STEP  0: pos=[{state[i]['posX']}, {state[i]['posY']}, {state[i]['posZ']}]; vel=<{state[i]['velX']}, {state[i]['velY']}, {state[i]['velZ']}>")

for stepCount in range(1, MAX_STEPS+1):

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

    # for i in range(len(state)):
    #     print(f"STEP {stepCount:2d}: pos=[{state[i]['posX']}, {state[i]['posY']}, {state[i]['posZ']}]; vel=<{state[i]['velX']}, {state[i]['velY']}, {state[i]['velZ']}>")

accumE = 0
for i in range(len(state)):
    pot = abs(state[i]['posX']) + abs(state[i]['posY']) + abs(state[i]['posZ'])
    kin = abs(state[i]['velX']) + abs(state[i]['velY']) + abs(state[i]['velZ'])
    print(f"ENERGY [{i}]: pot={pot}, kin={kin}, total={pot * kin}")
    accumE += (pot * kin)

print(f"Total energy: {accumE}")



