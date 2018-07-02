#find the length of string
def length(string):
    num = 0
    for i in string:
        num +=1
    return num
#find the number of times something occur in a string
def count(string,a):
    counter = 0
    for i in string:
        if i == a:
            counter +=1
    return counter
#replace any entery by somwthing else
def replaceStartEnd(string,a,b,index01,index02):
    if index02 > length(string):
        index02 = length(string)-1
    for var in range(index01,index02):
        if string[var] == a:
            string = string[0:var] + b + string[var +1:99999999]
    return string
#find the index of something in a string
def find(string,search):
    num = 0
    didfind = False
    for var in string:
        if var == search[0]:
            if search == string[num:(num+length(search))]:
                didfind = True
                return num
        num +=1
    if didfind == False:
        return -1
    return
#find the index of something in a string from right side
def rfind(string,search):
    num = 0
    didfind = False
    for var in string:
        if var == search[0]:
            if search == string[num:(num+length(search))]:
                index = num
                didfind = True
        num +=1
    if didfind == False:
        return -1
    return index
#find the index of something in a string from a specific position to a specific location

def findStartEnd(string,finding,start,end):
    if end > length(string):
        end = length(string)-1
    for var in range(start,end):
        if string[var] == finding[0]:
            if finding == string[var:(var+length(finding))]:
                return var
    return (-1)
#replace one thing with other
def replace(string,a,b):
    counter = 0
    for var in string:
        if var == a:
            string = string[0:counter] + b + string[counter +1:99999999]
        counter += 1
    return string
#makes all letters upper case
def upperCase(string):
    counter = 0
    lower = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for var in string:
        for i in range (length(lower)):
            if var == lower[i]:
                string = replace(string,string[counter],upper[i])
        counter +=1
    return string
#makes all letters lower
def lowerCase(string):
    counter = 0
    lower = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for var in string:
        for i in range (length(lower)):
            if var == upper[i]:
                string = replace(string,string[counter],lower[i])
        counter +=1
    return string
#switch the case of letters
def switchCase(string):
    counter = 0
    lower = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for var in string:
        for i in range (length(lower)):
            if var == upper[i]:
                string = replace(string,string[counter],lower[i])

            elif var == lower[i]:
                string = replace(string,string[counter],upper[i])
        counter +=1
    return string
#check if whole string is in alphabets
def isAlpha(string):
    counter = 0
    lower = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for var in string:
        for i in lower:
            if var == i:
                counter +=1
        for j in upper:
            if var == j:
                counter +=1
    if counter == length(string):
        return True
    else:
        return False
#check if whole string is in digits
def isdigit(string):
    counter = 0
    numbers = ["0",'1','2','3','4','5','6','7','8','9']
    for var in string:
        for i in numbers:
            if var == i:
                counter +=1
    if counter == length(string):
        return True
    else:
        return False
#reverse entire string
def reverse(string):
    counter = length(string)//2
    for var in range(counter):
        var02 =length(string)-var-1
        temporary = string[var]
        string = replaceStartEnd(string,string[var],string[var02],var,var+1)
        string = replaceStartEnd(string,string[var02],temporary,length(string)-var-1,length(string)-(var))
    return string
#capitalize only the first letter of all the words
def capitalize(string):
    string = upperCase(string[0]) + string[1:999999999]
    for i in range(length(string)):
        if string[i] == " ":
            string = string[0:i+1] + upperCase(string[i+1]) + string[i+2:999999999]
    return string
##check if string ends with something specific
def endwith(string,a,end):
    flag = True
    if end > length(string):
        end = length(string)

    for var in range(length(a)):

        if a[var] == string[end-(length(a)-1-var)]:
            flag = True and flag
        else:
            flag = False
    return flag
#check if the string is in numbers containing a decimal
def isdecimal(string):
    for i in range(length(string)):
        if string[i] == ".":
            return (isdigit(string[0:i]) and isdigit(string[i+1:999999]))
    return False
#reverse each word individually
def indivisualreverse(string):
    newString = ""
    string = " " + string
    flag = True
    index = 0
    while flag == True:
        space = findStartEnd(string," ",index+1,999999)
        if space != -1:
            newString += reverse(string[index:space])
            index = space
        if space == -1:
            flag = False
    newString += reverse(string[index+1:99999])
    return newString
##check if string start with something specific
def startwith(string,a,start):
    if a == string[0:length(a)]:
        return True
    return False
#check if whole string is in lowercase
def islower(string):
    counter = 0
    lower = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for var in string:
        for i in lower:
            if var == i:
                counter +=1
    if counter == length(string):
        return True
    else:
        return False
#check if whole string is in uppercase
def isupper(string):
    counter = 0
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for var in string:
        for j in upper:
            if var == j:
                counter +=1
    if counter == length(string):
        return True
    else:
        return False








