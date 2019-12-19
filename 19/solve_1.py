import itertools

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

codesStr = "109,424,203,1,21102,1,11,0,1105,1,282,21102,18,1,0,1106,0,259,2102,1,1,221,203,1,21102,31,1,0,1105,1,282,21101,38,0,0,1106,0,259,21002,23,1,2,22101,0,1,3,21102,1,1,1,21101,57,0,0,1105,1,303,1202,1,1,222,20102,1,221,3,20102,1,221,2,21102,1,259,1,21102,80,1,0,1105,1,225,21102,72,1,2,21101,91,0,0,1105,1,303,1201,1,0,223,20102,1,222,4,21101,0,259,3,21102,1,225,2,21102,1,225,1,21102,1,118,0,1105,1,225,20102,1,222,3,21101,104,0,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1106,0,259,1201,1,0,223,20101,0,221,4,20102,1,222,3,21101,0,18,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,106,0,109,20207,1,223,2,20101,0,23,1,21102,1,-1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,22102,1,-3,1,22102,1,-2,2,22102,1,-1,3,21101,250,0,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,0,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2105,1,0"
codes = list(map(int, list(codesStr.split(","))))
print(f"Parsed {len(codes)} codes")

# Add extra memory for writing past the codes input
codes.extend([0] * 10240)

MAX_X = 50
MAX_Y = 50
count = 0
for y in range(0, MAX_Y):
    for x in range(0, MAX_X):
        machineStates = [
            {
                "isFinished": False, 
                "relativeBase": 0,
                "codes": codes.copy(), "instPtr": 0, 
                "inputs": [x, y], "outputs": []
            }
        ]
        runProgram(machineStates, 0, -1)
        isHit = machineStates[0]['outputs'][0] == 1
        if(isHit):
            print("#", end="")
            count += 1
        else:
            print(".", end="")
    print("")
print(f"\nTotal hits: {count}")


# Total count 229 is too high
