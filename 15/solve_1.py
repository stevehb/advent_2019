import itertools
import subprocess as sp
from msvcrt import getch

def runProgram(machineStates, srcIdx, destIdx):

    def getParamAddr(machineState, paramNum, modes):
        codes = machineState["codes"]
        instPtr = machineState["instPtr"]
        paramCode = codes[instPtr + paramNum]
        mode = 0
        paramIdx = paramNum - 1
        if(paramIdx < len(modes)):
            mode = modes[paramIdx]

        if(mode == 0): return paramCode
        # if(mode == 1): return paramCode  # Should never happen
        if(mode == 2): return machineState["relativeBase"] + paramCode
        print(f"ERROR: unknown paramMode={mode} at instPtr={instPtr}")
        return -1

    def getParamVal(machineState, paramNum, modes):
        codes = machineState["codes"]
        instPtr = machineState["instPtr"]
        paramCode = codes[instPtr + paramNum]
        mode = 0
        paramIdx = paramNum - 1
        if(paramIdx < len(modes)):
            mode = modes[paramIdx]
        if(mode == 0): return codes[paramCode]
        if(mode == 1): return paramCode
        if(mode == 2): return codes[machineState["relativeBase"] + paramCode]
        print(f"ERROR: unknown paramMode={mode} at instPtr={instPtr}")
        return -1


    machineState = machineStates[srcIdx]
    codes = machineState["codes"]
    instPtr = machineState["instPtr"]
    inputVals = machineState["inputs"]
    lastOutput = 0

    while instPtr < len(codes):
        fullOpCode = codes[instPtr]
        opCode = fullOpCode % 100
        paramModes = list(map(int, list(str(int((fullOpCode - opCode) / 100))[::-1])))

        # ADD
        if(opCode == 1):
            firstVal = getParamVal(machineState, 1, paramModes)
            secondVal = getParamVal(machineState, 2, paramModes)
            resultIdx = getParamAddr(machineState, 3, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] add: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal + secondVal}")
            codes[resultIdx] = firstVal + secondVal
            instPtr = instPtr + 4

        # MUL
        elif(opCode == 2):
            firstVal = getParamVal(machineState, 1, paramModes)
            secondVal = getParamVal(machineState, 2, paramModes)
            resultIdx = getParamAddr(machineState, 3, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] mul: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal * secondVal}")
            codes[resultIdx] = firstVal * secondVal
            instPtr = instPtr + 4

        # GET INPUT
        elif(opCode == 3):
            if len(inputVals) > 0:
                inputVal = inputVals.pop(0)
                resultIdx = getParamAddr(machineState, 1, paramModes)
                # print(f"    [{srcIdx}@{instPtr}] input: inputVal={inputVal}, resultIdx={resultIdx}, remaining inputs: {inputVals}")
                codes[resultIdx] = inputVal
                instPtr = instPtr + 2
            else:
                # print(f"    [{srcIdx}@{instPtr}] input: no inputs; stalling machine {srcIdx}...")
                return {"isFinished": False, "lastOutput": lastOutput}

        # SET OUTPUT
        elif(opCode == 4):
            outputVal = getParamVal(machineState, 1, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] OUTPUT: destIdx={destIdx}, value={outputVal}")
            machineState["outputs"].append(outputVal)
            if(destIdx != -1):
                machineStates[destIdx]["inputs"].append(outputVal)
            lastOutput = outputVal
            instPtr = instPtr + 2

        # JUMP IF TRUE
        elif(opCode == 5):
            conditionVal = getParamVal(machineState, 1, paramModes)
            jumpVal = getParamVal(machineState, 2, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] jmp_if_true: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal != 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # JUMP IF FALSE
        elif(opCode == 6):
            conditionVal = getParamVal(machineState, 1, paramModes)
            jumpVal = getParamVal(machineState, 2, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] jmp_if_false: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal == 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # LESS THAN
        elif(opCode == 7):
            firstVal = getParamVal(machineState, 1, paramModes)
            secondVal = getParamVal(machineState, 2, paramModes)
            resultIdx = getParamAddr(machineState, 3, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] less_than: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal < secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

        # EQUALS
        elif(opCode == 8):
            firstVal = getParamVal(machineState, 1, paramModes)
            secondVal = getParamVal(machineState, 2, paramModes)
            resultIdx = getParamAddr(machineState, 3, paramModes)
            # print(f"    [{srcIdx}@{instPtr}] equals: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal == secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

        # SET RELATIVE BASE
        elif(opCode == 9):
            firstVal = getParamVal(machineState, 1, paramModes)
            machineState["relativeBase"] += firstVal
            instPtr = instPtr + 2

        # EXIT SUCCESS
        elif(opCode == 99):
            # Finished machines should just stall on instruction 99
            # instPtr = instPtr + 1
            break

        # EXIT ERROR
        else:
            print(f"something is broken: instPtr={instPtr}, opCode={opCode}")
            break

        machineState["codes"] = codes
        machineState["instPtr"] = instPtr
        machineState["inputs"] = inputVals

    # print(f"CODES: {codes}")
    machineState["isFinished"] = True
    return




