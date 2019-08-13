# -*- coding:utf-8 -*-

words = {
    'java': '依靠jvm虚拟机进行编译运行',
    'PHP': '号称世界上最好的语言',
    'python': '功能强大简单的语言',
    'flutter': '基于Dart实现的UI框架',
    'swift': '全新的IOS编程语言'
}

print(words)

for key, value in words.items():
    print('\nlanguage:' + key)
    print('feature:' + value)