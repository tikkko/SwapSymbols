
def swap(a: [str]):
    b = a.find(' ')
    c = a.rfind(' ')

    x = a[b + 1:c]
    g = x.replace('h', 'H')

    f = a.replace(x, g)
    return f


if __name__ == '__main__':
    print(swap("hello hill house horse"))