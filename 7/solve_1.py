import itertools

def runProgram(codes, inputVals):

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

    inputCounter = 0
    instCount = 0
    instPtr = 0
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
            # print(f"    [{instCount}] add: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal + secondVal}")
            codes[resultIdx] = firstVal + secondVal
            instPtr = instPtr + 4

        # MUL
        elif(opCode == 2):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            # print(f"    [{instCount}] mul: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal * secondVal}")
            codes[resultIdx] = firstVal * secondVal
            instPtr = instPtr + 4

        # READ AND SET INPUT
        elif(opCode == 3):
            resultIdx = codes[instPtr + 1]
            # print(f"    [{instCount}] input: inputCounter={inputCounter}, inputValue={inputVals[inputCounter]}, resultIdx={resultIdx}")
            codes[resultIdx] = inputVals[inputCounter]
            inputCounter = inputCounter + 1
            instPtr = instPtr + 2

        # READ AND PRINT OUTPUT
        elif(opCode == 4):
            resultVal = getParamVal(codes, instPtr, 1, paramModes)
            # print(f"    [{instCount}] OUTPUT: instPtr={instPtr}, output: {resultVal}")
            lastOutput = resultVal
            instPtr = instPtr + 2

        # JUMP IF TRUE
        elif(opCode == 5):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            # print(f"    [{instCount}] jmp_if_true: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal != 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # JUMP IF FALSE
        elif(opCode == 6):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            # print(f"    [{instCount}] jmp_if_false: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal == 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # LESS THAN
        elif(opCode == 7):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            # print(f"    [{instCount}] less_than: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
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
            # print(f"    [{instCount}] equals: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal == secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

        # EXIT SUCCESS
        elif(opCode == 99):
            instPtr = instPtr + 1
            break

        # EXIT ERROR
        else:
            print(f"something is broken: instPtr={instPtr}, opCode={opCode}")
            break

        instCount += 1

    # print(f"CODES: {codes}")
    return lastOutput

# WORKS
# codesStr = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
# permutes = [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0)]

# codesStr = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
# permutes = [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0), (5, 4, 3, 2, 1), (1, 0, 4, 3, 2)]

# codesStr = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
# permutes = [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0), (5, 4, 3, 2, 1), (1, 0, 4, 3, 2)]
# permutes = list(itertools.permutations([0, 1, 2, 3, 4]))

codesStr = "3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99"
permutes = list(itertools.permutations([0, 1, 2, 3, 4]))

bestThrust = 0
bestPhase = (0, 0, 0, 0, 0)
phaseCount = 0
for phases in permutes:
    codes = list(map(int, list(codesStr.split(","))))
    secondInput = 0
    output = 0
    print(f"Running phase {phaseCount}: {phases}")
    phaseCount += 1
    for phaseInput in phases:
        output = runProgram(codes, (phaseInput, secondInput))
        secondInput = output
    print(f"    output={output}")
    if(output > bestThrust):
        bestThrust = output
        bestPhase = phases

print(f"BEST thrust: {bestThrust}")
print(f"BEST phase: {bestPhase}")
