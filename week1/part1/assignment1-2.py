

print(50+50)
print(100-10)

#the following code will throw an 'invalid syntax' error if ran
#print(30+*6)
    
print(6^6)
print(6**6)
print(6+6+6+6+6+6)
    
print("Hello World")

print("Hello World : 10")



##################################################################
# morgage calculator
def calc_morgage(P: int, R: int, L:int) -> int:
    monthly_rate = R / 1200
    x = (1 + monthly_rate) ** L
    return P * ( monthly_rate * x ) / ( x - 1 ) 

print("input data:")

P, R, L = tuple(int(n) for n in input().split())

print()
print(f"{calc_morgage(P, R, L):.0f}")