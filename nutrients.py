"""
1) input Mass and time as M and T respectively. #eval()
2) input req.s as a list.
3) input actual intake as a list.
4) extract the required list ingredients to the variables.
5) extract the actual intake list ing.s to the variables.
6) check whether T > 120 or not to determine if protein is needed

Carbohydrates = (req[0])x(M x T/60)
...
Actual Nut...

Deficincies:
if
    if req(carb) - intake(carb) > 0:
        print("carb: Req(carb)-Intake(carb) g")

    if

"""
mass = eval(input())
time = eval(input())
req = eval(input())
actual = eval(input())

carbreq = (req[0] * mass * (time / 60))
elecreq = (req[1] * carbreq)
waterreq = (req[2] * mass * (time / 60))
if time > 120:
    protreq = (req[3] * mass * (time / 60))
else:
    protreq = eval(0.00)

carbact = actual[0]
elecact = actual[1]
wateract = actual[2]
protact = actual[3]

carbdef = carbreq - carbact
elecdef = elecreq - elecact
waterdef = waterreq - wateract
protdef = protreq - protact

print("Total Required Nutrients:")
print(f"Carbohydrates: {carbreq:.2f} g")
print(f"Electrolytes: {elecreq:.2f} ml")
print(f"Water: {waterreq:.2f} ml")
print(f"Protein: {protreq:.2f} g")
print()
print(f"Actual Nutrients:")
print(f"Carbohydrates: {carbact:.2f} g")
print(f"Electrolytes: {elecact:.2f} ml")
print(f"Water: {wateract:.2f} ml")
print(f"Protein: {protact:.2f} g")
print()

if carbdef <= 0 and elecdef <= 0 and \
    waterdef <= 0 and protdef <= 0:
    print("Deficiencies:")
    print("None")
else:
    print("Deficiencies:")
    if carbdef > 0:
        print(f"Carbohydrates deficient by {carbdef:.2f} g")
    if elecdef > 0:
        print(f"Electrolytes deficient by {elecdef:.2f} ml")
    if waterdef > 0:
        print(f"Water deficient by {waterdef:.2f} ml")
    if protdef > 0:
        print(f"Protein deficient by {protdef:.2f} g")