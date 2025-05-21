import psutil
import math
import time

memory_info = psutil.virtual_memory()
print(memory_info)



memory_gigabytes = memory_info[0] / math.pow(1024, 3) # isto i **
print(f"Your memory in gigabytes is: {memory_gigabytes:<5.2f} GB\n")




process = psutil.process_iter(['cpu_percent'])
for proc in process:
    #time.sleep(0.5)
    proc.cpu_percent(interval=None)
    print(f"CPU Percent is: {proc.cpu_percent(): .2f}%")



for proc in process:
    print(proc.cpu_percent())

cpu_usage = psutil.cpu_percent(interval=1)

print(f"Total CPU Usage is: {cpu_usage: .2f}%")
cores = psutil.cpu_count(logical=False)
print(f"Number of Physical Cores: {cores}")
logical_cores = psutil.cpu_count(logical=True)
print(f"Number of Logical Cores: {logical_cores}")

current_process = psutil.Process()
number_of_threads = current_process.num_threads()
print(f"Number of Threads in Current Process is: {number_of_threads}")



mem_usage = psutil.cpu_percent(interval = 1)
print(f"{mem_usage}%")

virtual = psutil.virtual_memory()
print(virtual)

mem_giga = virtual[0] / math.pow(1024 , 3)
print(f"Your RAM is: {round(mem_giga, 2)} GB")




