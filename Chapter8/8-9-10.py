def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# 10
"""
def make_great(magicians):
    index = 0
    for index in range(0, len(magicians)):
        magicians[index] += ' the Great'
        index += 1
"""

# 11
def make_great(magicians, new_magicians):
    while(magicians):
        magician = magicians.pop()
        new_magicians.append(magician + ' the Great')
    return new_magicians

magicians = ['liuqian', 'Dynamo', 'Jason Latimer']

show_magicians(magicians)

# 10
# make_great(magicians)
# show_magicians(magicians)

# 11
new_magicians = []
make_great(magicians[:], new_magicians)
show_magicians(magicians)
show_magicians(new_magicians)