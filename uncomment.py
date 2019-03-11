filename = input("Enter file to be Uncommented : ")
t = filename
filename = "/home/dharmang/Documents/" + filename

if filename.split('.')[1] == ("sh" or "py"):
    csyntax = '#'
elif filename.split('.')[1] == "cpp":
    csyntax = "//"
else:
    print("Sorry the program is not supported for other comment syntaxes!")

with open(filename, 'r') as fr:
    line = fr.readlines()
    n = len(line)
    
with open(filename, 'w') as fw:
    for i in range(0,n):
        if csyntax == "//":                                  #for cpp files
            if line[i][0:2] == csyntax:
                temp = fw.writelines(line[i].split(csyntax)[1])
            else:
                temp = fw.writelines(line[i])
            fw.write("")
        else:                                                #for sh and py files
            if line[i][0] == csyntax:
                temp = fw.writelines(line[i].split(csyntax)[1])
            else:
                temp = fw.writelines(line[i])
            fw.write("")

print("The filename : " + t + " has been Uncommented!")
#Thank you for using the program! :D  (Dharmang)
