#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_postive(n):
    if (n<1):
        return 0
    else:
        return n+sum_postive(n-2)
n=int(input("Enter the N value"))  
print(sum_postive(n))
