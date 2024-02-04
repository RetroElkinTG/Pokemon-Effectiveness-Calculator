# DISCLAIMER: The entire code was created by me with inspiration from Anvil tutorials.

from ._anvil_designer import PokemonHomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PokemonHome(PokemonHomeTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    
  def submit_button_click(self, **event_args):
    # This method is called when the button is clicked.
    # Resets results.
    self.NVE_label.visible=False
    self.SE_label.visible=False
    self.NE_label.visible=False
    self.SW_label.visible=False
    # Gets move and type of pokemon.
    if self.pokemon_move.text == "":
      pokemon_move = "Normal"
    else:
      pokemon_move = self.pokemon_move.text
    if self.pokemon_type.text == "":
      pokemon_type = "Normal"
    else:
      pokemon_type = self.pokemon_type.text
    # Pokemon type chart.
    type_chart = {
    'Normal': {
        'Rock': 0.5,
        'Ghost': 0,
        'Steel': 0.5
    },
    'Fire': {
        'Fire': 0.5,
        'Water': 0.5,
        'Grass': 2,
        'Ice': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Dragon': 0.5,
        'Steel': 2
    },
    'Water': {
        'Fire': 2,
        'Water': 0.5,
        'Grass': 0.5,
        'Ground': 2,
        'Rock': 2,
        'Dragon': 0.5
     },
    'Electric': {
        'Water': 2,
        'Electric': 0.5,
        'Grass': 0.5,
        'Ground': 0,
        'Flying': 2,
        'Dragon': 2
     },
    'Grass': {
        'Fire': 0.5,
        'Water': 2,
        'Grass': 0.5,
        'Poison': 0.5,
        'Ground': 2,
        'Flying': 0.5,
        'Bug': 2,
        'Rock': 2,
        'Dragon': 0.5,
        'Steel': 0.5
     },
    'Ice': {
        'Fire': 0.5,
        'Water': 2,
        'Grass': 2,
        'Ice': 0.5,
        'Ground': 2,
        'Flying': 2,
        'Dragon': 2,
        'Steel': 0.5
     },
    'Fighting': {
        'Normal': 2,
        'Ice': 2,
        'Poison': 0.5,
        'Flying': 0.5,
        'Psychic': 0.5,
        'Bug': 0.5,
        'Rock': 2,
        'Ghost': 0,
        'Dark': 2,
        'Steel': 2,
        'Fairy': 0.5
     },
    'Poison': {
        'Grass': 2,
        'Poison': 0.5,
        'Ground': 0.5,
        'Rock': 0.5,
        'Ghost': 0.5,
        'Steel': 0,
        'Fairy': 2
     },
    'Ground': {
        'Fire': 2,
        'Electric': 2,
        'Grass': 0.5,
        'Poison': 2,
        'Flying': 0,
        'Bug': 0.5,
        'Rock': 2,
        'Steel': 2
     },
    'Flying': {
        'Electric': 0.5,
        'Grass': 2,
        'Fighting': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Steel': 0.5
     },
    'Psychic': {
        'Fighting': 2,
        'Poison': 2,
        'Psychic': 0.5,
        'Dark': 0,
        'Steel': 0.5,
     },
    'Bug': {
        'Fire': 0.5,
        'Grass': 2,
        'Fighting': 0.5,
        'Posion': 0.5,
        'Flying': 0.5,
        'Psychic': 2,
        'Ghost': 0.5,
        'Dark': 2,
        'Steel': 0.5,
        'Fairy': 0.5
      },
    'Rock': {
        'Fire': 2,
        'Ice': 2,
        'Fighting': 0.5,
        'Ground': 0.5,
        'Flying': 2,
        'Bug': 2,
        'Steel': 0.5
       },
    'Ghost': {
        'Normal': 0,
        'Psychic': 2,
        'Ghost': 2,
        'Dragon': 0.5
       },
    'Dragon': {
        'Dragon': 2,
        'Steel': 0.5,
        'Fairy': 0,
       },
    'Dark': {
        'Fighting': 0.5,
        'Psychic': 2,
        'Ghost': 2,
        'Dark': 0.5,
        'Fairy': 0.5
       },
    'Steel': {
        'Fire': 0.5,
        'Water': 0.5,
        'Electric': 0.5,
        'Ice': 2,
        'Rock': 2,
        'Dark': 0.5,
        'Steel': 2
        },
    'Fairy': {
        'Fire': 0.5,
        'Ice': 2,
        'Poison': 0.5,
        'Dragon': 2,
        'Dark': 2,
        'Steel': 0.5
    } }
    # Retrieves value of type and move combination.
    get = type_chart.get(pokemon_move, {}).get(pokemon_type, 1)
    # Shows effectiveness text.
    if get == 0.5:
      self.NVE_label.visible=True
      text_result = "are not very effective"
    elif get == 2:
      self.SE_label.visible=True
      text_result = "are super effective"
    elif get == 0:
      self.NE_label.visible=True
      text_result = "have no effect"
    elif get == 1:
      self.SW_label.visible=True
      text_result = "have normal effectiveness"
    # Displays effectiveness of the move to the user.
    self.result.text = pokemon_move + "-type moves " + text_result + " against " + pokemon_type + "-type Pokemon."

  def moves_button_click(self, **event_args):
    # Opens moves table.
    open_form('PokemonMoves')

  def types_button_click(self, **event_args):
    # Opens types table.
    open_form('PokemonTypes')