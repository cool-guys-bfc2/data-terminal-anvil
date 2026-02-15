from ._anvil_designer import PytermTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Pyterm(PytermTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    x=anvil.server.call('execute',self.code.text)
    self.output.content=x
    print(x)
