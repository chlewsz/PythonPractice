# -*- coding:utf-8 -*-

rivers = {
    'changjiang': 'china',
    'huanghe': 'china',
    'nile': 'egypt'
}

for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title())

for river_name in rivers.keys():
    print(river_name)

for river_country in set(rivers.values()):
    print(river_country)