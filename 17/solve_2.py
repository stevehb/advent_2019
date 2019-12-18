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

codesStr = "2,330,331,332,109,3492,1101,1182,0,15,1101,1483,0,24,1002,0,1,570,1006,570,36,101,0,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,15,1,15,1008,15,1483,570,1006,570,14,21101,58,0,0,1105,1,786,1006,332,62,99,21101,333,0,1,21101,73,0,0,1105,1,579,1102,1,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1001,574,0,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21101,340,0,1,1106,0,177,21102,477,1,1,1106,0,177,21102,514,1,1,21101,176,0,0,1106,0,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,1002,572,1,1182,21102,1,375,1,21102,211,1,0,1105,1,579,21101,1182,11,1,21102,222,1,0,1105,1,979,21102,1,388,1,21101,233,0,0,1105,1,579,21101,1182,22,1,21101,244,0,0,1105,1,979,21102,401,1,1,21102,1,255,0,1105,1,579,21101,1182,33,1,21101,266,0,0,1106,0,979,21101,414,0,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1,1182,1,21101,0,313,0,1106,0,622,1005,575,327,1101,0,1,575,21101,327,0,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,24,22,0,109,4,1202,-3,1,587,20101,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2105,1,0,109,5,2102,1,-4,630,20102,1,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,652,21001,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,702,1,0,1106,0,786,21201,-1,-1,-1,1105,1,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1106,0,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21102,774,1,0,1105,1,622,21201,-3,1,-3,1105,1,640,109,-5,2106,0,0,109,7,1005,575,802,20101,0,576,-6,20101,0,577,-5,1106,0,814,21101,0,0,-1,21102,1,0,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,49,-3,22201,-6,-3,-3,22101,1483,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21101,0,1,-1,1105,1,924,1205,-2,873,21101,35,0,-4,1105,1,924,1202,-3,1,878,1008,0,1,570,1006,570,916,1001,374,1,374,2102,1,-3,895,1102,1,2,0,2102,1,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21002,0,1,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,49,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,41,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1102,1,1,575,21102,1,973,0,1106,0,786,99,109,-7,2106,0,0,109,6,21102,0,1,-4,21102,1,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21102,1,-4,-2,1105,1,1041,21102,1,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1201,-2,0,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1202,-2,1,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21101,0,439,1,1106,0,1150,21101,0,477,1,1105,1,1150,21101,514,0,1,21102,1,1149,0,1106,0,579,99,21101,0,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,2102,1,-4,0,109,-6,2105,1,0,40,9,40,1,7,1,40,1,7,1,40,1,7,1,22,9,9,1,7,1,22,1,7,1,9,1,7,1,22,1,7,1,9,1,7,1,22,1,7,1,9,1,7,1,22,1,7,1,9,1,7,1,22,1,7,1,9,1,7,1,10,11,1,1,7,1,7,11,10,1,9,1,1,1,7,1,7,1,1,1,18,1,9,1,1,1,7,11,18,1,9,1,1,1,15,1,20,1,3,9,15,1,20,1,3,1,5,1,17,1,20,1,3,1,5,1,17,1,20,1,3,1,5,1,17,1,20,1,3,1,5,1,17,1,20,1,3,1,5,1,17,1,18,11,1,13,5,1,18,1,1,1,3,1,3,1,13,1,5,1,10,11,3,11,3,11,10,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,1,9,1,3,1,16,1,7,1,9,13,1,11,6,1,7,1,19,1,1,1,11,1,6,9,19,13,1,1,36,1,9,1,1,1,36,1,9,1,1,1,36,1,9,1,1,1,36,1,9,1,1,1,36,1,9,1,1,1,36,1,3,9,36,1,9,1,38,11,8"

codes = list(map(int, list(codesStr.split(","))))
print(f"Parsed {len(codes)} codes")


# A,A,B,C,B,C,B,C,C,A
# A: L,10,R,8,R,8
# B: L,10,L,12,R,8,R,10
# C: R,10,L,12,R,10
inputs = []
inputs.extend(list(map(ord, "A,A,B,C,B,C,B,C,C,A\n")))
inputs.extend(list(map(ord, "L,10,R,8,R,8\n")))
inputs.extend(list(map(ord, "L,10,L,12,R,8,R,10\n")))
inputs.extend(list(map(ord, "R,10,L,12,R,10\n")))
inputs.extend(list(map(ord, "n\n")))


# Add extra memory for writing past the codes input
codes.extend([0] * 10240)
machineStates = [
    {
        "isFinished": False, 
        "relativeBase": 0,
        "codes": codes.copy(), "instPtr": 0, 
        "inputs": inputs, "outputs": []
    }
]


runProgram(machineStates, 0, -1)
outputs = machineStates[0]['outputs']
print(f"Outputs len: {len(outputs)}")
print(f"Output: {outputs}")

