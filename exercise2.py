
heights:list[float] = []
SENTINEL: int = -999
while True:
    height: float = float(input('enter heights:'))
    if height <1.60 or height >3.0:
        break
    if not 1.60 or height > 3.0:
          continue
    heights.append(height)
#1
    print(f"amount of players == {len(heights)}")  # gets the maximum value
#2
    print(f"max value player == {max(heights)}")
#3
    print(f"min value player == {min(heights)}")
#4
    print(f"avg == {sum(heights) / len(heights)}")
#5
    are_taller_than_2=0
    for i in range(3):
        if   height >2.0:
            break
    print(f"How many players are taller than 2.0 meters?{height}")

#6
    higher_than_average=0
    for i in range(2,3) :
            if sum(heights) / len(heights):
                higher_than_average +=1
                break
    print("Is it higher than average")

