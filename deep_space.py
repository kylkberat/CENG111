"""
1) Take an input containing 3 probes, all three probs \
contains these three variables: pos(x), pos(y), pos(z), \
mass, fuel level.

2) abs_x = x if x >= 0 else -x...

3) Manhattan Distance D = abs_x + abs_y + abs_z

4) lag = D * 0.05
  # x is negative AND y is positive lag += 20
  # z is 0 lag -= 5
  if lag < 0
     lag = 0

5) Calculate the energy (fuel * 100) / (mass * (lag + 1))
6) Determine the status of Efficiency Score.
7) Calculate lag, eff, status for three probes.
8) Sort the probes based on efficiency from high to low
9) print the details in the sorted order.

"""

deep = eval(input())

id1, x1, y1, z1, mass1, fuel1 = deep[0]
id2, x2, y2, z2, mass2, fuel2 = deep[1]
id3, x3, y3, z3, mass3, fuel3 = deep[2]


absx1 = x1 if x1 >= 0 else -x1
absx2 = x2 if x2 >= 0 else -x2
absx3 = x3 if x3 >= 0 else -x3

absy1 = y1 if y1 >= 0 else -y1
absy2 = y2 if y2 >= 0 else -y2
absy3 = y3 if y3 >= 0 else -y3

absz1 = z1 if z1 >= 0 else -z1
absz2 = z2 if z2 >= 0 else -z2
absz3 = z3 if z3 >= 0 else -z3


dist1 = absx1 + absy1 + absz1
dist2 = absx2 + absy2 + absz2
dist3 = absx3 + absy3 + absz3


lag1 = dist1 * 0.05
lag2 = dist2 * 0.05
lag3 = dist3 * 0.05

lag1 = lag1 + 20 if (x1 < 0 and y1 > 0) else lag1
lag2 = lag2 + 20 if (x2 < 0 and y2 > 0) else lag2
lag3 = lag3 + 20 if (x3 < 0 and y3 > 0) else lag3

lag1 = lag1 - 5 if z1 == 0 else lag1
lag2 = lag2 - 5 if z2 == 0 else lag2
lag3 = lag3 - 5 if z3 == 0 else lag3

lag1 = 0 if lag1 < 0 else lag1
lag2 = 0 if lag2 < 0 else lag2
lag3 = 0 if lag3 < 0 else lag3

e1 = (fuel1 * 100) / (mass1 * (lag1 + 1))
e2 = (fuel2 * 100) / (mass2 * (lag2 + 1))
e3 = (fuel3 * 100) / (mass3 * (lag3 + 1))

if e1 > 5.0:
    e1r = "Optimal"
elif 5.0 >= e1 >= 1.0:
    e1r = "Stable"
elif e1 < 1.0:
    e1r = "CRITICAL"

if e2 > 5.0:
    e2r = "Optimal"
elif 5.0 >= e2 >= 1.0:
    e2r = "Stable"
elif e2 < 1.0:
    e2r = "CRITICAL"

if e3 > 5.0:
    e3r = "Optimal"
elif 5.0 >= e3 >= 1.0:
    e3r = "Stable"
elif e3 < 1.0:
    e3r = "CRITICAL"

row1 = [id1, lag1, e1, e1r]
row2 = [id2, lag2, e2, e2r]
row3 = [id3, lag3, e3, e3r]

if e1 >= e2 and e1 >= e3:
    rank1 = row1
    if e2 >= e3:
        rank2 = row2
        rank3 = row3
    elif e3 >= e2:
        rank2 = row3
        rank3 = row2
elif e2 >= e1 and e2 >= e3:
    rank1 = row2
    if e1 >= e3:
        rank2 = row1
        rank3 = row3
    elif e3 >= e1:
        rank2 = row3
        rank3 = row1
elif e3 >= e1 and e3 >= e2:
    rank1 = row3
    if e1 >= e2:
        rank2 = row1
        rank3 = row2
    elif e2 >= e1:
        rank2 = row2
        rank3 = row1

print("--- RANK 1 ---")
print(f"Name: {rank1[0]}")
print(f"Lag: {rank1[1]:.2f} sec")
print(f"Efficiency: {rank1[2]:.2f}")
print(f"Status: {rank1[3]}")
print()
print("--- RANK 2 ---")
print(f"Name: {rank2[0]}")
print(f"Lag: {rank2[1]:.2f} sec")
print(f"Efficiency: {rank2[2]:.2f}")
print(f"Status: {rank2[3]}")
print()
print("--- RANK 3 ---")
print(f"Name: {rank3[0]}")
print(f"Lag: {rank3[1]:.2f} sec")
print(f"Efficiency: {rank3[2]:.2f}")
print(f"Status: {rank3[3]}")