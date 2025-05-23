import psutil
from psutil import cpu_percent
import time

print(f"{psutil.cpu_percent()} | {psutil.virtual_memory()} | {psutil.cpu_stats()} | {psutil.process_iter()} | {psutil.users()} | {psutil.disk_usage("C:")}\n")

process = list(psutil.process_iter(['name', 'memory_percent', 'cpu_percent']))

for proc in process:
    cpu_percent(interval=None)

time.sleep(5)


print(f"{'Name':<35}{'Memory(%)':<35}{'CPU(%)':<35}\n")

for proc in process:
    print(f"{proc.name():<35}{proc.memory_percent():<35.2f}{proc.cpu_percent():<35.2f}")

