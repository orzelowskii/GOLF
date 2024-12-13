from enum import Enum
from typing import List

from colorama import Fore, Style


class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __str__(self):
        if self == Suit.HEARTS or self == Suit.DIAMONDS:
            return Fore.RED + self.value + Style.RESET_ALL
        elif self == Suit.CLUBS or self == Suit.SPADES:
            return Fore.LIGHTBLACK_EX + self.value + Style.RESET_ALL


class Valeu(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"

    def __str__(self):
        return self.value


class Card:
    _id = 0

    def __init__(self, suit: Suit, value: Valeu):
        self.suit = suit
        self.value = value
        self._id = Card._generate_id()

    @classmethod
    def _generate_id(cls) -> int:
        """
        Generuje id rosnąco
        :return: zraca id
        """
        cls._id += 1
        return cls._id

    @property
    def id(self) -> int:
        return self._id

    @property
    def valeu(self) -> Valeu:
        return self.value

    def __str__(self) -> str:
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self) -> List[Card]:
        """
        Tworzy liste 52 kart
        :return: talie kart
        """
        return [Card(suit, valeu) for suit in Suit for valeu in Valeu]

    def shuffle(self):
        """
        tasuje karty
        :return: None
        """
        import random
        random.shuffle(self.cards)

    def get_card_and_remove(self, index: int) -> Card:
        """
        zwraca karte i usuwa ją z talii
        :param index: indeks karty
        :return: karta usunieta
        """
        if 0 <= index < len(self.cards):
            return self.cards.pop(index)
        else:
            raise IndexError("Index out of range")

    def get_card(self, index: int) -> Card:
        return self.cards[index]

    def __str__(self) -> str:
        return '\n'.join([str(card) for card in self.cards])

    def is_empty(self) -> bool:
        """
        sprawdza czy talia jest pusta
        :return: zwraca true jak talia jest pusta
        """
        return len(self.cards) == 0


class Player:
    _id_counter = 0

    def __init__(self, name: str):
        self.name = name
        self._id = Player._generate_id()
        self._points = 0
        self._player_cards = []

    @classmethod
    def _generate_id(cls) -> int:
        """
        Generuje id rosnąco
        :return: zraca id
        """
        cls._id_counter += 1
        return cls._id_counter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def points(self) -> int:
        return self._points

    @property
    def num_of_cards(self) -> int:
        return len(self._player_cards)

    @property
    def id(self) -> int:
        return self._id

    def add_points(self, additional_points: int):
        """
        Dodaje punkty do aktualnych punktów gracza
        :param additional_points: dodatkowe punkty
        :return:
        """
        if not isinstance(additional_points, int):
            raise ValueError("Points must be an integer")
        self._points += additional_points

    @property
    def player_cards(self) -> List[Card]:
        return self._player_cards

    @property
    def player_cards_len(self) -> int:
        return len(self._player_cards)

    def add_card(self, card: Card) -> None:
        self._player_cards.append(card)

    def remove_card(self, index: int) -> None:
        self._player_cards.pop(index)

    def has_cards(self) -> bool:
        return len(self._player_cards) > 0

    def get_card_valeu_by_index(self, index: int) -> Valeu:
        """
        Zwraca wartość karty na podstawie indeku karty w talicy kart gracza
        :param index: indeks karty
        :return: wartość
        """
        if 0 <= index < len(self._player_cards):
            return self._player_cards[index].valeu
        else:
            raise IndexError("Index out of range")

    def __str__(self) -> str:
        return "id: {}, name: {}, points: {}".format(self.id, self.name, self.points)