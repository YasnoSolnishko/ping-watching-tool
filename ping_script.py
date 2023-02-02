
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pythonping
import time
import statistics

plt.style.use('fivethirtyeight')

hostname = "www.google.com"
x_vals = []
y_vals = []
window_size = 60 # The size of the sliding window, in seconds
start_time = time.time() # Get the start time of the script

index = count()

def animate(i):
    latest_index = next(index)
    x_vals.append(latest_index)
    p = pythonping.ping(hostname, count=1, timeout=2, size=32)
    latest_y = p.rtt_avg_ms
    y_vals.append(latest_y)
    if latest_index > window_size:
        x_vals.pop(0) # Remove the first point
        y_vals.pop(0) # Remove the first point 
    #print(f'index {latest_index}, window_size {window_size}, {latest_index > window_size}, x_len {len(x_vals)}, y_len {len(y_vals)}')
    plt.cla()
    plt.plot(x_vals, y_vals)
    plt.annotate(f'Host name: {hostname}', xy=(0, 1), xycoords='axes fraction', fontsize=12,
                xytext=(0, 0), textcoords='offset points',
                ha='left', va='top')
    plt.annotate(f'Current RTT: {p.rtt_avg_ms} ms', xy=(0, 1), xycoords='axes fraction', fontsize=12,
                xytext=(0, -20), textcoords='offset points',
                ha='left', va='top')
    plt.annotate(f'Max RTT: {round(max(y_vals), 2)} ms', xy=(0, 1), xycoords='axes fraction', fontsize=12,
                xytext=(0, -40), textcoords='offset points',
                ha='left', va='top')
    plt.annotate(f'Min RTT: {round(min(y_vals), 2)} ms', xy=(0, 1), xycoords='axes fraction', fontsize=12,
                xytext=(0, -60), textcoords='offset points',
                ha='left', va='top')
    plt.annotate(f'Avg. RTT(last 60 sec:): {round(statistics.mean(y_vals), 2)} ms', xy=(0, 1), xycoords='axes fraction', fontsize=12,
                xytext=(0, -80), textcoords='offset points',
                ha='left', va='top')                
    
   
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
