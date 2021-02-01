try:
    a=int(input("Enter the number :"))
    if a<90 or a>120:
        raise ValueError("Abnormal Condition")
    print(a," is a valid number")
except Exception as e:
    print(e)