import platform


print(f"{platform.machine}, {platform.system()}, {platform.python_version()}, {platform.processor()}, {platform.release()}, {platform.python_build()}, {platform.machine()}")






version = platform.python_version()
version = int(version[0])
print(version)

if version != 3:
    print("Please update your Python.")
else:
    print("Your Python is up to date.")




