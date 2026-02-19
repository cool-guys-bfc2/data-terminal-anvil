from ._anvil_designer import RichtextTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Richtext(RichtextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.refresh_data_bindings()
