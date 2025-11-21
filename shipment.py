"""
1) Take an input as a nested list. ["ID", Weight, Distance, "Urgency"]
2) Calculate the shipping cost acc. to the given operations.
    # Light / Heavy - Distance if
3) Multiply the cost by 1.5 regarding to urgency.
4) Calculate the risk score acc. to the given ops.
5) Add 20 points if urgency is high.
6) Calculate the Total Cost.

7) Print cost of each shipment (formatted to 2 decimal)
8) Print Total Cost.
9) Determine the highest risk score shipment and print its ID.
10) Check the budget with respect to 1000.

"""
shipment = eval(input())

id1 = shipment[0][0]
weight1 = shipment[0][1]
distance1 = shipment[0][2]
urgency1 = shipment[0][3]

id2 = shipment[1][0]
weight2 = shipment[1][1]
distance2 = shipment[1][2]
urgency2 = shipment[1][3]

id3 = shipment[2][0]
weight3 = shipment[2][1]
distance3 = shipment[2][2]
urgency3 = shipment[2][3]

risk1 = (weight1 * distance1) / 100
risk2 = (weight2 * distance2) / 100
risk3 = (weight3 * distance3) / 100


if weight1 <= 50:
    cost1 = 10.0 + (distance1 * 0.2)
elif weight1 > 50:
    if distance1 > 500:
        cost1 = 50.0 + (distance1 * 0.5) + (weight1 * 1.5)
    elif distance1 <= 500:
        cost1 = 25.0 + (distance1 * 0.4) + (weight1 * 1.0)

if urgency1 == "High":
    cost1 = (1.5 * cost1)
    risk1 = risk1 + 20
elif urgency1 == "Standard":
    cost1 = cost1
else:
    print("Enter a valid urgency!")


if weight2 <= 50:
    cost2 = 10.0 + (distance2 * 0.2)
elif weight2 > 50:
    if distance2 > 500:
        cost2 = 50.0 + (distance2 * 0.5) + (weight2 * 1.5)
    elif distance2 <= 500:
        cost2 = 25.0 + (distance2 * 0.4) + (weight2 * 1.0)

if urgency2 == "High":
    cost2 = (1.5 * cost2)
    risk2 = risk2 + 20
elif urgency2 == "Standard":
    cost2 = cost2
else:
    print("Enter a valid urgency!")


if weight3 <= 50:
    cost3 = 10.0 + (distance3 * 0.2)
elif weight3 > 50:
    if distance3 > 500:
        cost3 = 50.0 + (distance3 * 0.5) + (weight3 * 1.5)
    elif distance3 <= 500:
        cost3 = 25.0 + (distance3 * 0.4) + (weight3 * 1.0)

if urgency3 == "High":
    cost3 = (1.5 * cost3)
    risk3 = risk3 + 20
elif urgency3 == "Standard":
    cost3 = cost3
else:
    print("Enter a valid urgency!")


totalcost = cost1 + cost2 + cost3

if risk1 >= risk2 >= risk3 or risk1 >= risk3 >= risk2:
    most_risky = id1
elif risk2 >= risk1 >= risk3 or risk2 >= risk3 >= risk1:
    most_risky = id2
elif risk3 >= risk2 >= risk1 or risk3 >= risk1 >= risk2:
    most_risky = id3



print(f"{id1} Cost: {cost1:.2f} USD")
print(f"{id2} Cost: {cost2:.2f} USD")
print(f"{id3} Cost: {cost3:.2f} USD")
print("-------------------")
print(f"Total Cost: {totalcost:.2f} USD")
print(f"Most Risky: {most_risky}")
print("Budget: Exceeded") if totalcost > 1000 else print("Budget: Approved")