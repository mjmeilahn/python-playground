
from datetime import datetime
import pytz
import os
tz = pytz.timezone('US/Pacific')
begin = datetime.now(tz)
mdy = datetime.now(tz).strftime('%m-%d-%y')

"""
PUT THE FOLLOWING AT THE TOP OF YOUR SCRIPT:
from log import Log
l = Log('unique-log-id-goes-here')
log, endLog = l.log, l.endLog

EXAMPLE:
...start of script...
log(event)

...middle of script...

endLog()
...end of script...
"""

class Log:
    def __init__(self, name):
        self.name = name.strip()
        self.file = os.path.join(os.getcwd(), 'logs', f'{self.name}-{mdy}-log.txt')
        open(self.file, 'w+')
        self.update('Running at ' + begin.strftime('%I:%M:%S%p %Z'))

    def update(self, content):
        print(self.name + ': ' + content)
        file = open(self.file, 'a')
        file.write(content + '\n')
        file.close()

    def log(self, message):
        since = str(datetime.now(tz) - begin).split('.')[0]
        self.update(f'{message} ({since})')

    def endLog(self):
        end = datetime.now(tz).strftime('%I:%M:%S%p %Z')
        total = str(datetime.now(tz) - begin).split('.')[0]
        self.update(f'Finished at {end} ({total})')
