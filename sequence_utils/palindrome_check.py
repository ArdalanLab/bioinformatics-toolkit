#check if a sequence is palindrome or not:
def ispalindrom(mystr, s, e):
    if s >= e:
        return True
    if(mystr[s] != mystr[e]):
        return False
    if (s < e + 1):
        return ispalindrom(mystr, s + 1, e - 1)
x = "aattaa"
print(ispalindrom(x, 0, len(x)-1))
#the function loops as long as it does not reach a False at line "5"
