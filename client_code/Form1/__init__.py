from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import m3.components as m3

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    x=anvil.server.call_s('getconn')
    self.connect.text=x
    y='Pending' in anvil.server.call_s('getconn','status')
    self.navigation_link_1.badge=y
    # Any code you write here will run before the form opens.

  @handle("submit", "click")
  def submit_click(self, **event_args):
    """This method is called when the component is clicked."""
    x=anvil.server.call('execute_query',self.connect.text,self.query.text)
    if isinstance(x,str):
     self.output.content+='\n'+x
    else:
      self.output.content+='\n'+str(x)

  @handle("connect", "change")
  def connect_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    anvil.server.call_s('conn',self.connect.text)
