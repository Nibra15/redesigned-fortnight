inp = input("")
ban = ["=","?","*","^","$","№","@","_"]
for bukva in inp:
    for i in ban:
        if bukva == i:
            print(bukva)
