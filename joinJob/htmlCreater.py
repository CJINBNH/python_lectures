from userInterface import temperatureView
from userInterface import preassureView
from userInterface import windSpeedView

def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += ' <p {}> Temperature: {} c</p>\n'\
        .format(style, temperatureView(device))
    html += ' <p {}> Wind Speed: {} m/s</p>\n'\
        .format(style, windSpeedView(device))
    html += ' <p {}> Preassure: {} mmHg</p>\n'\
        .format(style, preassureView(device))
    html += '</body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)
    return html

def newCreate(data, device = 1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += ' <p {}> Temperature: {} c</p>\n'\
        .format(style, t)
    html += ' <p {}> Wind Speed: {} m/s</p>\n'\
        .format(style, w)
    html += ' <p {}> Preassure: {} mmHg</p>\n'\
        .format(style, p)
    html += '</body>\n</html>'
    with open('newIndex.html', 'w') as page:
        page.write(html)
    return data