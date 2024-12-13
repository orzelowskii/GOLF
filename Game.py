from typing import List

from colorama import Fore, Style

from Objects import Valeu, Deck, Player, Card


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.seen_deck = []

    def single_player(self) -> None:
        """
        Rozpoczęcie gry jednoosobowej. podglądanie kart. zapis gry.
        :return: None
        """
        player = Player(input("Podaj imie gracza: "))
        player_computer = Player("computer")
        list_of_players = [player, player_computer]
        self.deal_cards(list_of_players)
        self.single_suspicion_of_cards(list_of_players)
        self.single_main_play(list_of_players)
        self.count_points(list_of_players)
        if self.winner(list_of_players) == player_computer.name:
            print(Fore.RED + "\nPRZEGRAŁEŚ :((\n" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"\nWYGRAŁEŚ {player.name} !!!\n" + Style.RESET_ALL)
        self.save_game(list_of_players)

    def single_main_play(self, list_of_players: List[Player]) -> None:
        """
        Głowna pętla gry jednoosobowej. ruch odbywa gracz na zmiane z komputerem
        :param list_of_players: lista graczy
        :return: None
        """
        num_of_round = 2
        golf = True
        has_cards = True

        while not self.deck.is_empty() and golf and has_cards:
            print(Fore.YELLOW + f"RUNDA {num_of_round}" + Style.RESET_ALL)
            print("===============================")
            previous_player = None
            for player in list_of_players:
                if not golf:
                    print(f"Gracz {previous_player.name} krzyknał GOLF")
                    break
                if not has_cards:
                    print(f"Gracz {previous_player.name} pozbył sie wszystkich kart")
                    break
                if self.deck.is_empty():
                    print("Skończyły sie karty w talii")
                    break
                if player.name != "computer":
                    print(Fore.CYAN + player.name + Style.RESET_ALL + ", twoja kolej")
                    print("Karty: ")
                    self.show_stars(player)
                    print("Karta na stosie kart użytych:")
                    print(self.seen_deck[0])
                    print()
                    print("Wybierz swój ruch:")
                    print("1. odrzuć karte")
                    print("2. wez karte ze stosu")
                    print("3. wez karte ze stosu kart zużytych")
                    print("4. GOLF!!!")
                    opt = (int)(input("Wybieram: "))
                    while opt < 1 or opt > 4:
                        print("Zły wybór, musisz wybrać między 1 a 3")
                        opt = (int)(input("Wybieram: "))

                    match opt:
                        case 1:
                            print()
                            self.throw_card(player)
                        case 2:
                            print()
                            self.take_new_card(player)
                        case 3:
                            print()
                            self.take_seen_card(player)
                        case 4:
                            golf = False
                else:
                    opt = 2

                    for i in range(player.player_cards_len):
                        if self.compare_card_values(self.seen_deck[0], player.player_cards[i]):
                            opt = 3
                            index = i

                    for i in range(player.player_cards_len):
                        if self.get_card_valeu_by_index(0) == player.get_card_valeu_by_index(i):
                            opt = 1
                            index = i

                    match opt:
                        case 1:
                            self.single_throw_card(player, index)
                        case 2:
                            self.single_take_new_card(player)
                        case 3:
                            self.single_take_seen_card(player, index)
                        case 4:
                            golf = False

                previous_player = player
            num_of_round += 1
            print("===============================\n")

    def multi_player(self) -> None:
        """
        Rozpoczęcie gry wielosobowej. podglądanie kart. zapisywanie gry
        :return: None
        """
        num_of_players = (int)(input("Wybierz liczbe graczy: "))
        while num_of_players <= 1:
            print("liczba graczy musi być conajmniej 2 !!!")
            num_of_players = (int)(input("Wybierz liczbe graczy: "))

        list_of_players = []

        for i in range(num_of_players):
            player = Player(input("Podaj imie gracza " + (str)(i + 1) + ": "))
            list_of_players.append(player)
        self.deal_cards(list_of_players)
        self.suspicion_of_cards(list_of_players)
        self.multi_main_play(list_of_players)
        self.count_points(list_of_players)
        print(f"\nWygrał {self.winner(list_of_players)} !!!\n")
        self.save_game(list_of_players)

    def multi_main_play(self, list_of_players: List[Player]) -> None:
        """
        Główna pętla gry wieloosobowej. ruch odbywa każdy gracz z listy.
        :param list_of_players: lista graczy
        :return: None
        """
        num_of_round = 2
        golf = True
        has_cards = True

        while not self.deck.is_empty() and golf and has_cards:
            print(Fore.YELLOW + f"RUNDA {num_of_round}" + Style.RESET_ALL)
            print("===============================")
            previous_player = None
            for player in list_of_players:
                if not golf:
                    print(f"Gracz {previous_player.name} krzyknał GOLF")
                    break
                if not has_cards:
                    print(f"Gracz {previous_player.name} pozbył sie wszystkich kart")
                    break
                if self.deck.is_empty():
                    print("Skończyły sie karty w talii")
                    break
                print(Fore.CYAN + player.name + Style.RESET_ALL + ", twoja kolej")
                print("Karty: ")
                self.show_stars(player)
                print()
                print("Karta na stosie kart użytych:")
                print(self.seen_deck[0])
                print()
                print("Wybierz swój ruch:")
                print("1. odrzuć karte")
                print("2. wez karte ze stosu")
                print("3. wez karte ze stosu kart zużytych")
                print("4. GOLF!!!")
                opt = (int)(input("Wybieram: "))
                while opt < 1 or opt > 4:
                    print("Zły wybór, musisz wybrać między 1 a 3")
                    opt = (int)(input("Wybieram: "))

                match opt:
                    case 1:
                        print()
                        self.throw_card(player)
                    case 2:
                        print()
                        self.take_new_card(player)
                    case 3:
                        print()
                        self.take_seen_card(player)
                    case 4:
                        golf = False
                previous_player = player
            num_of_round += 1
            print("===============================\n")

    def throw_card(self, player: Player) -> None:
        """
        Pozwala odrzucc karte graczowi w grze wieloosoboweji
        :param player: gracz
        :return: None
        """
        print("wybierz karte ktorą chcesz odrzucić:")
        self.show_stars(player)
        x = (int)(input("numer karty: "))
        while x < 1 or x > player.player_cards_len:
            print(f"Zły wybór, musisz wybrać między 1 a {player.player_cards_len}")
            x = (int)(input("numer karty: "))
        if player.get_card_valeu_by_index(x - 1) == self.get_card_valeu_by_index(0):
            print("\nTrafiłeś !!!\n")
            self.seen_deck.insert(0, player.player_cards[x - 1])
            player.remove_card(x - 1)
        else:
            print("\nNie tarfiłeś :((\n")
            player.player_cards.append(self.deck.get_card_and_remove(0))

    def single_throw_card(self, player: Player, index: int) -> None:
        """
        pozwala odrzucić karte wskazaną przez użytkownika w grze jednoosobowej
        :param player: gracz
        :param index: indek kartydo odrzucenia
        :return: None
        """
        self.seen_deck.insert(0, player.player_cards[index])
        player.remove_card(index)

    def take_new_card(self, player: Player) -> None:
        """
        gracze pobierą karte z góry z talii kart w grze wieloosobowej
        :param player: gracz
        :return: None
        """
        print(f"Nowa karta to: {self.deck.get_card(0)}")
        print("Chcesz tą karte odrzucić czy wymienieć na jedna z swoich kart?")
        print("1. odrzucić")
        print("2. wymienić")
        otp = (int)(input("Wybieram: "))
        print()
        match otp:
            case 1:
                self.seen_deck.insert(0, self.deck.get_card_and_remove(0))
            case 2:
                print("za która karte chcesz wymienić?")
                self.show_stars(player)
                x = (int)(input("numer karty: "))
                while x < 1 or x > player.player_cards_len:
                    print(f"Zły wybór, musisz wybrać między 1 a {player.player_cards_len}")
                    x = (int)(input("numer karty: "))
                change = player.player_cards[x - 1]
                player.player_cards[x - 1] = self.deck.get_card_and_remove(0)
                self.seen_deck[0] = change

    def single_take_new_card(self, player: Player) -> None:
        """
        gracz pobiera karte z góry z talii kart w grze jednoosobowej
        :param player: gracz
        :return: None
        """
        x = 0
        for i in range(player.player_cards_len):
            if self.compare_card_values(self.deck.get_card(0), player.player_cards[i]):
                x = i

        change = player.player_cards[x]
        player.player_cards[x] = self.deck.get_card_and_remove(0)
        self.seen_deck[0] = change

    def take_seen_card(self, player: Player) -> None:
        """
        gracze pobierą karte z góry z talii kart zużytych w grze wieloosobowej
        :param player: gracz
        :return: None
        """
        print(f"karta to: {self.seen_deck[0]}")
        print("za która karte chcesz wymienić?")
        self.show_stars(player)
        x = (int)(input("numer karty: "))
        while x < 1 or x > player.player_cards_len:
            print(f"Zły wybór, musisz wybrać między 1 a {player.player_cards_len}")
            x = (int)(input("numer karty: "))
        change = self.seen_deck[0]
        change2 = player.player_cards[x - 1]
        player.player_cards[x - 1] = change
        self.seen_deck[0] = change2

    def single_take_seen_card(self, player: Player, index: int) -> None:
        """
        gracz pobiera karte z góry z talii kart zużytych w grze jednoosobowej
        :param player: gracz
        :param index: indeks karty
        :return: None
        """
        change = self.seen_deck[0]
        change2 = player.player_cards[index]
        player.player_cards[index] = change
        self.seen_deck[0] = change2

    def suspicion_of_cards(self, list_of_players: List[Player]) -> None:
        """
        daje wybór graczom które dwie karty chcą podejrzeć przy grze wieloosobowej
        :param list_of_players: lista graczy
        :return: None
        """
        print()
        print(Fore.YELLOW + "RUNDA 1" + Style.RESET_ALL)
        print("===============================\n")
        for player in list_of_players:
            print(Fore.CYAN + player.name + Style.RESET_ALL + ", twoja kolej")
            print("- Podejrzyj dwie karty")
            self.show_stars(player)
            print("Wybierz jakie karty chcesz podejrzec")
            x1 = (int)(input("numer pierwszej karty: "))
            while x1 < 1 or x1 > 5:
                print("Zły wybór, musisz wybrać między 1 a 5")
                x1 = (int)(input("numer pierwszej karty: "))
            x2 = (int)(input("numer drugiej karty: "))
            while x2 < 1 or x2 > 5:
                print("Zły wybór, musisz wybrać między 1 a 5")
                x2 = (int)(input("numer drugiej karty: "))
            self.show_cards(player, x1, x2)
            print("===============================\n")

    def single_suspicion_of_cards(self, list_of_players: List[Player]) -> None:
        """
        daje wybór graczowi które dwie karty chce podejrzeć przy grze jednoosobowej z komputerem
        :param list_of_players: lista graczy
        :return: None
        """
        print()
        print(Fore.YELLOW + "RUNDA 1" + Style.RESET_ALL)
        print("===============================\n")
        print(Fore.CYAN + list_of_players[0].name + Style.RESET_ALL + ", twoja kolej")
        print("- Podejrzyj dwie karty")
        self.show_stars(list_of_players[0])
        print("Wybierz jakie karty chcesz podejrzec")
        x1 = (int)(input("numer pierwszej karty: "))
        while x1 < 1 or x1 > 5:
            print("Zły wybór, musisz wybrać między 1 a 5")
            x1 = (int)(input("numer pierwszej karty: "))
        x2 = (int)(input("numer drugiej karty: "))
        while x2 < 1 or x2 > 5:
            print("Zły wybór, musisz wybrać między 1 a 5")
            x2 = (int)(input("numer drugiej karty: "))
        self.show_cards(list_of_players[0], x1, x2)
        print("===============================\n")

    def show_cards(self, player: Player, x1: int, x2: int) -> None:
        """
        Wyświetla dwie wybrane karty gracza
        :param player: gracz
        :param x1: pierwsza karta
        :param x2: druga karta
        :return: None
        """
        for i in range(player.player_cards_len):
            if i == (x1 - 1) or i == (x2 - 1):
                print(f"{i + 1}. {player.player_cards[i]}")
            else:
                print(f"{i + 1}. *")
        print()

    def show_stars(self, player: Player) -> None:
        """
        Wyświetla tyle gwiazdeg ile gracz ma kart
        :param player: gracz
        :return: None
        """
        for i in range(player.player_cards_len):
            print(f"{i + 1}. *")
        print()

    def deal_cards(self, list_of_players: List[Player]) -> None:
        """
        Rozdaje każdemu graczowi z listy po 5 kart
        :param list_of_players: lista graczy
        :return: None
        """
        num_of_cards_per_player = 5
        for player in list_of_players:
            for i in range(num_of_cards_per_player):
                player.add_card(self.deck.get_card_and_remove(0))
        self.seen_deck.insert(0, self.deck.get_card_and_remove(0))

    def save_game(self, list_of_players: List[Player]) -> None:
        """
        Zapisuje wyniki gry do pliku ranking.txt
        :param list_of_players: lista graczy
        :return: None
        """
        game_name = input("Podaj nazwę gry: ")
        file_name = "ranking.txt"

        sorted_players = sorted(list_of_players, key=lambda player: player.points, reverse=False)

        with open(file_name, 'a') as file:
            file.write(Fore.YELLOW + f"Nazwa gry: {game_name}\n" + Style.RESET_ALL)
            file.write(Fore.RED + "===============================\n" + Style.RESET_ALL)
            for player in sorted_players:
                file.write(f"id: {player.id}, name: {player.name}, points: {player.points}\n")
            file.write(Fore.RED + "===============================\n" + Style.RESET_ALL)
            file.write("\n")

        print("Wyniki gry zapisane do rankingu")

    def get_card_valeu_by_index(self, index: int) -> Valeu:
        """
        szuka wartości karty z talii kart zużytych na podstawie podanego indeksu
        :param index:
        :return: wartość karty
        """
        if 0 <= index < len(self.seen_deck):
            return self.seen_deck[index].valeu
        else:
            raise IndexError("Index out of range")

    def count_points(self, list_of_players: List[Player]) -> None:
        """
        Oblicza ilość punktów każdego gracza z listy
        :param list_of_players: lista gtraczy
        :return: None
        """
        for player in list_of_players:
            for i in range(player.player_cards_len):
                if player.get_card_valeu_by_index(i) == Valeu.TWO:
                    player.add_points(2)
                elif player.get_card_valeu_by_index(i) == Valeu.THREE:
                    player.add_points(3)
                elif player.get_card_valeu_by_index(i) == Valeu.FOUR:
                    player.add_points(4)
                elif player.get_card_valeu_by_index(i) == Valeu.FIVE:
                    player.add_points(5)
                elif player.get_card_valeu_by_index(i) == Valeu.SIX:
                    player.add_points(6)
                elif player.get_card_valeu_by_index(i) == Valeu.SEVEN:
                    player.add_points(7)
                elif player.get_card_valeu_by_index(i) == Valeu.EIGHT:
                    player.add_points(8)
                elif player.get_card_valeu_by_index(i) == Valeu.NINE:
                    player.add_points(9)
                elif player.get_card_valeu_by_index(i) == Valeu.TEN:
                    player.add_points(10)
                elif player.get_card_valeu_by_index(i) == Valeu.JACK:
                    player.add_points(11)
                elif player.get_card_valeu_by_index(i) == Valeu.QUEEN:
                    player.add_points(15)
                elif player.get_card_valeu_by_index(i) == Valeu.KING:
                    player.add_points(0)
                elif player.get_card_valeu_by_index(i) == Valeu.ACE:
                    player.add_points(1)

    def winner(self, list_of_players: List[Player]) -> Player:
        """
        Oblicza ilości puknktów wszystkich graczy i ustawia jako wygranego tego który ma ich najmniej.
        :param list_of_players: lista graczy
        :return: zwraca gracza z najmnijesza ilością punktów
        """
        winner = list_of_players[0]
        for player in list_of_players:
            if player.points <= winner.points:
                if player.points == winner.points:
                    if player.num_of_cards < winner.num_of_cards:
                        winner = player
                else:
                    winner = player
        return winner.name

    def compare_card_values(self, card1: Card, card2: Card) -> bool:
        """
        Porównuje wartości kart na podstawie przypisanych do nich wag
        :param card1: pierwsza karta
        :param card2: druga karta
        :return: zwraca true gdy card1 ma mniejszą wartość
        """
        value_to_points = {
            Valeu.TWO: 2,
            Valeu.THREE: 3,
            Valeu.FOUR: 4,
            Valeu.FIVE: 5,
            Valeu.SIX: 6,
            Valeu.SEVEN: 7,
            Valeu.EIGHT: 8,
            Valeu.NINE: 9,
            Valeu.TEN: 10,
            Valeu.JACK: 11,
            Valeu.QUEEN: 12,
            Valeu.KING: 13,
            Valeu.ACE: 14
        }

        if value_to_points[card1.valeu] < value_to_points[card2.valeu]:
            return True
        else:
            return False
