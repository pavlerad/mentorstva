import platform
from platform import python_version, python_build, system

python_version = platform.python_version()
python_build = platform.python_build()
print(f"You Python version is {python_version}. Have a great day!")
print(f"You Python build is {python_build}. Have a great day!\n")

if int(python_version[0]) != 3:
    print("Your Python version is not up to date. Please update it.")
else:
    print("Your Python version is up to date. Have a great day!\n")




info = platform.system()
print(info)

version = platform.python_version()
processor = platform.processor()
python_version = platform.python_version()
arch = platform.architecture()
machine = platform.machine()
edit = platform.win32_edition()


print(f"{info} | {version} | {processor} | {python_version} | {arch} | {machine} | {edit}")
