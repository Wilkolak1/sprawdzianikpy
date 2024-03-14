with open("napisy.txt", "r") as nazwa:
    napisy = nazwa.readline()
    dane = open("wynik.txt", "w")

    # a
    if(len(napisy) %2==0):
        dane.write("a: " + napisy)
    # b

    # d
    elif(napisy.endswith(1)):
        dane.write("d: " + napisy)