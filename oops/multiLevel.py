class A: #base
    varA="welcome to A"
class B: #base
    varB="welcome to B"
class C(A,B): #derived
    varC="welcome to C"
c1=C()
print(c1.varA)