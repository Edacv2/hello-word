while True:
    """This will create a mutiplication table starting with the given number + 10
        until user enter stop"""
    print("\nMultiplication Table\n")
    num_r = input("Enter number or type \"stop\" to quit: ")
    if num_r == "stop":
        break
    else:
        print()
        for num1 in range (int(num_r), int(num_r) + 10):
            print("num =", num1, ":", end = " ")            
            for num2 in range(1, 10+1):
                print("{:2d}".format(num1 * num2), end = " ")                
            print()