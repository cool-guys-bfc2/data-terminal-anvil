import anvil.server
import io
from contextlib import redirect_stdout
import math,string,random,re,json,cmath,datetime,csv,time

@anvil.server.callable
def execute(rc,env={}):
  anvil.server.cookies.shared['status']='Pending task...'
  scope={'math':math,'string':string,'random':random,'re':re,'json':json,'datetime':datetime,'cmath':cmath,'csv':csv,'time':time}
  for k in env:
    scope[k]=env[k]
  text=rc
  text = text.replace('“', '"').replace('”', '"') # Double quotes
  text = text.replace('‘', "'").replace('’', "'") # Single quotes
  c=text
  buffer=io.StringIO()
  with redirect_stdout(buffer):
    exec(c,{'__builtins__':__builtins__},scope)
  x=buffer.getvalue()
  anvil.server.cookies.shared['status']='Complete!'
  return x

@anvil.server.route('/python')
def pyterm():
  return anvil.server.FormResponse('Pyterm')