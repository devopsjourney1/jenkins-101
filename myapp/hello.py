import fire

def hello(name="World"):
  return "Hello %s! Welcome to my worlkd" % name

if __name__ == '__main__':
  fire.Fire(hello)