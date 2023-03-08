

print("The program has Started")
ascii = int(input("Please Enter an ASCII code: "))
charecter = chr(ascii)

if ascii >= 32 and ascii <= 126:
    print(f"The character represented by the ASCII code {ascii} is:  {charecter}.")

else:
    print("Please Enter Between 32 - 126")

print("Program has Ended")