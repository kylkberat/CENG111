"""
1) Take input of three nested list.
   # segments = [
   # ["Segment 1", "speed", "m/minute", 6.0, "duration", "minute", 30],
   # ["Segment 2", "duration", "hour", 10.0, "speed", "km/hour", 5.0],
   # ["Segment 3", "distance", "m", 5.5, "duration", "hour", 4.0]
   # ]
2) Take input of minimum speed.
   # 3.5
3)

"""

segments = eval(input())
min_speed = eval(input())

id1, var11, unit11, val11, var12, unit12, val12 = segments[0]
id2, var21, unit21, val21, var22, unit22, val22 = segments[1]
id3, var31, unit31, val31, var32, unit32, val32 = segments[2]

succ_seg = 0
succ_dist = 0
succ_dur = 0
succ_avg_speed = 0

unsucc_seg = 0
unsucc_dist = 0
unsucc_dur = 0
unsucc_avg_speed = 0

if unit11 == "m":
    val11_cvd = val11 / 1000
elif unit11 == "km":
    val11_cvd = val11
elif unit11 == "minute":
    val11_cvd = val11 / 60
elif unit11 == "hour":
    val11_cvd = val11
elif unit11 == "m/minute":
    val11_cvd = val11 * (60/1000)
elif unit11 == "km/hour":
    val11_cvd = val11

if unit12 == "m":
    val12_cvd = val12 / 1000
elif unit12 == "km":
    val12_cvd = val12
elif unit12 == "minute":
    val12_cvd = val12 / 60
elif unit12 == "hour":
    val12_cvd = val12
elif unit12 == "m/minute":
    val12_cvd = val12 * (60/1000)
elif unit12 == "km/hour":
    val12_cvd = val12

if unit21 == "m":
    val21_cvd = val21 / 1000
elif unit21 == "km":
    val21_cvd = val21
elif unit21 == "minute":
    val21_cvd = val21 / 60
elif unit21 == "hour":
    val21_cvd = val21
elif unit21 == "m/minute":
    val21_cvd = val21 * (60/1000)
elif unit21 == "km/hour":
    val21_cvd = val21

if unit22 == "m":
    val22_cvd = val22 / 1000
elif unit22 == "km":
    val22_cvd = val22
elif unit22 == "minute":
    val22_cvd = val22 / 60
elif unit22 == "hour":
    val22_cvd = val22
elif unit22 == "m/minute":
    val22_cvd = val22 * (60/1000)
elif unit22 == "km/hour":
    val22_cvd = val22

if unit31 == "m":
    val31_cvd = val31 / 1000
elif unit31 == "km":
    val31_cvd = val31
elif unit31 == "minute":
    val31_cvd = val31 / 60
elif unit31 == "hour":
    val31_cvd = val31
elif unit31 == "m/minute":
    val31_cvd = val31 * (60/1000)
elif unit31 == "km/hour":
    val31_cvd = val31

if unit32 == "m":
    val32_cvd = val32 / 1000
elif unit32 == "km":
    val32_cvd = val32
elif unit32 == "minute":
    val32_cvd = val32 / 60
elif unit32 == "hour":
    val32_cvd = val32
elif unit32 == "m/minute":
    val32_cvd = val32 * (60/1000)
elif unit32 == "km/hour":
    val32_cvd = val32




if var11 == "speed" and var12 == "duration":
    speed1 = val11_cvd
    duration1 = val12_cvd
    distance1 = val11_cvd * val12_cvd
    miss = distance1
    if speed1 >= min_speed:
        print(f"Segment 1: distance {miss:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss:.2f} km, Unsuccessful")
elif var11 == "duration" and var12 == "speed":
    speed1 = val12_cvd
    duration1 = val11_cvd
    distance1 = val11_cvd * val12_cvd
    miss = distance1
    if speed1 >= min_speed:
        print(f"Segment 1: distance {miss:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss:.2f} km, Unsuccessful")
elif var11 == "distance" and var12 == "duration":
    distance1 = val11_cvd
    duration1 = val12_cvd
    speed1 = val11_cvd / val12_cvd
    miss = speed1
    if speed1 >= min_speed:
        print(f"Segment 1: speed {miss:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss:.2f} km/hour, Unsuccessful")
elif var11 == "duration" and var12 == "distance":
    distance1 = val12_cvd
    duration1 = val11_cvd
    speed1 = val12_cvd / val11_cvd
    miss = speed1
    if speed1 >= min_speed:
        print(f"Segment 1: speed {miss:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss:.2f} km/hour, Unsuccessful")
elif var11 == "speed" and var12 == "distance":
    distance1 = val12_cvd
    speed1 = val11_cvd
    duration1 = val12_cvd / val11_cvd
    miss = duration1
    if speed1 >= min_speed:
        print(f"Segment 1: duration {miss:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss:.2f} hour, Unsuccessful")
elif var11 == "distance" and var12 == "speed":
    distance1 = val11_cvd
    speed1 = val12_cvd
    duration1 = val11_cvd / val12_cvd
    miss = duration1
    if speed1 >= min_speed:
        print(f"Segment 1: duration {miss:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss:.2f} hour, Unsuccessful")



if var21 == "speed" and var22 == "duration":
    speed2 = val21_cvd
    duration2 = val22_cvd
    distance2 = val21_cvd * val22_cvd
    miss2 = distance2
    if speed2 >= min_speed:
        print(f"Segment 1: distance {miss2:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss2:.2f} km, Unsuccessful")
