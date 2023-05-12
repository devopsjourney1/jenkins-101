import fire

def hello(name="World"):
  return "Hello %s! Welcome to my world! " % name


def test(name):
  if name:
    msg = "Test: {1}."
    return
  else:
    return False
  
  # retrun True
  
def test2(name):
  print('Error code %d' % '42') 
  print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
  print(f'hello {name}')

def test3(name):
  print(f'hello {name}')
  z = (1,2) + ['a']
  return z

if __name__ == '__main__':
  fire.Fire(hello)