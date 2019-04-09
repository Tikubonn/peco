
class Scope:
  
  def __init__ (self):
    self.scopes = [{}]
  
  def __enter__ (self):
    self.enter()
  
  def __exit__ (self, error, errorvalue, backtrace):
    self.exit()
  
  def enter (self):
    self.scopes.append(dict())
  
  def exit (self):
    self.scopes.pop()
  
  def get_value (self, name, defaultvalue=None):
    for scope in reversed(self.scopes):
      if name in scope:
        return scope[name]
    return defaultvalue
  
  def set_value (self, name, value):
    self.scopes[-1][name] = value
  