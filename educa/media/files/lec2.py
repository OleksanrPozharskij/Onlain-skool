# if value1:
#     commands
# elif value2:
#     commands
# else:
#     commands
"""
for змінна in послідовність:
   команди

for змінна in послідовність:
   команди
else:
   команди
"""
suma = 0
for i in range(10):
    suma += i
    print(i, end="\t")
print(suma)

print(list(range(11, 1, -2)))
suma = 0
for i in range(11, 1, -2):
    suma += i
    print(i, end="\t")
print(suma)

for i in "python":
    print(i, end="\t")
print("\n"+"-"*20)
"""
while умова:
    команди
else:       #доцільно, коли використовується break
    команди
"""

a=4
b=5
result=b if a>b else a
print(result)
print(str(a)+">", b,"=",result)
name=input("input name:\n")
age=int(input("input age:\n"))
print("Привіт, {0:-<10}! Тобі {1:d} років. Пішли {0} на прогалянку!".format(name,age))
print(f"Привіт, {name}! Тобі {age} років")

list1=[element for element in "Python"]

list2=[] #list()
for element in "Python":
    list2.append(element)

print(list1)
list2.insert(2,'k')
print(list2)
print(list2.index('t'))