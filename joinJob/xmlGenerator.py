from userInterface import temperatureView
from userInterface import preassureView
from userInterface import windSpeedView

def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperatureView(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind speed view>\n'\
        .format(windSpeedView(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(preassureView(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def newCreate(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data