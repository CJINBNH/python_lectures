from datetime import datetime as dt
def temperatureLogger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'.format(time, data))

def preassureLogger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};preassure;{}\n'.format(time, data))

def windSpeedLogger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind speed;{}\n'.format(time, data))