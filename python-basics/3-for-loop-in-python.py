name = ['Ayush', 'Rajveer', 'Rudra', 'Kartik']
for x in name:
    print(x)

#break in for loop
print("\nBreak in for loop")
for x in name:
    print(x)
    if x == 'Rudra':
        break

#continuie in for loop
print("\nContinue in for loop")
for x in name:
    if x == 'Rudra':
        continue
    print(x)
