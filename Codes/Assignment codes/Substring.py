def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total


# if __name__ == '__main__':
string = input("Enter the string :")
sub_string = input("Enter the substring :")

count = count_substring(string, sub_string)
print(count)