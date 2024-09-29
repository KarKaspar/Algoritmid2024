#Fibonacci
#F0 = 0
#F1 = 1
#Fn = F(n-1)+F(n-2)
def fibonacci(n):
    null=0
    üks=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n-1):
            if i%2==0:
                null=null+üks
            else:
                üks=üks+null
        if n%2==0:
            return null
        else:
            return üks