segmentno = eval(input())


s1var1 = segmentno[0][1]
s1val1 = float(segmentno[0][2])
s1var2 = segmentno[0][3]
s1val2 = float(segmentno[0][4])

s2var1 = segmentno[1][1]
s2val1 = float(segmentno[1][2])
s2var2 = segmentno[1][3]
s2val2 = float(segmentno[1][4])

s3var1 = segmentno[2][1]
s3val1 = float(segmentno[2][2])
s3var2 = segmentno[2][3]
s3val2 = float(segmentno[2][4])

if s1var1 == "speed" and s1var2 == "duration":
    s1_speed = s1val1
    s1_dur = s1val2
    s1_dist = float((s1val1 * s1val2))
    print(f"Segment 1: distance = {s1_dist}")
elif s1var1 == "duration" and s1var2 == "speed":
    s1_speed = s1val2
    s1_dur = s1val1
    s1_dist = float((s1val1 * s1val2))
    print(f"Segment 1: distance = {s1_dist}")
elif s1var1 == "distance" and s1var2 == "duration":
    s1_dist = s1val1
    s1_dur = s1val2
    s1_speed = float((s1val1 / s1val2))
    print(f"Segment 1: speed = {s1_speed}")
elif s1var1 == "duration" and s1var2 == "distance":
    s1_dur = s1val1
    s1_dist = s1val2
    s1_speed = float((s1val2 / s1val1))
    print(f"Segment 1: speed = {s1_speed}")
elif s1var1 == "distance" and s1var2 == "speed":
    s1_dist = s1val1
    s1_speed = s1val2
    s1_dur = float((s1val1 / s1val2))
    print(f"Segment 1: duration = {s1_dur}")
elif s1var1 == "speed" and s1var2 == "distance":
    s1_speed = s1val1
    s1_dist = s1val2
    s1_dur = float((s1val2 / s1val1))
    print(f"Segment 1: duration = {s1_dur}")

if s2var1 == "speed" and s2var2 == "duration":
    s2_speed = s2val1
    s2_dur = s2val2
    s2_dist = float((s2val1 * s2val2))
    print(f"Segment 2: distance = {s2_dist}")
elif s2var1 == "duration" and s2var2 == "speed":
    s2_speed = s2val2
    s2_dur = s2val1
    s2_dist = float((s2val1 * s2val2))
    print(f"Segment 2: distance = {s2_dist}")
elif s2var1 == "distance" and s2var2 == "duration":
    s2_dist = s2val1
    s2_dur = s2val2
    s2_speed = float((s2val1 / s2val2))
    print(f"Segment 2: speed = {s2_speed}")
elif s2var1 == "duration" and s2var2 == "distance":
    s2_dur = s2val1
    s2_dist = s2val2
    s2_speed = float((s2val2 / s2val1))
    print(f"Segment 2: speed = {s2_speed}")
elif s2var1 == "distance" and s2var2 == "speed":
    s2_dist = s2val1
    s2_speed = s2val2
    s2_dur = float((s2val1 / s2val2))
    print(f"Segment 2: duration = {s2_dur}")
elif s2var1 == "speed" and s2var2 == "distance":
    s2_speed = s2val1
    s2_dist = s2val2
    s2_dur = float((s2val2 / s2val1))
    print(f"Segment 2: duration = {s2_dur}")

if s3var1 == "speed" and s3var2 == "duration":
    s3_speed = s3val1
    s3_dur = s3val2
    s3_dist = float((s3val1 * s3val2))
    print(f"Segment 3: distance = {s3_dist}")
elif s3var1 == "duration" and s3var2 == "speed":
    s3_speed = s3val2
    s3_dur = s3val1
    s3_dist = float((s3val1 * s3val2))
    print(f"Segment 3: distance = {s3_dist}")
elif s3var1 == "distance" and s3var2 == "duration":
    s3_dist = s3val1
    s3_dur = s3val2
    s3_speed = float((s3val1 / s3val2))
    print(f"Segment 3: speed = {s3_speed}")
elif s3var1 == "duration" and s3var2 == "distance":
    s3_dur = s3val1
    s3_dist = s3val2
    s3_speed = float((s3val2 / s3val1))
    print(f"Segment 3: speed = {s3_speed}")
elif s3var1 == "distance" and s3var2 == "speed":
    s3_dist = s3val1
    s3_speed = s3val2
    s3_dur = float((s3val1 / s3val2))
    print(f"Segment 3: duration = {s3_dur}")
elif s3var1 == "speed" and s3var2 == "distance":
    s3_speed = s3val1
    s3_dist = s3val2
    s3_dur = float((s3val2 / s3val1))
    print(f"Segment 3: duration = {s3_dur}")
print()
to_dist = (s1_dist + s2_dist + s3_dist)
print(f"Total Distance: {to_dist}")
to_dur = (s1_dur + s2_dur + s3_dur)
print(f"Total Duration: {to_dur}")
vav = (to_dist / to_dur)
print(f"Average Speed: {vav:.2f}")

if s1_speed > s2_speed > s3_speed or s1_speed > s3_speed > s2_speed:
    print("Maximum Speed Segment: Segment 1")
elif s2_speed > s3_speed > s1_speed or s2_speed > s1_speed > s3_speed:
    print("Maximum Speed Segment: Segment 2")
elif s3_speed > s1_speed > s2_speed or s3_speed > s2_speed > s1_speed:
    print("Maximum Speed Segment: Segment 3") 

if s1_speed < s2_speed < s3_speed or s1_speed < s3_speed < s2_speed:
    print("Minimum Speed Segment: Segment 1")
elif s2_speed < s3_speed < s1_speed or s2_speed < s1_speed < s3_speed:
    print("Minimum Speed Segment: Segment 2")
elif s3_speed < s1_speed < s2_speed or s3_speed < s2_speed < s1_speed:
    print("Minimum Speed Segment: Segment 3")