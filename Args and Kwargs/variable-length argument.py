def format(**kwargs):
    a = []
    for key,val in kwargs.items():
        a.append((key,val))
    return kwargs,a

print(format(name="arnab",roll=12)) # ({'name': 'arnab', 'roll': 12}, [('name', 'arnab'), ('roll', 12)])


def say(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("roll"))
    return

say(name="arnab",roll=12)