
# codesStr = "3,9,8,9,10,9,4,9,99,-1,8"  # Is input equal to 8
# codesStr = "3,3,1108,-1,8,3,4,3,99"  # Is input equal to 8
# codesStr = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"  # output 0 if the input was zero or 1 if the input was non-zero
# codesStr = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"  # output 0 if the input was zero or 1 if the input was non-zero

# output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8
# codesStr = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

codesStr = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,33,37,225,101,6,218,224,1001,224,-82,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1102,87,62,225,1102,75,65,224,1001,224,-4875,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,49,27,225,1101,6,9,225,2,69,118,224,101,-300,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,76,37,224,1001,224,-113,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,47,50,225,102,43,165,224,1001,224,-473,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1002,39,86,224,101,-7482,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,11,82,225,1,213,65,224,1001,224,-102,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1001,14,83,224,1001,224,-120,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,53,39,225,1101,65,76,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,226,224,1002,223,2,223,1005,224,329,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,374,1001,223,1,223,1008,677,226,224,102,2,223,223,1005,224,389,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,434,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,449,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,464,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,479,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,539,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,599,1001,223,1,223,8,677,677,224,102,2,223,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,644,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226"



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



def runProgram(codes, inputValue):
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
            print(f"    [{instCount}] add: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal + secondVal}")
            codes[resultIdx] = firstVal + secondVal
            instPtr = instPtr + 4

        # MUL
        elif(opCode == 2):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{instCount}] mul: first={firstVal}, second={secondVal}, resultIdx={resultIdx}, result={firstVal * secondVal}")
            codes[resultIdx] = firstVal * secondVal
            instPtr = instPtr + 4

        # READ AND SET INPUT
        elif(opCode == 3):
            resultIdx = codes[instPtr + 1]
            print(f"    [{instCount}] input: inputValue={inputValue}, resultIdx={resultIdx}")
            codes[resultIdx] = inputValue
            instPtr = instPtr + 2

        # READ AND PRINT OUTPUT
        elif(opCode == 4):
            resultVal = getParamVal(codes, instPtr, 1, paramModes)
            print(f"    [{instCount}] OUTPUT: instPtr={instPtr}, output: {resultVal}")
            lastOutput = resultVal
            instPtr = instPtr + 2

        # JUMP IF TRUE
        elif(opCode == 5):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            print(f"    [{instCount}] jmp_if_true: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal != 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # JUMP IF FALSE
        elif(opCode == 6):
            conditionVal = getParamVal(codes, instPtr, 1, paramModes)
            jumpVal = getParamVal(codes, instPtr, 2, paramModes)
            print(f"    [{instCount}] jmp_if_false: conditionVal={conditionVal}, jumpVal={jumpVal}")
            if(conditionVal == 0):
                instPtr = jumpVal
            else:
                instPtr = instPtr + 3

        # LESS THAN
        elif(opCode == 7):
            firstVal = getParamVal(codes, instPtr, 1, paramModes)
            secondVal = getParamVal(codes, instPtr, 2, paramModes)
            resultIdx = codes[instPtr + 3]
            print(f"    [{instCount}] less_than: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
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
            print(f"    [{instCount}] equals: firstVal={firstVal}, secondVal={secondVal}, resultIdx={resultIdx}")
            if(firstVal == secondVal):
                codes[resultIdx] = 1
            else:
                codes[resultIdx] = 0
            instPtr = instPtr + 4

        elif(opCode == 99):
            instPtr = instPtr + 1
            break
        else:
            print(f"something is broken: instPtr={instPtr}, opCode={opCode}")
            break

        # print(f"    {codes}")
        instCount += 1

    # print(f"CODES: {codes}")
    return lastOutput


codes = list(map(int, list(codesStr.split(","))))
print(f"Running IntComp with {len(codes)} codes")
print(f"CODES: {codes}")
lastOutput = runProgram(codes, 5)
print(f"lastOutput={lastOutput}")
