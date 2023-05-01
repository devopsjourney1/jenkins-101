import fire

def hello(name="World"):
  return "Hello %s! Welcome to my world!" % name

if __name__ == '__main__':
  fire.Fire(hello)