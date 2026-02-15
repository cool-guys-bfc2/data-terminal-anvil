import anvil.server
import io
from contextlib import redirect_stdout

@anvil.server.callable
def execute(rc):
  text=rc
  text = text.replace('“', '"').replace('”', '"') # Double quotes
  text = text.replace('‘', "'").replace('’', "'") # Single quotes
  c=text
  buffer=io.StringIO()
  with redirect_stdout(buffer):
    exec(c,{'__builtins__':__builtins__},{})
  x=buffer.getvalue()
  return x

@anvil.server.route('/python')
def pyterm():
  return anvil.server.