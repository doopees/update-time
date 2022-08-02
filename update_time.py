#!/usr/bin/env python2

import os
import json
import commands
from datetime import datetime

_, response = commands.getstatusoutput('curl -s http://worldtimeapi.org/api/timezone/America/Lima')
api_data = json.loads(response)

date_str = api_data['datetime']
date_fmt = '%Y-%m-%dT%X.%f-05:00'
date_obj = datetime.strptime(date_str, date_fmt)

shell_cmd = date_obj.strftime('sudo date -s "%a %b %d %X -05 %Y"')
#os.system(shell_cmd)
