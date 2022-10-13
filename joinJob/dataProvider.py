from random import randint
def getTemperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)
def getPreassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)
def getWindSpeed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def dataCollection(senson = 1):
    return (getTemperature(senson), getPreassure(senson), getWindSpeed(senson))