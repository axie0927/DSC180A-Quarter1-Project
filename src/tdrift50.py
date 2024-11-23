# This function calculates the time taken from the initiation of charge generation to the collection at the detector's point contact at the threshold of 50%.

import numpy as np

def get_tdrift50(waveform, start_idx = 1000):
    
    # Find the index of the peak value
    max_idx = np.argmax(waveform)

    # Calculate the middle y-value (50%) between start and max
    start_y = waveform[start_idx]
    max_y = waveform[max_idx]
    mid_y = (start_y + max_y) / 2

    # Find the x-value (index) where the waveform crosses the middle y-value
    mid_x_idx = start_idx + np.argmax(waveform[start_idx:max_idx] >= mid_y)

    tdrift50 = mid_x_idx - start_idx 

    return int(tdrift50)