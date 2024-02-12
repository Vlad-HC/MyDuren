from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from duren import Deck

class DeckApp(App):
    card1_image = ObjectProperty(None)
    card2_image = ObjectProperty(None)
    result_text = ObjectProperty('')

    def build(self):
        self.deck = Deck()
        return DeckLayout()

    def draw_cards(self):
        card1 = self.deck.deck[0]
        card2 = self.deck.deck[1]
        difference, winner = self.deck.compare_cards(card1, card2)
        self.result_text = f'Difference: {difference}, Winner: {winner}'

class DeckLayout(BoxLayout):
    pass

if __name__ == '__main__':
    DeckApp().run()

