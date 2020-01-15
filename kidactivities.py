running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(name):
    print(f"{name} is running")

def swing(name):
    print(f"{name} is swinging")

def slide(name):
    print(f"{name} is sliding")

def hide(name):
    print(f"{name} is hiding")

for i in running_kids:
    run(i) 

for i in swinging_kids:
    swing(i)

for i in sliding_kids:
    slide(i)

for i in hiding_kids:
    hide(i)


