import pandas as pd

class PoolState():

    def __init__(self, address):
        self.address = address
        self.ticks_df = pd.DataFrame()
        
