import psutil

cpunums=psutil.cpu_count()
pycpunums= psutil.cpu_count(logical=False)

print(cpunums)
print(pycpunums)