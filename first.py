#print("\n\t\tOOAD project\n")

dict = {1: "Electronics", 2: "Stationary", 3:"Games"}

print("\tHello!!\n\t\tWe provide the below categories to shop for...\n")

for i in dict:
    print(i, "-",dict[i])

n = int(input("\n\tEnter your choice (Enter 0 to quit): "))

if n==1:
    import electron
elif n==2:
    import stationary
elif n==3:
    import games
else:
    print("\nCome back soon! exiting....\n")