codesStr = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,102,1,1034,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,1002,1038,1,1043,101,0,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,101,0,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,7,1032,1006,1032,165,1008,1040,37,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,39,1044,1105,1,224,1101,0,0,1044,1105,1,224,1006,1044,247,102,1,1039,1034,102,1,1040,1035,101,0,1041,1036,102,1,1043,1038,102,1,1042,1037,4,1044,1106,0,0,35,37,2,26,91,30,85,34,87,18,47,29,50,23,7,46,94,2,26,42,36,23,3,32,65,21,63,18,54,31,52,75,4,35,24,24,74,33,81,89,75,50,36,43,7,20,45,9,23,10,70,12,81,62,12,51,3,5,96,7,93,90,12,41,5,52,30,91,12,62,34,44,92,68,9,81,9,6,30,38,63,27,51,3,44,47,27,86,41,1,73,78,15,34,98,9,63,66,21,89,96,5,9,36,21,97,6,26,75,14,86,16,82,21,23,91,25,15,66,33,2,50,26,18,61,73,17,49,15,99,19,68,96,33,23,12,81,11,51,19,30,56,74,27,40,76,15,49,11,24,50,27,50,36,77,36,16,22,80,86,11,85,20,87,24,26,6,64,35,27,65,32,86,42,99,30,78,68,24,67,82,4,76,63,36,4,46,21,72,68,17,21,69,71,36,82,22,57,1,29,95,59,18,48,40,91,7,44,22,64,5,52,20,20,86,34,9,67,74,22,13,31,97,23,19,78,19,12,80,19,82,83,11,26,5,10,74,2,42,5,94,26,79,51,33,15,47,9,12,84,20,37,85,63,27,92,16,10,82,64,15,50,75,12,68,51,37,87,10,51,18,11,13,99,97,30,33,48,2,45,29,22,45,20,49,14,78,33,41,89,4,67,21,40,42,20,4,34,64,98,32,77,28,79,9,51,91,58,19,45,56,4,10,3,52,47,65,11,21,53,25,57,78,33,16,70,88,34,56,37,86,30,4,84,91,86,90,37,37,25,59,2,96,25,19,69,6,11,67,83,38,8,49,18,17,21,56,20,43,89,8,78,30,80,52,29,9,65,1,1,65,27,84,23,8,33,99,71,28,38,45,14,40,31,45,44,12,94,12,65,23,96,5,93,50,35,84,10,34,81,2,51,15,11,92,69,20,65,27,68,86,76,36,49,38,79,92,38,72,8,32,80,29,41,7,15,78,38,5,10,61,24,44,38,19,80,9,60,95,95,33,48,13,51,32,57,84,97,1,51,36,6,51,96,16,62,32,13,93,4,79,40,2,68,74,38,4,30,82,17,67,51,68,29,3,85,13,5,2,30,71,36,77,35,78,23,87,22,7,78,5,60,2,11,42,15,68,89,66,93,31,38,31,81,8,65,22,7,27,83,59,21,12,73,64,72,40,38,59,20,29,92,20,7,65,16,86,81,12,44,77,97,30,19,49,61,24,29,24,31,87,89,31,42,80,17,91,23,18,91,10,53,5,17,53,30,96,96,34,83,34,18,68,79,97,18,4,56,37,33,62,31,79,99,32,14,99,87,83,53,34,26,17,70,59,31,12,42,91,32,93,5,54,8,10,83,20,58,92,30,71,24,34,60,3,9,64,72,12,70,14,22,69,38,27,77,31,84,8,54,44,58,9,30,95,22,12,61,95,21,81,71,5,64,44,7,71,4,17,41,2,89,16,20,93,88,20,31,45,28,49,91,15,72,43,6,21,82,15,25,99,8,11,34,18,93,50,15,15,98,27,34,44,38,15,29,79,42,14,86,68,56,7,3,97,21,58,11,33,67,6,53,23,71,16,58,74,17,92,17,14,98,23,35,60,32,70,54,1,82,2,41,32,68,91,27,80,6,25,55,93,23,52,91,3,95,44,3,42,70,23,16,54,36,36,59,5,63,27,40,11,73,34,48,29,73,36,74,77,58,25,55,25,45,7,58,53,49,8,95,13,84,23,58,37,42,6,70,36,58,73,55,14,51,5,99,95,61,20,65,0,0,21,21,1,10,1,0,0,0,0,0,0"
codes = list(map(int, list(codesStr.split(","))))
print(f"Parsed {len(codes)} codes")
# Add extra memory for writing past the codes input
codes.extend([0] * 10240)

machineStates = [
    {
        "isFinished": False, 
        "relativeBase": 0,
        "codes": codes.copy(), "instPtr": 0, 
        "inputs": [], "outputs": []
    }
]


