def reverse(integer):
    strinteger = str(integer)
    backwards = ''
    for i in range(len(strinteger) - 1, -1, -1):
        backwards += strinteger[i]
        i -= 1
    return int(backwards)

    
def main():
    plist = []
    for i2 in range(999, 600, -1):
        for i in range(999, 600, -1):
            intcheck = i * i2
            if intcheck == reverse(intcheck):
                plist.append(intcheck)
    lpp = max(plist)
    print(lpp)
                

main()

