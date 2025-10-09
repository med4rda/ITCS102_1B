for a in range(1,7,1):
    for c in range(6,a,-1):
        print(" ", end=" ")
    for b in range(a,0,-1):
        print(b,end=" ")
    for cb in range(2,a+1,1):
        print(cb,end=" ")
    print()