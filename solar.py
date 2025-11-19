"""
1) Take an input of "targeted output threshold". (minimum power for farm)
2) Take another input of nested list containing data for three section.
3) Convert all of the unit data to the variables.
4) Inspect the base efficiency acc. to angle.
    # abs() is forbidden. You should define yourself with if statements.
5) Inspect the temperature penalties according to given temperatures with if statements.
6) Calculate the final output and assign it to a variable.
7) Compare the final output with the targeted output.
8) Print the statements sequently.

"""

target = float(input("What is the minimum power for farm? "))
nelist = eval(input("Enter the environmental factors sequently: "))

secname1 = nelist[0][0]
angle1 = nelist[0][1]
temp1 = nelist[0][2]
dust1 = nelist[0][3]

secname2 = nelist[1][0]
angle2 = nelist[1][1]
temp2 = nelist[1][2]
dust2 = nelist[1][3]

secname3 = nelist[2][0]
angle3 = nelist[2][1]
temp3 = nelist[2][2]
dust3 = nelist[2][3]

ebase1 = 100 - (angle1 - 90) if angle1 >= 90 else 100 - (90 - angle1)
ebase2 = 100 - (angle2 - 90) if angle2 >= 90 else 100 - (90 - angle2)
ebase3 = 100 - (angle3 - 90) if angle3 >= 90 else 100 - (90 - angle3)

ptemp1 = (temp1 - 25) * 0.5 if temp1 > 25 else 0
ptemp2 = (temp2 - 25) * 0.5 if temp2 > 25 else 0
ptemp3 = (temp3 - 25) * 0.5 if temp3 > 25 else 0

finalo1 = (ebase1 - ptemp1) * (1.0 - dust1) * 0.2
print(f"{secname1} Output: {finalo1:.2f} kW")
finalo2 = (ebase2 - ptemp2) * (1.0 - dust2) * 0.2
print(f"{secname2} Output: {finalo2:.2f} kW")
finalo3 = (ebase3 - ptemp3) * (1.0 - dust3) * 0.2
print(f"{secname3} Output: {finalo3:.2f} kW")
print()
totalo = finalo1 + finalo2 + finalo3
print(f"Total Output: {totalo:.2f} kW")

if totalo >= target:
    print("Status: Operational")
else:
    print("Status: Low Power")

if finalo1 <= finalo2 <= finalo3 or finalo1 <= finalo3 <= finalo2:
    print(f"Least Efficient: {secname1}")
elif finalo2 <= finalo1 <= finalo3 or finalo2 <= finalo3 <= finalo1:
    print(f"Least Efficient: {secname2}")
elif finalo3 <= finalo1 <= finalo2 or finalo3 <= finalo2 <= finalo1:
    print(f"Least Efficient: {secname3}")