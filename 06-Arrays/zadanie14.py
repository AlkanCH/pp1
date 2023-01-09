names = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]

longest=""

for i in range(0,len(names)):
    if len(names[i])>len(longest):
        longest=names[i]

print(longest)