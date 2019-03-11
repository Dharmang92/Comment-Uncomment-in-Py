filename = input("Enter file name to be Commented : ")
t = filename
filename = "/home/dharmang/Documents/" + filename

if filename.split('.')[1] == ("sh" or "py"):
    csyntax = '#'
elif filename.split('.')[1] == "cpp":
    csyntax = '//'
else:
    print("Sorry the program is not supported for other comment syntaxes!")

with open(filename, 'r') as fr:
    line = fr.readlines()

with open(filename, 'w') as fw:
    n = len(line)
    for i in range(0,n):
        temp = csyntax + line[i]
        fw.writelines(temp)
        fw.write("")
        
print("The filename : " + t + " has been Commented!")
#Thank you for using the program! :D  (Dharmang)
