

# codesStr = "1,9,10,3,2,3,11,0,99,30,40,50"
# codesStr = "1,1,1,4,99,5,6,0,99"
codesStr = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
# codesStr = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0"

def runProgram(codes, noun, verb):
    codes[1] = noun
    codes[2] = verb

    i = 0
    while i < len(codes):
        code = int(codes[i])

        if(code == 99):
            break

        firstIdx = int(codes[i + 1])
        firstVal = int(codes[firstIdx])
        secondIdx = int(codes[i + 2])
        secondVal = int(codes[secondIdx])
        resultIdx = int(codes[i + 3])

        resultVal = 0
        if(code == 1):
            resultVal = firstVal + secondVal
        elif(code == 2):
            resultVal = firstVal * secondVal
        else:
            print(f"something is broken: idx={i}, code={code}")
            break

        # print(f"i={i}, code={code}, firstVal={firstVal}, secondVal={secondVal}, resultVal={resultVal}")
        codes[resultIdx] = resultVal

        i = i + 4

    return codes[0]


for nounVal in range(0, 100):
    for verbVal in range(0, 100):
        codes = codesStr.split(",")
        output = runProgram(codes, nounVal, verbVal)
        if(int(output) == 19690720):
            print(f"noun={nounVal}, verb={verbVal}, output={output}")
            print(f"answer={(nounVal * 100) + verbVal}")
        # if(int(output) == 19690720):
        #     print("!!! ^^^^ !!!")
