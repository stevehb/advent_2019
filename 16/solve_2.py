from timeit import default_timer as timer
import numpy as np


def generatePattern(patternSize):
    orig = [ 0, 1, 0, -1 ]
    pattern = [] * patternSize
    for i in range(0, patternSize):
        row = np.repeat(orig, i+1)
        row = np.tile(row, int(patternSize / len(row)) + 1)
        row = row[1:patternSize+1]
        pattern.append(row)
        if(i % 10000 == 0):
            print(f"   at pattern row {i}")
    return pattern

# inputStr = "03036732577212944063491565474664"
# inputStr = "02935109699940807407585447034323"
inputStr = "59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822"
inputs = list(map(int, list(inputStr)))
inputs = np.array(inputs * 1)
print(f"Input length: {len(inputs)}")
startTime = timer()
pattern = generatePattern(len(inputs))
endTime = timer()
print(f"Generated multiple pattern in {endTime-startTime} sec")
offset = int(inputStr[0:7])
print(f"Offset will be at index {offset}")

PHASE_COUNT = 100

nextPhaseInput = inputs
phaseOutput = np.empty(len(nextPhaseInput), dtype=np.int64)
print(f"Starting {PHASE_COUNT} phases")
startTime = timer()
for phase in range(1, PHASE_COUNT+1):
    phaseOutput = np.empty(len(nextPhaseInput), dtype=np.int64)
    for i in range(len(nextPhaseInput)):
        phaseOutput[i] = abs(np.sum(np.multiply(nextPhaseInput, pattern[i]))) % 10
    nextPhaseInput = phaseOutput
    # if(phase % 10 == 0):
    endTime = timer()
    print(f"Phase[{phase}] total elapsed: {endTime - startTime} seconds")

    if(phase == PHASE_COUNT):
        endTime = timer()
        outputStr = ''.join(list(map(str, phaseOutput)))
        offsetStr = outputStr[offset:offset+8]
        firstEight = outputStr[0:8]
        print(f"PHASE {phase}: offsetStr: {offsetStr} (firstEight: {firstEight})")
        print(f"TIME: {endTime - startTime} seconds")
