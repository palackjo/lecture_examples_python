# switch.stlx translation

try:
    i  = input("Zahl eingeben: ")
    i  = int(i)
    n  = i % 10
    msg = "letzte Ziffer ist %s"
    if n in (1,2,3,4,5,6,7,8,9,0):
        print(msg % n)
    else:
        print("impossible")
except:
    print("Sie haben versagt")
