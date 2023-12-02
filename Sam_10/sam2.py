try:
    with open('empty_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("файл пустой")
        else:
            print(data)
except Exception as e:
    print(e)

try:
    with open('non_empty_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("файл пустой")
        else:
            print(data)
except Exception as e:
    print(e)