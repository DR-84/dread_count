# calculate dread


import pyfiglet

ascii_banner1 = pyfiglet.figlet_format("DREADCOUNT")
ascii_banner2 = pyfiglet.figlet_format("DREAD =")
print(ascii_banner1)

print("Enter Damage:")
a = float(input())
print("Enter Reproducibility:")
b = float(input())
print("Enter Exploitability:")
c = float(input())
print("Enter Effected Users:")
d = float(input())
print("Enter Discoverability:")
e = float(input())

dread = (a + b + c + d + e) // 5
print(
    "\nDamage ={}\nReproducibility ={}\nExploitability ={}\nEffected Users ={}\nDiscoverability ={}".format(
        a, b, c, d, e
    )
)
print(ascii_banner2, dread)
