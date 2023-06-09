import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')

# Set the camera resolution
width = 10
height = 10

# Set the speed of the bar
speed = 1  # px/ms
period = 1/speed  # ms


# Generate events of a white bar on a dark background
events = {"x": [], "y": [], "ts": [], "pol": []}
time = 0

for x in np.arange(width):
    y = np.random.choice(np.arange(0, height), size=height, replace=False)
    ts_tmp = [np.random.uniform(time, time+period) for _ in range(height)]
    ts = sorted(np.round(ts_tmp, decimals=2))
    for idx in range(0, len(y)):
        events['x'].append(x)
        events['y'].append(y[idx])
        events['ts'].append(ts[idx])
        events['pol'].append(1)
    time+=period

#visualisation events
time_window = 1 #ms
time_tmp=time_window
matrix_events = np.zeros((height,width))
fig = plt.figure()
for idx in range(0, len(events['x'])):
    matrix_events[events['y'][idx], events['x'][idx]] = events['pol'][idx]
    if events['ts'][idx] >= time_tmp:
        plt.imshow(matrix_events)  # or ax.imshow(frame)
        plt.draw()
        plt.pause(0.0001)
        matrix_events = np.zeros((height, width))
        time_tmp += time_window

print('end')
