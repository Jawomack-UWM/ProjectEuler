

f = open('names.txt')
names = f.read().replace('"', '').split(',')
names.sort()
print(names)