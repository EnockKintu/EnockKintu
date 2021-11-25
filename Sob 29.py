#The asterix pattern of half a diamond
for row in range(9):
    for col in range(5):
        if col-row==0 or row+col==8:
            print("*", end="")
        else:
            print(end=" ")
    print()
          
