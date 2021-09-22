cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()

for i in cro:
    string = string.replace(i,'0')

print(len(string))
