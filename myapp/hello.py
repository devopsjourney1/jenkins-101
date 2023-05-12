import fire

def hello(name="World"):
  return "Hello %s! Welcome to my world! " % name


def test(name):
  if name:
    return True
  else:
    return False
  
  # retrun True
  
def test2(name):
  print(f'hello {name}')

def test3(name):
  print(f'hello {name}')

if __name__ == '__main__':
  fire.Fire(hello)