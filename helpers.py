import re 

def multiple_replace(dict, text):
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

