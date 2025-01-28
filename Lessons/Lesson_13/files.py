import os
# data_file = open('data.txt', 'r')
# data = data_file.read()
# print('srtrte' + 1)
# data_file.close()

base_path = os.path.dirname(__file__)
# file_path = f'{base_path}/data.txt'
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)
def read_file():
    with open(file_path, 'r') as data_file:
        # data = data_file.read()
        # print(data)
        for line in data_file.readlines():
            yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

pavel_path = os.path.dirname(os.path.dirname(base_path))
final_pavel_path = os.path.join(pavel_path, 'test.py')
print(final_pavel_path)

with open(final_pavel_path) as pavel_file:
    print(pavel_file)
