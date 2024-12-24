tot_a = 0
tot_b = 0
tot_c = 0
tot_s = 0
tot_f = 0
count = 1

while count <= 5:
    m1 = int(input("Enter marks 1: "))
    m2 = int(input("Enter marks 2: "))
    m3 = int(input("Enter marks 3: "))

    avg = (m1 +m2 + m3)/3

    if avg >= 80:
        gr = "A"
        tot_a = tot_a + 1
    elif avg >= 70:
        gr = "B"
        tot_b = tot_b + 1
    elif avg >=60:
        gr = "C"
        tot_c = tot_c + 1
    elif avg >= 50:
        gr = "S"
        tot_s = tot_s + 1
    else:
        gr = "F"
        tot_f = tot_f + 1

    print ("Average: ", avg)
    print ("Grade: ", gr)
    count += 1

print ("Total A: ", tot_a)
print ("Total B: ", tot_b)
print ("Total C: ", tot_c)
print ("Total S: ", tot_s)
print ("Total F: ", tot_f)
