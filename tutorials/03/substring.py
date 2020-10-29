def is_substring(string, substring):
    if len(substring) > len(string):
        return False
    
    for index, char in enumerate(substring):
        if char != string[index]:
            return False

    return True


string = input()
if string == '0':
    exit()

substring = input()
while substring != '0':
    if is_substring(string, substring):
        print(substring, end = ' ')
    substring = input()
