#While Loop
#Washing Loop
Dirty = True
sum = 0
while Dirty == True:
    wash = input("Do you wish to continue the washing? (yes / no ): ").lower()
    sum += 1
    if wash == "yes":
        print("Washing Continues...")
        continue
    else:
        print("Washing Stops...")
        break
print("Number of cycle is", sum)