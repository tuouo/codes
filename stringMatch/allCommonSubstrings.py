#！/usr/bin/env python3
# -*- coding: utf-8 -*-

def acs(a, b):
    x, y = 0, 0
    xylen = 1
    aLen = len(a)
    bLen = len(b)    
    result = [[0 for i in range(bLen + 1)] for j in range(aLen + 1)]
    for i in range(aLen):
        for j in range(bLen):
            if a[i] == b[j]:
                result[i+1][j+1] = result[i][j] + 1
                if result[i+1][j+1] > xylen:
                    x, y, xylen = i, j, result[i+1][j+1]
        #print(result[i + 1][1:])
    for i in result:
        del i[0]
    return result[1:], x - xylen + 1 , y - xylen + 1, xylen

if __name__ == '__main__':
    a = 'gtcctcgatacaggtatttccactcatccagacttaaatattcgtggtggcgctagcttt'
    b = 'agtgccacacttgagcaagctgttaatagcgcgacttctagaggcgttcttgttgtagcg'
    a = 'gtcctcga'
    b = 'agtgccac'
    result, x, y, xylen = acs(a, b)
    sub = a[x : x + xylen]
    print(x, y, xylen, sub)
    print('%s len(a):%s,site:%s' % (a, len(a), x))
    print(' ' * x + sub)
    print('%s len(b):%s,site:%s' % (b, len(b), y))
    print(' ' * y + sub)
    for i in result:
        print(i)    