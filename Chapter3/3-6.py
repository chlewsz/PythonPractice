guests = ['john', 'bob', 'lili']

print(guests[1].title() + ' refuse my invitation')
guests.remove('bob')

print('I found a bigger dining-table')
guests.insert(0, 'mark')
guests.insert(2, 'lucy')
guests.append('jack')
print('I want to invite ' + guests[0].title() + ' to party.')
print('I want to invite ' + guests[1].title() + ' to party.')
print('I want to invite ' + guests[2].title() + ' to party.')
print('I want to invite ' + guests[3].title() + ' to party.')
print('I want to invite ' + guests[4].title() + ' to party.')

print('Have ' + str(len(guests)) + " guest will comming")