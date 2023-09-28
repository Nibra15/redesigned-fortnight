a = "fiajfökafj  oafjak mf afj pa j oleg@mail.ru" .split("@")
string1 = a[0]
string2 = a[1]
index_of_space1 = string1.rfind(" ")
index_of_space2 = string2.rfind(" ")
print(string1[31:]+"@"+string2[:7])