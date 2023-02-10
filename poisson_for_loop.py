import math
 
def f(x, lam):
    return (math.exp(-lam) * lam**x)/(math.factorial(x))

lam=float(input("Enter the mean:"))
#p=int(input("Enter the poisson variate:"))

sol=0
for i in range(5):
  poisson=f(i,lam)
  sol+=poisson

#printing probability of x<=4
print("The poisson distribution is:",sol)

print("when demand is refused poisson distribution is:",1-sol)