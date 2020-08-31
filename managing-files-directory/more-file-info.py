import os
print(os.path.getsize("renamed_hello_world.py"))

# 
print(os.path.getmtime("renamed_hello_world.py"))

import datetime
timestamp = os.path.getmtime("renamed_hello_world.py")
date_modified = datetime.datetime.fromtimestamp(timestamp)
print(date_modified)


path = os.abspath("renamed_hello_world.py")
print(path)
