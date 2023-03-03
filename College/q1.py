def reverse(num):
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    print("Reverse of the number:", rev)
def reverseStr(str1):
    str2 = ""
    for i in str1:
        str2 = i + str2
    print("Reverse of the string:", str2)
    if str2 == str1:
        print("Palindrome")
    else:
        print("Not a Palindrome")

while True:
    print("1. Reverse a number ")
    print("2. Reverse a string ")
    print("3. Exit ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the number : "))
        reverse(num)
    elif choice == 2:
        str1 = input("Enter the string : ")
        reverseStr(str1)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
