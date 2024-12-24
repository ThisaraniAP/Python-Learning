import datetime

print("\n\n")

a = datetime.datetime.now()

print(a,"\n")
print(a.year, "\n")
print(a.strftime("%A"), "\n")

b = datetime.datetime(2023, 4, 4)
print(b, "\n")

c = datetime.datetime(2023, 4, 4, 23, 23, 23)
print(c, "\n")
