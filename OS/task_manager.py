import psutil
import time


print(psutil.cpu_percent())
print(psutil.version_info)
print(psutil.disk_partitions())
print(psutil.cpu_stats())
print(round(psutil.boot_time(),2))
print(psutil.cpu_times_percent())
print(psutil.net_connections())
print(f"Your CPU percent is: {psutil.cpu_percent(): .2f}%")
print(psutil.net_if_addrs())
print(psutil.cpu_count())
print(psutil.net_if_stats())
print(psutil.virtual_memory())
print(psutil.users())
print(psutil.disk_usage("C:"))


print("\n")



process = list(psutil.process_iter(["name", 'memory_percent', 'cpu_percent']))
print(f"{"NAME":<25}  {"MEMORY(%)":<10}  {"CPU(%)":<10}\n")
time.sleep(3)
for proc in process:
    proc.cpu_percent(interval=None)

time.sleep(3)

for proc in process:
    print(f"{proc.name():<25} {proc.memory_percent():<10.2f} {proc.cpu_percent(): <10.2f}")



import platform


system = platform.system()

