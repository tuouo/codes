#！/usr/bin/env python3
# -*- coding: utf-8 -*-

def lcs(a, b):
    aLen = len(a)
    bLen = len(b)
    result = [[0 for i in range(bLen + 1)] for j in range(aLen + 1)]
	# error: result = [[0] * (bLen + 1)] * (aLen + 1) 		#point same (aLen + 1), not point (aLen + 1) list
    for i in range(aLen):
        for j in range(bLen):
            if a[i] == b[j]:
                result[i+1][j+1] = result[i][j] + 1
            elif result[i][j+1] > result[i+1][j]:
                result[i+1][j+1] = result[i][j+1]
            else:
                result[i+1][j+1] = result[i+1][j]
    return result

def lcsGet(a, b):
    res = lcs(a, b)
    aLen = len(a)
    bLen = len(b)
    strs = []
    while(aLen > 0 and bLen > 0):
        if res[aLen-1][bLen] == res[aLen][bLen]:
            aLen -= 1
        elif res[aLen][bLen-1] == res[aLen][bLen]:
            bLen -= 1
        else:
            aLen -= 1
            bLen -= 1
            strs.append(a[aLen])
    return strs[::-1]

def show(strs, *n):
    slen = len(strs)
    print(slen, ''.join(strs))
    for a in n:
        p = 0
        print(a)
        for i in range(len(a)):
            if a[i] == strs[p]:
                print(a[i], end = '')
                p += 1
                if p == slen:
                    print()
                    break
            else:
                print(' ', end = '')


if __name__ == '__main__':
    a = 'gtcctcgatacaggtatttccactcatccagacttaaatattcgtggtggcgctagcttt'
    b = 'agtgccacacttgagcaagctgttaatagcgcgacttctagaggcgttcttgttgtagcg'
    #res = lcs(a, b)
    #print(res[-1][-1], len(a), len(b))
    #for i in res:
        #print(i)	
    strs = lcsGet(a, b)
    show(strs, a, b)