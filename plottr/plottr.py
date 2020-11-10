import os
import json


# Local import statements
from universe import Universe
from series import Series
from novel import Novel

# Folders
ROOT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
CONFIG_DIR = os.path.join(ROOT_DIR, 'files') 




# FLAGS
load_file = True

# ARGS
universe = ''
series = ''
novel = ''


# The universe for which all connected stories take place
# Load a Universe
temp_json_universe_file = os.path.join(CONFIG_DIR, 'test_json_data_1.json') 
if load_file:
    with open(temp_json_universe_file) as json_file:
        data = json.load(json_file)







# Builder Functions
# If a universe does not exist, create one
if not universe:
    universe =  Universe()
# If a series does not exist, create one
if not series:
    series = Series()
# If a novel does not exist, create one
if not novel:
    novel = Novel()


universe.add_series(series)
series.add_novel(novel)



print(novel.__dict__)
print(getattr(novel,'title'))


 