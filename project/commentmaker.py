# GRUPPE 21
import os

files = [x for x in os.listdir() if x[-2:] == 'py']

commend = '# GRUPPE 21\n'
for root, dirs, files in os.walk('.'):
    for file in files:
        if file[-2:] == 'py':
            path = os.path.join(root, file)
            data = ''
            with open(path, 'r') as f:
                data = commend + f.read()
            with open(path, 'w') as f:
                f.write(data)
            print(path)
