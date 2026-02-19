from ._anvil_designer import GitfetchTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Gitfetch(GitfetchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    x=anvil.server.call_s('fetch',self.text_area_1.text)
    y=[]
    for i in x:
      try:
        y.append('<h1>'+i['description']+'</h1>')
        for k in i:
          v=i[k]
          if k!='description':
            y.append(str(k)+'='+str(v))
      except:
        pass
    ind=0
    for i in y:
      if not i:
        del y[ind]
      ind+=1
    self.rich_text_1.content='<br/>'.join(y)
