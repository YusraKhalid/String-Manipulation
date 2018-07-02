import YKStringProcessor

def main():
    string = input("Enter replace string: ")
    finding = input("What do you want to find: ")
    replace = input("What do you want to replace: ")
    replaceWith = input("what do you want to replace it with: ")
    flag = True
    while flag == True:
        try:
            index01 = int(input("Where do you want to start from:"))
            index02 = int(input("Where do you want to end:"))
        except:
            flag = True
        else:
            flag = False
    end = input("Check if string ends with till the given end location:")
    start = input("Check if string starts with till the given start location:")


    print("Length of stirng is:",YKStringProcessor.length(string))
    print("The location of",finding," is",YKStringProcessor.find(string,finding))
    print("Replaced all:",YKStringProcessor.replace(string,replace,replaceWith))
    print("Uppercased:",YKStringProcessor.upperCase(string))
    print("Lowercase:",YKStringProcessor.lowerCase(string))
    print("Switchcase:",YKStringProcessor.switchCase(string))
    print("Is the string alpha:",YKStringProcessor.isAlpha(string))
    print("The location of",finding,"from right is:",YKStringProcessor.rfind(string,finding))
    print("The reversed string is:", YKStringProcessor.reverse(string))
    print("Replaced in the specific range:", YKStringProcessor.replaceStartEnd(string,replace,replaceWith,index01,index02))
    print("Found",finding," in a specific range:", YKStringProcessor.findStartEnd(string,finding,index01,index02))
    print("Capitalized first letters:",YKStringProcessor.capitalize(string))
    print("Does the string ends with",end,"in the specific range:",YKStringProcessor.endwith(string,finding,index01))
    print("Does string contains all digits:",YKStringProcessor.isdigit(string))
    print("Is sting a decimal",YKStringProcessor.isdecimal(string))
    print("Reversed individual words in a string:",YKStringProcessor.indivisualreverse(string))
    print("Does the string starts with",start,"in the specific range:",YKStringProcessor.startwith(string,finding,index01))
    print("Is all the string in lowercase:",YKStringProcessor.islower(string))
    print("Is all the string in uppercase:",YKStringProcessor.isupper(string))



main()
