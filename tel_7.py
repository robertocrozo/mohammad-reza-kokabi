x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = []
for i in range(len(x)):
    if i % 2 == 0:
        new.append (x[i])
print(x)



x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = []
i = 0
while i < len(x):
    new.append(x[i])
    i += 2
print(new)
