
pigs = int(input("Enter three digits (each digit for one pig):"))


sum = int((pigs%10) + ((pigs/10))%10 + pigs/100)
print(sum)

pigsDivide = sum//3;
print(pigsDivide)

whatsLeft = sum-(pigsDivide*3)
print(whatsLeft)

isDividable = not(whatsLeft)
print(isDividable)
