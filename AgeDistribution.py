import csv
import matplotlib.pyplot as plt
import numpy as np
vips = []

with open("customers.csv") as user:

    man = csv.DictReader(user)
    for row in man:
        if row["Age"] and row["City"] == "Karaj":
          vips.append(int(row["Age"][:2]))

count = {}

for n in vips:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

y = list(count.values())
x = list(count.keys())

plt.bar(x, y)

plt.title("Customer Age Distribution in Karaj City", fontsize =12, fontweight='bold')
plt.xlabel("Customer Age (years)", fontsize=12, fontweight='bold')
plt.ylabel("Number of Customers", fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()