MAP_W = 81
MAP_H = 61
droidMap = [x[:] for x in [[-1] * MAP_W] * MAP_H]
droidX = int(MAP_W / 2) + 1
droidY = int(MAP_H / 2) + 1
droidMap[droidY][droidX] = 1
mapBarStr = '-' * MAP_W

lastMessage = ""
isRunning = True
while(isRunning):
    # Create the map string    
    mapStrs = []
    mapStrs.append("")
    mapStrs.append("|" + mapBarStr + "|")
    for y in range(MAP_H):
        rowStr = "|"
        for x in range(MAP_W):
            tile = droidMap[y][x]
            if(x == droidX and y == droidY):
                rowStr += "D"
            elif(tile == -1):
                rowStr += " "
            elif(tile == 0):
                rowStr += "#"
            elif(tile == 1):
                rowStr += "."
            elif(tile == 2):
                rowStr += "O"
        rowStr += "|"
        mapStrs.append(rowStr)
    mapStrs.append("|" + mapBarStr + "|")

    # Draw the map
    tmp = sp.call('cls', shell=True)
    for rowStr in mapStrs: print(rowStr)

    print("")
    if lastMessage:
        print(lastMessage)
        lastMessage = ""
        print("")
    
    # Get and parse input
    print(f"Current position: [{droidX}, {droidY}]")
    print("Input: ", end="")
    inputDir = -1
    nextX = droidX
    nextY = droidY
    key = ord(getch())
    if(key == 27 or key == 113):  # ESC or 'q'
        print("Quitting")
        isRunning = False
        break
    elif(key == 224):
        key = ord(getch())
        if(key == 75):  # LEFT
            inputDir = 3
            nextX -= 1
            print("LEFT")
        elif(key == 72):  # UP
            inputDir = 1
            nextY -= 1
            print("UP")
        elif(key == 77):  # RIGHT
            inputDir = 4
            nextX += 1
            print("RIGHT")
        elif(key == 80):  # DOWN
            inputDir = 2
            nextY += 1
            print("DOWN")
    
    if(inputDir == -1):
        lastMessage += f"Invalid input {key}; try again"
        continue

    machineStates[0]['inputs'] = [inputDir]
    machineStates[0]['outputs'] = []
    runProgram(machineStates, 0, -1)
    result = machineStates[0]['outputs'][0]
    lastMessage += f"\nRan inputs={[inputDir]}; Got outputs={machineStates[0]['outputs']}"
    if(result == 0):
        lastMessage += f"\nHit a wall at [{nextX}, {nextY}]"
        droidMap[nextY][nextX] = 0
    elif(result == 1):
        lastMessage += f"\nMoved to [{nextX}, {nextY}]"
        droidX = nextX
        droidY = nextY
        droidMap[nextY][nextX] = 1
    elif(result == 2):
        lastMessage += f"\nSuccess! Found Oxygen at [{nextX}, {nextY}]"
        droidX = nextX
        droidY = nextY
        droidMap[nextY][nextX] = 2



    # print("1 = North, 2 = South, 3 = West, 4 = East, 0 = Quit")
    # inputStr = input("Directions: ").strip()
    # dirCmds = list(inputStr)
    # dirCmds = list(map(str.strip, dirCmds))
    # dirCmds = [i for i in dirCmds if i] 
    # dirCmds = list(map(int, dirCmds))
    # for dirCmd in dirCmds:
    #     nextX = droidX
    #     nextY = droidY
    #     if(dirCmd == 0):
    #         print("Quitting")
    #         isRunning = False
    #         break
    #     elif(dirCmd == 1):
    #         nextY -= 1
    #     elif(dirCmd == 2):
    #         nextY += 1
    #     elif(dirCmd == 3):
    #         nextX -= 1
    #     elif(dirCmd == 4):
    #         nextX += 1
    #     else:
    #         lastMessage += f"\nIgnoring unknown command {dirCmd}"
    #         continue
        
    #     # Send commands and handle result
    #     machineStates[0]['inputs'] = [dirCmd]
    #     machineStates[0]['outputs'] = []
    #     runProgram(machineStates, 0, -1)
    #     result = machineStates[0]['outputs'][0]
    #     lastMessage += f"\nRan inputs={[dirCmd]}; Got outputs={machineStates[0]['outputs']}"
    #     if(result == 0):
    #         lastMessage += f"\nHit a wall at [{nextX}, {nextY}]"
    #         droidMap[nextY][nextX] = 0
    #     elif(result == 1):
    #         lastMessage += f"\nMoved to [{nextX}, {nextY}]"
    #         droidX = nextX
    #         droidY = nextY
    #         droidMap[nextY][nextX] = 1
    #     elif(result == 2):
    #         lastMessage += f"\nSuccess! Found Oxygen at [{nextX}, {nextY}]"
    #         droidX = nextX
    #         droidY = nextY
    #         droidMap[nextY][nextX] = 2
    print("")
    print("")
    print("")

print("End of loop")
