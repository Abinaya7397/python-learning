#bus ticket booking
booking=int(input("enter a amount"))
if booking>=750:
    print("i got a sleeper bed")
elif booking >= 350:
    print("i got a normal sheet")
else:
    print("standing travel")
