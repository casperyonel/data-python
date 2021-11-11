from matplotlib import pyplot as plt

open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     line.strip
#     type = line.split(',')
#     print(type[2])

real_total = 0

chocolate_x_values = []
strawberry_x_values = []
vanilla_x_values = []

for line in open_file:
    line.strip
    type = line.split(',')
    if type[-3] == "Chocolate":
        choc_total = float(type[-2]) * float(type[-1])
        chocolate_x_values.append(int(choc_total))
    elif type[-3] == "Strawberry":
        strawberry_total = float(type[-2]) * float(type[-1])
        strawberry_x_values.append(int(strawberry_total))
    elif type[-3] == "Vanilla":
        vanilla_total = float(type[-2]) * float(type[-1])
        vanilla_x_values.append(int(vanilla_total))

print(chocolate_x_values)
print(strawberry_x_values)
print(vanilla_x_values)

y_values = [15, 20, 30, 40, 50, 60, 70, 80, 90]
    
plt.plot(y_values, chocolate_x_values, color="navy")
# plt.plot(y_values, strawberry_x_values, color="navy")
# plt.plot(y_values, vanilla_x_values, color="navy")
plt.title("Comparing the various flavors")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()




    # total = 0
    # total = (float(type[-2]) * float(type[-1]))
    # real_total += total