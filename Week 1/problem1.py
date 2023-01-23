class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self, val):
    return val in self.__myTeam

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print ('Tim' in classmates)
  print ('Sam' in classmates)

main()