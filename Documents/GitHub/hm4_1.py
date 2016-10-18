import package4

x = int(raw_input("Input any nubmer from 1 to 9: "))
if x > 0 and x < 4:
    s = raw_input("Input string: ")
    n = int(raw_input("Input repeats: "))
    package4.if1(s, n)
elif x > 3 and x < 7:
    m = int(raw_input("Input number of degree: "))
    package4.if2(x, m)
elif x > 6 and x < 10:
    package4.if3(x)
else:
    print "ERROR!"
