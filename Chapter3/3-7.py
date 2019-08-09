guests = ['john', 'bob', 'lili']

print(guests[1].title() + ' refuse my invitation')
guests.remove('bob')

print('I found a bigger dining-table')
guests.insert(0, 'mark')
guests.insert(2, 'lucy')
guests.append('jack')

print('sorry, I have only invite two guest')
print('sorry, ' + guests.pop())
print('sorry, ' + guests.pop())
print('sorry, ' + guests.pop())
print('I want to invite ' + guests[0].title() + ' to party.')
print('I want to invite ' + guests[1].title() + ' to party.')
del guests[1]
del guests[0]
print(guests)