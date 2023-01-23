class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __iter__(self):
    return iter(self.__myTeam)

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  for member in classmates:
    print(member)

main()