def array():
    arr = []
    for i in range(int(input())):
        arr.append(int(input()))
    return arr

def main():
    arr = array()
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()