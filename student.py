def main():
    #your code goes here
    number=float(input('Enter A Number: '))
    if number/5%3==0:
      print("fizzbuzz")
    elif number%5==0:
      print("buzz")
    elif number%3==0:
      print("fizz")
    else:
      print(number)

if __name__ =='__main__':
    main()
