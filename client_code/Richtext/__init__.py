from ._anvil_designer import RichtextTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Richtext(RichtextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_area_1.text=anvil.server.call_s('getconn','html.index')
    # Any code you write here will run before the form opens.

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.refresh_data_bindings()

  @handle("text_area_1", "change")
  def text_area_1_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    x=self.text_area_1.text
    anvil.server.call_s('conn',x)
