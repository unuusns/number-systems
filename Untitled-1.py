while True:
    
       number_system =input("Enter the number system: [1]Decimal, [2]Binary [3]Octal [4]Hexadecimal: \n")  
if number_system == "1":
        decimal_number = int(input("Enter the decimal number: "))
        print("Binary: ", bin(decimal_number))
        print("Octal: ", oct(decimal_number))
        print("Hexadecimal: ", hex(decimal_number))
elif number_system == "2":
        binary_number = input("Enter the binary number: ")
        print("Decimal: ", int(binary_number, 2))
        print("Octal: ", oct(int(binary_number, 2)))
        print("Hexadecimal: ", hex(int(binary_number, 2)))
elif number_system == "3":
        octal_number = input("Enter the octal number: ")
        print("Decimal: ", int(octal_number, 8))
        print("Binary: ", bin(int(octal_number, 8)))
        print("Hexadecimal: ", hex(int(octal_number, 8)))
elif number_system == "4":
        hexadecimal_number = input("Enter the hexadecimal number: ")
        print("Decimal: ", int(hexadecimal_number, 16))
        print("Binary: ", bin(int(hexadecimal_number, 16)))
        print("Octal: ", oct(int(hexadecimal_number, 16)))
else:
       print("invalid task")





    
    
    
    
    
        
            
    
    
    
    
    



