
Seq = int(input("Enter number of terms: "))

num1 = 0
num2 = 1
count = 0

print("Fibonacci Seq:")
while count < Seq:
    print(num1)
    temp = num1 + num2
    num1 = num2

    num2 = temp
    count += 1

