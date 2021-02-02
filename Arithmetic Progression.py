import time
a = int(input("a: "))
d = int(input("d: "))
n = int(input("n: "))

s_n = 1
fs = "."
time.sleep(1)

print("The following is the AP:")
time.sleep(1)

#Print first number
print(f"{s_n}{fs} {a}")
time.sleep(1)

#Loop for the next numbers
for x in range(n-1):
    a = a + d
    s_n = s_n + 1
    print(f"{s_n}{fs} {a}")
    time.sleep(1)