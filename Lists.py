import time
camp_list = ["bruh", "lmao", "red bull"]
camp_site = ["Crystal Lake", 404, 37.2, True]
me = camp_list[0]
you = camp_list[-1]
print(me)
print(you)
print(camp_list)
ok = input("ok\n")
if ok == "location":
    print(camp_site[0])
    time.sleep(5)
elif ok == "number":
    print(camp_site[1])
    time.sleep(5)
elif ok == "temp":
    print(camp_site[2])
    time.sleep(5)
elif ok == "danger":
    print(camp_site[3])
    time.sleep(5)
#lists are awesome
#let me tell you why
#because they are not bloated like strings
#example = "hi strings are awesome"
#and you cannot call out diffrent words, letters, etc from a string
#but in lists you can
#because lists are indexed(in order)
#example = ["ok", "lmao", "hehe"]
#and computers start counting from "0" so ok is 0, lmao is 1, hehe is 2