import os
from datetime import datetime
import operator

class Guard:
    def __init__(self, inpString):
        self.input = inpString
        self.id = 0
        self.datesWorked = []
        self.minutesSlept = 0
        self.sleepTimes = []
        self.wakingUpTimes = []

    def getId(self, inpString):
        return int(inpString.replace("#", ""))

    def addSleepingTime(self, time):
        self.sleepTimes.append(self.cleanTime(time))

    def addWakingTime(self, time):
        cleanedTime = self.cleanTime(time)
        self.wakingUpTimes.append(cleanedTime)
       
        # Since he woke up, we can get the minutes slept. 
        self.minutesSlept += self.calculateMinutesSlept(self.sleepTimes[-1], cleanedTime)

    def calculateMinutesSlept(self, sleepingTime, wakingTime):
        _,delim,st = sleepingTime.partition(":")
        _,delim,wt = wakingTime.partition(":")

        minutesSlept = int(wt) - int(st)

        return minutesSlept

    def createSleepingSchedule(self):
        return zip(self.sleepTimes, self.wakingUpTimes)
    
    def cleanTime(self, time):
        time = time.replace("[", "")
        return time.replace("]", "")

##################################### END CLASS #############################################

def readFile(filaNmame):
    res = []
    inputPath = os.path.abspath(filaNmame)
    print(inputPath)
    with open(inputPath, "r") as f:
        for line in f:
            res.append(line)

    return res

def getLaziestGuard(sortedInput):
    """
    Desc of data on each index
    0 - [date
    1 - time]
    2 - Guard/falls/wakes
    3 - #id/asleep/up
    """
    guards = set()
    for item in sortedInput:
        data = item.split(" ")       
        if "#" in data[3]:
            guard = Guard(data)
            guard.id = guard.getId(data[3])
            existingGuard = checkIfGuardExistInRepo(guard.id, guards)           
            if existingGuard is not False:
                guard = existingGuard
                
        if "asleep" in data[3]:
            guard.addSleepingTime(data[1])
        if "wakes" in data[2]:
            guard.addWakingTime(data[1])
        guards.add(guard)

    mostLazyGuard = max(guards, key=lambda x: x.minutesSlept)

    return mostLazyGuard, guards

def checkIfGuardExistInRepo(id, guards):
    for guard in guards:
        if guard.id == id:
            return guard
    
    return False

def getMinuteSleptMost(guard):
    sleepingSchedule = guard.createSleepingSchedule()
    scheduleList = list(sleepingSchedule)
    sets = []
    for interval in scheduleList:
        start = getMinutes(interval[0])
        end = getMinutes(interval[1])

        s = set(range(start, end))
        sets.append(s)

    d = createMinuteToCountDict(sets)
    if(len(d.keys()) > 0):

        maxMin = max(d.keys(), key=(lambda key: d[key]))
        
        count = d[maxMin]

        return (maxMin, count)
    else:
        return 0,0 

def createMinuteToCountDict(sets):
    minutes = []

    for item in sets:
        minutes += list(item)

    minToCount = {}
    
    for minute in minutes:
        if minute in minToCount:
            minToCount[minute] += 1
        else:
            minToCount[minute] = 0

    return minToCount
   
def getMinutes(time):
    return int(time.split(":")[1])

###################### PART 2 ###############################################################
def getMostMinuteSleptByAGuard(guard):
    minute, count = getMinuteSleptMost(guard)

    return (minute, count)

def getMinutesSleptByGuards(guards):
    maxCount = 0
    maxMin = 0
    gid = 0
    for guard in guards:
        minute, count = getMostMinuteSleptByAGuard(guard)
        if count > maxCount:
            maxCount = count
            maxMin = minute
            gid = guard.id
        
    return (maxMin, gid)



########################### MAIN #############################################################
def main():
    inputs = readFile("input.txt")
    sortedInp = sorted(inputs)
    mostLazyGuard, guards = getLaziestGuard(sortedInp)
    print(mostLazyGuard.id)

    print(getMinuteSleptMost(mostLazyGuard))

    # PART TWO
    print(getMinutesSleptByGuards(guards))



if __name__ == "__main__":
    main()

