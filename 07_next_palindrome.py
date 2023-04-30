def is_palindrome(s):
    a=str(s)
    return a==a[::-1]                       

def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n=n+1
    return n

if __name__=="__main__":
    try:
        num=int(input("enter number of test subjects: \n"))
        list=[]
        for i in range(num):
            a=int(input(f"enter element no \"{i+1}\" to check its next PALINDROME: \n"))
            list.append(a)

        for i in range(num):
            print(f"Next PALINDROME for {list[i]} is {next_palindrome(list[i])}")
    
    except ValueError:
        print("only Integers allowed!!")

