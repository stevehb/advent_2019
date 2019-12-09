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
            print(f"    [{srcIdx}@{instPtr}] OUTPUT: destIdx={destIdx}, value={outputVal}")
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

# codesStr = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# codesStr = "1102,34915192,34915192,7,4,7,99,0"
# codesStr = "104,1125899906842624,99"
codesStr = "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,902,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,39,1005,1102,1,1,1021,1101,0,212,1025,1101,0,24,1014,1102,22,1,1019,1101,0,35,1003,1101,38,0,1002,1101,0,571,1026,1102,32,1,1006,1102,31,1,1000,1102,25,1,1018,1102,1,37,1016,1101,0,820,1023,1102,1,29,1004,1101,564,0,1027,1101,0,375,1028,1101,26,0,1013,1102,1,370,1029,1101,21,0,1007,1101,0,0,1020,1102,1,30,1001,1102,36,1,1011,1102,1,27,1017,1101,0,28,1012,1101,0,217,1024,1101,823,0,1022,1102,1,20,1009,1101,0,23,1010,1101,34,0,1015,1101,33,0,1008,109,5,1208,0,39,63,1005,63,199,4,187,1106,0,203,1001,64,1,64,1002,64,2,64,109,13,2105,1,6,4,209,1105,1,221,1001,64,1,64,1002,64,2,64,109,-4,21108,40,39,-1,1005,1013,241,1001,64,1,64,1105,1,243,4,227,1002,64,2,64,109,5,21102,41,1,-1,1008,1018,40,63,1005,63,267,1001,64,1,64,1106,0,269,4,249,1002,64,2,64,109,-28,1202,10,1,63,1008,63,30,63,1005,63,291,4,275,1106,0,295,1001,64,1,64,1002,64,2,64,109,24,21107,42,43,-4,1005,1011,313,4,301,1106,0,317,1001,64,1,64,1002,64,2,64,109,-8,21108,43,43,3,1005,1010,335,4,323,1105,1,339,1001,64,1,64,1002,64,2,64,109,-8,1207,4,34,63,1005,63,359,1001,64,1,64,1106,0,361,4,345,1002,64,2,64,109,26,2106,0,3,4,367,1106,0,379,1001,64,1,64,1002,64,2,64,109,-21,2102,1,-2,63,1008,63,37,63,1005,63,399,1105,1,405,4,385,1001,64,1,64,1002,64,2,64,109,2,1207,-2,30,63,1005,63,427,4,411,1001,64,1,64,1105,1,427,1002,64,2,64,109,4,2108,36,-5,63,1005,63,447,1001,64,1,64,1106,0,449,4,433,1002,64,2,64,109,-13,1201,8,0,63,1008,63,41,63,1005,63,469,1106,0,475,4,455,1001,64,1,64,1002,64,2,64,109,14,21107,44,43,3,1005,1014,495,1001,64,1,64,1106,0,497,4,481,1002,64,2,64,109,2,1205,8,511,4,503,1106,0,515,1001,64,1,64,1002,64,2,64,109,14,1206,-6,527,1105,1,533,4,521,1001,64,1,64,1002,64,2,64,109,-29,2107,31,8,63,1005,63,551,4,539,1105,1,555,1001,64,1,64,1002,64,2,64,109,28,2106,0,1,1001,64,1,64,1106,0,573,4,561,1002,64,2,64,109,-3,21101,45,0,-4,1008,1019,45,63,1005,63,595,4,579,1105,1,599,1001,64,1,64,1002,64,2,64,109,-23,1208,2,39,63,1005,63,615,1105,1,621,4,605,1001,64,1,64,1002,64,2,64,109,15,2108,32,-9,63,1005,63,643,4,627,1001,64,1,64,1105,1,643,1002,64,2,64,109,-9,2107,33,0,63,1005,63,659,1106,0,665,4,649,1001,64,1,64,1002,64,2,64,109,7,21101,46,0,2,1008,1015,49,63,1005,63,689,1001,64,1,64,1106,0,691,4,671,1002,64,2,64,109,-8,2101,0,-3,63,1008,63,35,63,1005,63,711,1105,1,717,4,697,1001,64,1,64,1002,64,2,64,109,12,1202,-9,1,63,1008,63,31,63,1005,63,741,1001,64,1,64,1105,1,743,4,723,1002,64,2,64,109,-27,2102,1,10,63,1008,63,31,63,1005,63,769,4,749,1001,64,1,64,1105,1,769,1002,64,2,64,109,9,2101,0,1,63,1008,63,31,63,1005,63,791,4,775,1106,0,795,1001,64,1,64,1002,64,2,64,109,28,1206,-7,809,4,801,1105,1,813,1001,64,1,64,1002,64,2,64,2105,1,-4,1106,0,829,4,817,1001,64,1,64,1002,64,2,64,109,-15,21102,47,1,-2,1008,1010,47,63,1005,63,851,4,835,1106,0,855,1001,64,1,64,1002,64,2,64,109,5,1205,3,867,1106,0,873,4,861,1001,64,1,64,1002,64,2,64,109,-12,1201,0,0,63,1008,63,39,63,1005,63,895,4,879,1105,1,899,1001,64,1,64,4,64,99,21101,0,27,1,21102,913,1,0,1106,0,920,21201,1,47951,1,204,1,99,109,3,1207,-2,3,63,1005,63,962,21201,-2,-1,1,21101,0,940,0,1105,1,920,21201,1,0,-1,21201,-2,-3,1,21101,0,955,0,1106,0,920,22201,1,-1,-2,1105,1,966,21202,-2,1,-2,109,-3,2105,1,0"

codes = list(map(int, list(codesStr.split(","))))
# print(f"Codes: {codes}")
codes.extend([0] * 10240)
print(f"Parsed {len(codes)} codes")
machineStates = [
    {
        "isFinished": False, 
        "relativeBase": 0,
        "codes": codes.copy(), "instPtr": 0, 
        "inputs": [1], "outputs": []
    }
]

runProgram(machineStates, 0, -1)
print(f"Outputs: {machineStates[0]['outputs']}")
