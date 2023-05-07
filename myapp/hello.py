import fire

def hello(name="World"):
  return "Hello %s! Welcome to my world! " % name
def test(name):
  if name:
    return True
  else:
    return False
  retrun "None"
if __name__ == '__main__':
  fire.Fire(hello)