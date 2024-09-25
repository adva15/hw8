

numbers: list[int] = []
for i in range(1,101):
   numbers.append(i)
#b
print('first number:', numbers[0])
#c
print('last number:', numbers[-1])
#d
print('len', len(numbers))
#e
print(numbers[2:12])
#f
print(numbers[79:])
#g
print(numbers[:17])
#h
print(numbers[::-1])
#i
print(numbers[1:100:2])
#j
for i in range(len(numbers)):
   if numbers[i] % 3 == 0:
      print(numbers[i]," ", end="")
print()
#k
for i in range(len(numbers)):
  if numbers[i] % 7 == 0:
       print(numbers[i]," ", end="")
print()
#l
print(numbers[9::10])
#m
for i in range(98,66-3,-3):
   print(numbers[i]," ", end="")
print()
#n
SENTINEL: int = 999
numbers.insert(50,999)
print(numbers)
#O
numbers.pop()
print(numbers)

