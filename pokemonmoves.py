from ._anvil_designer import PokemonMovesTemplate
from anvil import *
import tables
from tables import app_tables
import anvil.server

class PokemonMoves(PokemonMovesTemplate):
  def __init__(self, **properties):
    # Loads the database as the form opens.
    self.init_components(**properties)
    self.repeating_panel_pokemon.items = anvil.server.call('get_pokemonmove')

  def text_box_1_lost_focus(self, **event_args):
    # This method is called when the TextBox loses focus.
    self.data_grid_pokemon.rows_per_page = int(self.text_box_1.text) + 1

  def search(self, **event_args):
    # Search the pokemon records for any for whom any field contains the query.
    self.repeating_panel_pokemon.items = anvil.server.call('search_pokemonmove', self.text_box_search.text)

  def home_button_click(self, **event_args):
    # Opens the homepage.
    open_form('PokemonHome')

  def types_button_click(self, **event_args):
    # Opens the types table.
    open_form('PokemonTypes')