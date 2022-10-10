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
        writeFunctionToFile(line)
        if line.find('{') != -1:
          x = x + line.count('{')
        if x == 0:
          break
        if line.find('}') != -1:
          x = x - line.count('}')
        if x == 0:
          break
      break

def writeFunctionToFile(line):
  with open('functions.js', 'a') as file:
    file.write(line)

search_str(r'text.txt', 'MakeHouse')