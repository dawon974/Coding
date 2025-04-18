standard = int(input())
speed = int(input())

if speed - standard <= 0:
    print("Congratulations, you are within the speed limit!")
elif speed - standard >=1 and speed - standard <= 20:
    print("You are speeding and your fine is $100.")
elif speed - standard >=21 and speed - standard <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")