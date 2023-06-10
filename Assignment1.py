def Name_Surname(L1, L2):
    for i in range(0, len(L1)):
        List3 = L1[i] + " " + L2[i]
        print(List3)


List1 = input("Enter the First names")
L1 = List1.split()

List2 = input("Enter the last Names")
L2 = List2.split()

Name_Surname(L1, L2)