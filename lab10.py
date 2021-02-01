def neg():
  try:
    n=int(input("Enter an integer :"))
    if n<0:
        print("Found negative")
  except ValueError as ve:
        print("Inner Block :",ve)
        raise IOError ("Keyboard Error") from ValueError
try:
    neg()
except ValueError as ve:
    print("Outer block :",ve)
except IOError as ie:
    print("Outer block : Chained Error caught ",ie)