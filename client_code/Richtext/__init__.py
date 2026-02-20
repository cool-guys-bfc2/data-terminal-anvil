from ._anvil_designer import RichtextTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Richtext(RichtextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_area_1.text=anvil.server.call_s('getconn','html.index')
    self.dropdown_menu_1.selected_value=anvil.server.call_s("getconn","html.format")

    # Any code you write here will run before the form opens.

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    if self.dropdown_menu_1.selected_value not in ['javascript']:
      self.refresh_data_bindings()

  @handle("text_area_1", "change")
  def text_area_1_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    x=self.text_area_1.text
    anvil.server.call_s('conn',x,'html.index')

  @handle("dropdown_menu_1", "change")
  def dropdown_menu_1_change(self, **event_args):
    """This method is called when an item is selected"""
    anvil.server.call_s('conn',self.dropdown_menu_1.selected_value,"html.format")

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    self.refresh_data_bindings()
    """This method is called when the component is clicked."""
    if self.dropdown_menu_1.selected_value=='javascript':
      result = anvil.js.window.eval(self.text_area_1.text)
      if result:
        self.rich_text_1.content=result
      else:
        self.rich_text_1.content="No output was given..."
