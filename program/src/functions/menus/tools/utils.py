def update_tasks(user_name, line):
  with open('../../builtSites/' + user_name + '/tasks.txt', 'a') as file:
    file.write(line)
    return 0