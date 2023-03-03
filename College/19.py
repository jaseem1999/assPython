#. Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.1.Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character
list_num = input("Enter a list of integers: ")
list_num = list_num.split()
list_num = [int(x) for x in list_num]
list_num = ['over' if x > 100 else x for x in list_num]
print("All list ",list_num)