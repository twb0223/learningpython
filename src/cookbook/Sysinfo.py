import psutil

cpunums=psutil.cpu_count()
pycpunums= psutil.cpu_count(logical=False)


mem=psutil.users()
print(cpunums)
print(pycpunums)
print(mem)