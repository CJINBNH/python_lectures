import dataProvider as prov
import logger as log

def temperatureView(sensor):
    data = prov.getTemperature(sensor)
    log.temperatureLogger(data)
    return data
def preassureView(sensor):
    data = prov.getPreassure(sensor)
    log.preassureLogger(data)
    return data
def windSpeedView(sensor):
    data = prov.getWindSpeed(sensor)
    log.windSpeedLogger(data)
    return data