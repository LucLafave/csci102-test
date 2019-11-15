# fibonacci.py

def fib():
    fibs = [1, 2]
    x = 0
    y = 0
    num = 1
    for i in range(1,9):
        if i == 0:
            continue
        else:
            fibs.append(fibs[i-1] + fibs[i])

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
    
