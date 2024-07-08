a=int(input())
b=int(input())

try:
    if b==0:
        raise ZeroDivisionError
    
except ZeroDivisionError as ze:
    print(ze)

else:
    print(a/b)

#  & "C:/Program Files/Python311/python.exe" "c:/Users/jadha/OneDrive/Desktop/Python/Exception Handling/raise.py"