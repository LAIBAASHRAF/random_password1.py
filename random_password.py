import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}()<>,._+-=/\@#$%^&*"
all = lower+upper+numbers+symbols
lenght = 10
password = "".join(random.sample(all, lenght))
print("the random password you generated:", password)

