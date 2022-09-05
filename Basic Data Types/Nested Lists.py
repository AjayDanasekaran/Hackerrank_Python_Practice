if __name__ == '__main__':
    marks={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks[name]=score
        
    mark = marks.values()
    lowest = sorted(list(set(mark)))[1]
    low = []
    
    for key,value in marks.items():
        if value == lowest:
            low.append(key)
            
    low.sort()
    for name in low:
        print(name)
    
        
