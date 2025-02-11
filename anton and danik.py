import re
n = input()
s = input()
Danik = len(re.findall(r'D', s))
Anton = len(s)  - Danik
if(Danik > Anton):
  print("Danik")
elif(Danik == Anton):
  print("Friendship")
else:
  print("Anton")
