#======================================================
#COE67-222 Operating Systems - Lab 01 Report
#Name: Danich Khawngam
#Student ID: 67100479
#======================================================
import os
import platform
import psutil

print(f"OS Name: {platform.system()} {platform.release()}")
print(f"Number of CPU Cores: {psutil.cpu_count(logical=True)}")
print(f"Total RAM: {psutil.virtual_memory().total / (1024**3):.2f} GiB")

