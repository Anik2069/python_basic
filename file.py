
#r+ read and write
anikfile=open("anik.txt",'r')

print(anikfile.readable())

print(anikfile.read())
print(anikfile.read())
print(anikfile.readline())

print(anikfile.readlines())


anikfile.close()

