import itertools

def runProgram(machineStates, srcIdx, destIdx):

    def getParamVal(codes, instPtr, paramNum, modes):
        paramCode = codes[instPtr + paramNum]
        mode = 0
        paramIdx = paramNum - 1
        if(paramIdx < len(modes)):
            mode = modes[paramIdx]

        if(mode == 0):
            # print(f"    PARAMS: param[{paramNum}] at {instPtr + paramNum} has mode={mode}: idx={paramCode},  value={codes[paramCode]}")
            return codes[paramCode]
        else:
            # print(f"    PARAMS: param[{paramNum}] at {instPtr + paramNum} has mode={mode}: value={paramCode}")
            return paramCode

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
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{srcIdx}@{instPtr}] add: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal + secondVal}")
            codes[resultIdx] = firstVal + secondVal
            instPtr = instPtr + 4

        # MUL
        elif(opCode == 2):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{srcIdx}@{instPtr}] mul: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal * secondVal}")
            codes[resultIdx] = firstVal * secondVal
            instPtr = instPtr + 4

        # GET INPUT
        elif(opCode == 3):
            if len(inputVals) > 0:
                inputVal = inputVals.pop(0)
                resultIdx = codes[instPtr + 1]
                print(f"    [{srcIdx}@{instPtr}] input: inputVal={inputVal}, resultIdx={resultIdx}, remaining inputs: {inputVals}")
                codes[resultIdx] = inputVal
                instPtr = instPtr + 2
            else:
                print(f"    [{srcIdx}@{instPtr}] input: no inputs; stalling machine {srcIdx}...")
                return {"isFinished": False, "lastOutput": lastOutput}

        # SET OUTPUT
        elif(opCode == 4):
            outputVal = getParamVal(codes, instPtr, 1, paramModes)
            print(f"    [{srcIdx}@{instPtr}] OUTPUT: destIdx={destIdx}, value={outputVal}")
            machineStates[destIdx]["inputs"].append(outputVal)
            lastOutput = outputVal
            instPtr = instPtr + 2

        # JUMP IF TRUE
        elif(opCode == 5):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            print(f"    [{srcIdx}@{instPtr}] jmp_if_true: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal != 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # JUMP IF FALSE
        elif(opCode == 6):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            print(f"    [{srcIdx}@{instPtr}] jmp_if_false: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal == 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # LESS THAN
        elif(opCode == 7):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{srcIdx}@{instPtr}] less_than: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal < secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

        # EQUALS
        elif(opCode == 8):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{srcIdx}@{instPtr}] equals: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal == secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

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
    return {"isFinished": True, "lastOutput": lastOutput}

codesStr = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
permutes = [(5, 6, 7, 8, 9), (6, 7, 8, 9, 5), (9, 8, 7, 6, 5)]

# codesStr = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
# permutes = [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0), (5, 4, 3, 2, 1), (1, 0, 4, 3, 2)]

# codesStr = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
# permutes = [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0), (5, 4, 3, 2, 1), (1, 0, 4, 3, 2)]
# permutes = list(itertools.permutations([0, 1, 2, 3, 4]))

# codesStr = "3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99"
# permutes = list(itertools.permutations([5, 6, 7, 8, 9]))

bestThrust = 0
bestPhase = (0, 0, 0, 0, 0)

for phases in permutes:
    codes = list(map(int, list(codesStr.split(","))))
    print(f"Running phases {phases}")

    machineStates = [
        {"isFinished": False, "codes": codes, "instPtr": 0, "inputs": [phases[0], 0]},
        {"isFinished": False, "codes": codes, "instPtr": 0, "inputs": [phases[1]]},
        {"isFinished": False, "codes": codes, "instPtr": 0, "inputs": [phases[2]]},
        {"isFinished": False, "codes": codes, "instPtr": 0, "inputs": [phases[3]]},
        {"isFinished": False, "codes": codes, "instPtr": 0, "inputs": [phases[4]]}
    ]

    loopCount = 0
    lastOutput = -1
    isLooping = True
    while(isLooping):
        allFinished = True
        for i in range(0, 5):
            # if(machineStates[i]["isFinished"] is True): continue

            nextIdx = i + 1 if i < 4 else 0
            result = runProgram(machineStates, i, nextIdx)
            isFinished = result["isFinished"] is True
            machineStates[i]["isFinished"] = isFinished
            print(f"    MAIN[{loopCount}]: machine {i} isFinished={isFinished}: " + ("FINISHED" if isFinished else "not finished") + f": returned {result}\n")
            allFinished = allFinished and isFinished
            if(isFinished and i == 4):
                lastOutput = result["lastOutput"]
                print(f"    MAIN[{loopCount}]: machine {i} is finished; loop complete: lastOutput={lastOutput}")
                allFinished = True
        isLooping = not allFinished
        loopCount += 1
        if(loopCount > 10): break

    print(f"    lastOutput={lastOutput}")
    if(lastOutput > bestThrust):
        bestThrust = lastOutput
        bestPhase = phases

print(f"BEST thrust: {bestThrust}")
print(f"BEST phase: {bestPhase}")
