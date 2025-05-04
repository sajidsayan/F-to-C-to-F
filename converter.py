print("F to C converter C to F converter")
print("1. F to C")
print("2. C to F")
choice = input("Enter your choice: ")
if choice == "1":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius: ", c)
elif choice == "2":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit: ", f)
