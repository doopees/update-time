#!/usr/bin/env python2

# A symbolic link to this file was created in /bin/
# and @reboot /bin/update_time.py & was added to crontab.


import os
import json
import commands
from datetime import datetime


def main():
    # Wait until we get a successful response from the World Time API.
    failed = 1
    while failed:
        failed, response = commands.getstatusoutput('curl -s http://worldtimeapi.org/api/timezone/America/Lima')

    # Parse JSON string into a dictionary.
    api_data = json.loads(response)

    # Fetch the datetime data from the dictionary and build a datetime object.
    date_str = api_data['datetime']
    date_fmt = '%Y-%m-%dT%X.%f-05:00'
    date_obj = datetime.strptime(date_str, date_fmt)

    # Construct the shell command to update the system time and execute it.
    shell_cmd = date_obj.strftime('sudo date -s "%a %b %d %X -05 %Y"')
    os.system(shell_cmd)


if __name__ == '__main__':
    main()
