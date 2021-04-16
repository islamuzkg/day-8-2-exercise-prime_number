#Write your code below this line 👇
def prime_checker(number):
    prime_list=[]
    for j in range(2, number+1):
        if all(j % i != 0 for i in range(2, j)):
            prime_list.append(j)
            
    if number in prime_list:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



