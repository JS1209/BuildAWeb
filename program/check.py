def search_str(file_path, word):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      if line.find(word) != -1:
        found = True
        getFunction(file_path, lines.index(line))
        break

def getFunction(file_path, line_number):
  x = 0
  while True:
    with open(file_path, 'r') as file:
      for i in range(line_number):
        next(file, None)
      for line in file:
        print(line)
        if line.find('{') != -1:
          x = x + 1
        if line.find('}') != -1:
          x = x - 1
        if x == 0:
          break
      break

search_str(r'text.txt', 'dezeFunctie')