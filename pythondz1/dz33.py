months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
a = months_a.union(months_b)
a.add("Dec")
for i in a:
    print(i)
x = {1, 2, 3}
y = {4, 3, 6}

print(x.intersection(y))
