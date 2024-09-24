"""
    Author: Alperen Aydın
    Description: Thompson Sampling Algorithm (Reinforced Learning)
"""

import random
import pandas as pd

def ts(data) -> int:
    if not type(data) == pd.DataFrame:
        raise Exception("Data type must be DataFrame")
    
    n = len(data)
    d = len(data.columns)
    ones = [0] * d
    zeros = [0] * d
    tco = []
    total = 0

    for i in range(1,n):
        chosen = 0
        max_ts = 0
        for j in range(0,d):
            ranbeta = random.betavariate(ones[j] + 1,zeros[j] + 1)
            if ranbeta > max_ts:
                max_ts = ranbeta
                chosen = j
        tco.append(chosen)
        reward = data.values[i,chosen]
        if reward == 1:
            ones[chosen] = ones[chosen] + 1  
        else:
            zeros[chosen] = zeros[chosen] + 1
        total += reward

    print(total)
