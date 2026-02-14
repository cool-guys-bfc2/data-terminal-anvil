from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import m3.components as m3


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
