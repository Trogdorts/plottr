from utils import *

class Universe(object):
    def __init__(self, series = []):
        self.series = series
        print("Created new universe.")
        self.serial = create_serial(self)
    

    def add_series(self, series):
        self.series.append(series)
        
    def get_series(self):
        return self.series
        
        
    def get_universe(self):
        pass
        
        
        
