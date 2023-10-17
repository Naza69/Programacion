dick1={"naza":18, "rodri":19}
dick2={"naza":18, "thomi":18}
for i in dick1.items():
    if i in dick2:
        del dick2[i]
dick1.update(dick2)
print(dick1)