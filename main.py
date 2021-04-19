import stdiomask

print("\n\t\tOOAD project\n")

print("\tEnter Login credentials to shop!")

u = input("\n\tUsername: ")
p = stdiomask.getpass(prompt='\n\tPassword: ', mask='•')

if u=='pesu' and p=='pesu':
    print('\nWelcome', u, '!!\n')
    import first
else:
    print('\nWrong credentials... \ntry again')
    import main

print("\n")