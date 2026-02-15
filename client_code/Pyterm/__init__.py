from ._anvil_designer import PytermTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Pyterm(PytermTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.code.text=anvil.server.call_s('getconn','py.main')
    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    x=anvil.server.call_s('execute',self.code.text)
    self.output.content+='\n'+x
    print(x)

  @handle("code", "change")
  def code_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    anvil.server.call_s('conn',self.code.text,'py.main')

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.text_1.text=anvil.server.call_s('getconn','status')
    x='Pending' in self.text_1.text
    self.linear_progress_indicator_1.visible=x
    
