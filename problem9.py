def findPythagorean():
    for a in range(1, 600):
        for b in range(200, 800):
            for c in range(300, 1000):
                if a **2 + b** 2 == c **2 and a + b + c == 1000:
                    return a, b, c

def main():
    a, b, c = findPythagorean()
    print(a, b, c)
    print(a * b * c)
main()
