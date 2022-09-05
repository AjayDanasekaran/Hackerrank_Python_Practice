def count_substring(string, sub_string):
    count = 0
    mainlength = len(string)
    sublength = len(sub_string)
    for i in range(mainlength):
        if string[i:i+sublength] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
