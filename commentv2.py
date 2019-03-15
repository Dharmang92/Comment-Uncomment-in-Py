#Useful in sh or py (Shell files or python files) or any other language having Single line comment

filename = input("Enter file name to be Commented : ")
t = filename
filename = "/home/dharmang/Documents/" + filename

with open(filename, 'r') as fr:
    line = fr.readlines()

if filename.split('.')[1] == ("sh" or "py"):
    csyntax = '#'
elif filename.split('.')[1] == "cpp":
    csyntax = '//'
else:
    print("Sorry the program is not supported for other comment syntaxes!")

with open(filename, 'w') as fw:
    n = len(line)
    choice = input("Custom Comment Area? >")
    if choice == 'y':
        startl = int(input("Enter starting line >"))
        endl = int(input("Enter ending line >"))
        startl -= 1
        
        for i in range(0,startl):
            temp = line[i]
            fw.writelines(temp)
            fw.write("")
        for i in range(startl,endl):
            temp = csyntax + line[i]
            fw.writelines(temp)
            fw.write("")
        for i in range(endl,n):
            temp = line[i]
            fw.writelines(temp)
            fw.write("")
            
    elif choice == 'n':
        for i in range(0,n):
            temp = csyntax + line[i]
            fw.writelines(temp)
            fw.write("")
        
print("The filename : " + t + " has been Commented!")
#Thank you for using the program! :D  (Dharmang)
