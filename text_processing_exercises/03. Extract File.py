def extract(data):
    needed_info = data[-1].split('.')
    file_name = needed_info[0]
    extension = needed_info[1]

    print(f'File name: {file_name}')
    print(f'File extension: {extension}')


d = input().split('\\')
extract(d)
