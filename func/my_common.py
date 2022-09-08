from ast import If


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 关键字参数
def _person(name, age, kw):
    kw['sex'] = '2'
    print(name, age, kw)

# 头字母大写英文
def normalize(str):
    return str[0].upper()+str[1:].lower()
