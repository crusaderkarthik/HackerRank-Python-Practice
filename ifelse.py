        ##** TYPE 1 **##

n = int(input())
if (n % 2 == 1):
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n>20:
    print("Not Weird")

        ##** TYPE 2 **##
n=int(input())
print("Weird" if n % 2 == 1 or n in range(6,21) else "Not Weird")
