def search_str(read_file, write_file, word):
  with open(read_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      if line.find(word) != -1:
        found = True
        getFunction(read_file, write_file, lines.index(line))
        break

def getFunction(read_file, write_file, line_number):
  x = 0
  while True:
    with open(read_file, 'r') as file:
      for i in range(line_number):
        next(file, None)
      for line in file:
        writeFunctionToFile(write_file, line)
        if line.find('{') != -1:
          x = x + line.count('{')
        if x == 0:
          break
        if line.find('}') != -1:
          x = x - line.count('}')
        if x == 0:
          break
      break

def writeFunctionToFile(write_file, line):
  with open(write_file, 'a') as file:
    file.write(line)