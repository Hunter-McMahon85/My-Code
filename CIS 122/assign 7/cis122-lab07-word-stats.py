# CIS 122 spring 2021 lab 7 word stats
# Author: Hunter McMahon
# Partner: completed solo during lab session
# Description: hold on one sec just need my ti84

#import our word list
fin = open('words_alpha.txt')

#temp variables to hold the stats
count = 0
longest = ''
shortest = 'this is just a temporary word so that the lenght of this temp sting is long so that the shortest word can be tested for'
palindromes = 0
other = a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0

#find our stats with a for loop
for line in fin:
    line =line.strip()
    count += 1
    if len(line) > len(longest):
        longest = line
    if len(line) < len(shortest):
        shortest = line
    if line == line[::-1]:
        palindromes += 1
    if line.lower()[0] == 'a':
        a += 1
    elif line.lower()[0] == 'b':
        b += 1
    elif line.lower()[0] == 'c':
        c += 1
    elif line.lower()[0] == 'd':
        d += 1
    elif line.lower()[0] == 'e':
        e += 1
    elif line.lower()[0] == 'f':
        f += 1
    elif line.lower()[0] == 'g':
        g += 1
    elif line.lower()[0] == 'h':
        h += 1
    elif line.lower()[0] == 'i':
        i += 1
    elif line.lower()[0] == 'j':
        j += 1
    elif line.lower()[0] == 'k':
        k += 1
    elif line.lower()[0] == 'l':
        l += 1
    elif line.lower()[0] == 'm':
        m += 1
    elif line.lower()[0] == 'n':
        n += 1
    elif line.lower()[0] == 'o':
        o += 1
    elif line.lower()[0] == 'p':
        p += 1
    elif line.lower()[0] == 'q':
        q += 1
    elif line.lower()[0] == 'r':
        r += 1
    elif line.lower()[0] == 's':
        s += 1
    elif line.lower()[0] == 't':
        t += 1
    elif line.lower()[0] == 'u':
        u += 1
    elif line.lower()[0] == 'v':
        v += 1
    elif line.lower()[0] == 'w':
        w += 1
    elif line.lower()[0] == 'x':
        x += 1
    elif line.lower()[0] == 'y':
        y += 1
    elif line.lower()[0] == 'z':
        z += 1
    else:
        other += 1
def percent(num):
    """
    takes a number and divides it by count to calculate its percentage
        does the math to calculat the percent of what letters make up the first letters of the words on the list
    Args
    num(int): the number were finding the percent of the total count of
    Returns:
    perc: the percentage rounded and as a string
    """
    perc = 100*(num/count)
    perc = round(perc, 2)
    perc = str(perc)+'%'
    return perc
#print the stats
print('Count:', count)
print('Longest word is', longest, '('+str(len(longest))+')')
print('Shortest word is', shortest, '('+str(len(shortest))+')')
print('Palindromes:', palindromes, '('+percent(palindromes)+')')
print('First letter counts')
print('A:', a, '('+percent(a)+')')
print('B:', b, '('+percent(b)+')')
print('C:', c, '('+percent(c)+')')
print('D:', d, '('+percent(d)+')')
print('E:', e, '('+percent(e)+')')
print('F:', f, '('+percent(f)+')')
print('G:', g, '('+percent(g)+')')
print('H:', h, '('+percent(h)+')')
print('I:', i, '('+percent(i)+')')
print('J:', j, '('+percent(j)+')')
print('K:', k, '('+percent(k)+')')
print('L:', l, '('+percent(l)+')')
print('M:', m, '('+percent(m)+')')
print('N:', n, '('+percent(n)+')')
print('O:', o, '('+percent(o)+')')
print('P:', p, '('+percent(p)+')')
print('Q:', q, '('+percent(q)+')')
print('R:', r, '('+percent(r)+')')
print('S:', s, '('+percent(s)+')')
print('T:', t, '('+percent(t)+')')
print('U:', u, '('+percent(u)+')')
print('V:', v, '('+percent(v)+')')
print('W:', w, '('+percent(w)+')')
print('X:', x, '('+percent(x)+')')
print('Y:', y, '('+percent(y)+')')
print('Z:', z, '('+percent(z)+')')
print('Other:', other, '('+percent(other)+')')
