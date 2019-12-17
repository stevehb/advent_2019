import itertools
from timeit import default_timer as timer

def generatePattern(patternSize):
    orig = [ 0, 1, 0, -1 ]
    pattern = list()
    for i in range(0, patternSize):
        pattern.append([item for item in orig for j in range(i + 1)])
    for i in range(0, patternSize):
        mul = int(patternSize / len(pattern[i])) + 1
        pattern[i] = pattern[i] * mul
        pattern[i] = pattern[i][1:patternSize+1]
        # pattern[i] = pattern[i][:patternSize]
    return pattern

# inputStr = "12345678"
# inputStr = "80871224585914546619083218645595"
# inputStr = "19617804207202209144916044189917"
inputStr = "59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822"
inputs = list(map(int, list(inputStr)))
startTime = timer()
pattern = generatePattern(len(inputs))
endTime = timer()
print(f"Generated multiple patter in {endTime-startTime} sec")

PHASE_COUNT = 100


nextPhaseInput = inputs
phaseOutput = []
print(f"Starting {PHASE_COUNT} phases")
startTime = timer()
for phase in range(1, PHASE_COUNT+1):
    phaseOutput = []
    for i in range(len(nextPhaseInput)):
        phaseOutput.append(abs(sum([a * b for a,b in zip(nextPhaseInput, pattern[i])])) % 10)
    nextPhaseInput = phaseOutput
    if(phase % 10 == 0):
        endTime = timer()
        print(f"Phase[{phase}] total elapsed: {endTime - startTime} seconds")

    if(phase == PHASE_COUNT):
        endTime = timer()
        print(f"PHASE {phase}: {''.join(list(map(str, phaseOutput))[:8])}")
        print(f"TIME: {endTime - startTime} seconds")