elif var21 == "duration" and var22 == "speed":
    speed2 = val22_cvd
    duration2 = val21_cvd
    distance2 = val21_cvd * val22_cvd
    miss2 = distance2
    if speed2 >= min_speed:
        print(f"Segment 1: distance {miss2:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss2:.2f} km, Unsuccessful")
elif var21 == "distance" and var22 == "duration":
    distance2 = val21_cvd
    duration2 = val22_cvd
    speed2 = val21_cvd / val22_cvd
    miss2 = speed2
    if speed2 >= min_speed:
        print(f"Segment 1: speed {miss2:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss2:.2f} km/hour, Unsuccessful")
elif var21 == "duration" and var22 == "distance":
    distance2 = val22_cvd
    duration2 = val21_cvd
    speed2 = val22_cvd / val21_cvd
    miss2 = speed2
    if speed2 >= min_speed:
        print(f"Segment 1: speed {miss2:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss2:.2f} km/hour, Unsuccessful")
elif var21 == "speed" and var22 == "distance":
    distance2 = val22_cvd
    speed2 = val21_cvd
    duration2 = val22_cvd / val21_cvd
    miss2 = duration2
    if speed2 >= min_speed:
        print(f"Segment 1: duration {miss2:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss2:.2f} hour, Unsuccessful")
elif var21 == "distance" and var22 == "speed":
    distance2 = val21_cvd
    speed2 = val22_cvd
    duration2 = val21_cvd / val22_cvd
    miss2 = duration2
    if speed2 >= min_speed:
        print(f"Segment 1: duration {miss2:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss2:.2f} hour, Unsuccessful")



if var31 == "speed" and var32 == "duration":
    speed3 = val31_cvd
    duration3 = val32_cvd
    distance3 = val31_cvd * val32_cvd
    miss3 = distance3
    if speed3 >= min_speed:
        print(f"Segment 1: distance {miss3:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss3:.2f} km, Unsuccessful")
elif var31 == "duration" and var32 == "speed":
    speed3 = val32_cvd
    duration3 = val31_cvd
    distance3 = val31_cvd * val32_cvd
    miss3 = distance3
    if speed3 >= min_speed:
        print(f"Segment 1: distance {miss3:.2f} km, Successful")
    else:
        print(f"Segment 1: distance {miss3:.2f} km, Unsuccessful")
elif var31 == "distance" and var32 == "duration":
    distance3 = val31_cvd
    duration3 = val32_cvd
    speed3 = val31_cvd / val32_cvd
    miss3 = speed3
    if speed3 >= min_speed:
        print(f"Segment 1: speed {miss3:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss3:.2f} km/hour, Unsuccessful")
elif var31 == "duration" and var32 == "distance":
    distance3 = val32_cvd
    duration3 = val31_cvd
    speed3 = val32_cvd / val31_cvd
    miss3 = speed3
    if speed3 >= min_speed:
        print(f"Segment 1: speed {miss3:.2f} km/hour, Successful")
    else:
        print(f"Segment 1: speed {miss3:.2f} km/hour, Unsuccessful")
elif var31 == "speed" and var32 == "distance":
    distance3 = val32_cvd
    speed3 = val31_cvd
    duration3 = val32_cvd / val31_cvd
    miss3 = duration3
    if speed3 >= min_speed:
        print(f"Segment 1: duration {miss3:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss3:.2f} hour, Unsuccessful")
elif var31 == "distance" and var32 == "speed":
    distance3 = val31_cvd
    speed3 = val32_cvd
    duration3 = val31_cvd / val32_cvd
    miss3 = duration3
    if speed3 >= min_speed:
        print(f"Segment 1: duration {miss3:.2f} hour, Successful")
    else:
        print(f"Segment 1: duration {miss3:.2f} hour, Unsuccessful")



if speed1 >= min_speed:
    succ_seg += 1
    succ_dist += distance1
    succ_dur += duration1
else:
    unsucc_seg += 1
    unsucc_dist += distance1
    unsucc_dur += duration1

if speed2 >= min_speed:
    succ_seg += 1
    succ_dist += distance2
    succ_dur += duration2
else:
    unsucc_seg += 1
    unsucc_dist += distance2
    unsucc_dur += duration2

if speed3 >= min_speed:
    succ_seg += 1
    succ_dist += distance3
    succ_dur += duration3
else:
    unsucc_seg += 1
    unsucc_dist += distance3
    unsucc_dur += duration3

print()
print(f"Number of Successful Segments: {succ_seg}")
print(f"Number of Unsuccessful Segments: {unsucc_seg}")
print()
print(f"Total Distance (Successful): {succ_dist:.1f} km")
print(f"Total Distance (Unsuccessful): {unsucc_dist:.1f} km")

if succ_seg > 0:
    succ_avg_speed = succ_dist / succ_dur
    print(f"Average Speed (Successful): {succ_avg_speed:.1f} km/hour")
else:
    print("There is not a single successful segment!")

if unsucc_seg > 0:
    unsucc_avg_speed = unsucc_dist / unsucc_dur
    print(f"Average Speed (Unsuccessful): {unsucc_avg_speed:.1f} km/hour")
else:
    print("CONGRATULATIONS, All three segments are successful!")