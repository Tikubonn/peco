
from io import StringIO

class Template:
  
  """
  this has information that parsed source code.
  you can get rendered text with .render() and .render_string()
  """
  
  def __init__ (self, sentencenode, scope):
    self.sentencenode = sentencenode
    self.scope = scope
  
  def render (self, stream, **parameters):
    
    """
    render template to stream with parameters.
    
    Parameters
    ----------
    stream: io.TextIOBase
      this file-like object used to output.
    parameters: 
      this used to rendering.
    """
    
    with self.scope:
      for name, value in parameters.items():
        self.scope.set_value(name, value)
      self.sentencenode.write(stream)
  
  def render_string (self, **parameters):
    
    """
    render template with parameters then return rendered text.
    
    Parameters
    ----------
    parameters: 
      this used to rendering.
      
    Returns
    -------
    rendered: str
      this is rendered string.
    """
    
    with StringIO() as stream:
      self.render(stream, **parameters)
      rendered = stream.getvalue()
      return rendered
    