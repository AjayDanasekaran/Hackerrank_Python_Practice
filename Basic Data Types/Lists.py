if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        s=input().split();
        for i in range(1,len(s)):
            s[i]=int(s[i])
        if s[0] == "insert":
            L.insert(s[1],s[2])
        elif s[0] == "append":
            L.append(s[1])
        elif s[0] == "pop":
            L.pop();
        elif s[0] == "print":
            print(L)
        elif s[0] == "remove":
            L.remove(s[1])
        elif s[0] == "sort":
            L.sort();
        else:
            L.reverse();
