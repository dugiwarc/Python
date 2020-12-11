a = input('Please enter the first number, "a":\n')
b = input('Please enter the second number, "b":\n')
if a < b:
    a,b = b,a

r1,r2 = a,b
s1,s2 = 1,0
t1,t2 = 0,1
while r2 > 0:
    q,r = divmod(r1,r2)
    r1,r2 = r2,r
    s1,s2 = s2,s1 - q * s2
    t1,t2 = t2,t1 - q * t2

print r1,s1,t1