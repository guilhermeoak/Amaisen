#!/bin/bash

import subprocess
from src import *
from datetime import datetime

subprocess.run(['clear'])

print("System started...\n")

user = str(subprocess.check_output(['whoami']))[2:-3]
now = datetime.now()
print(src.util.whatToSay(now.hour), user.capitalize(), '\n')


src.EmailResource.send_email()
