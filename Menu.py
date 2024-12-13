from colorama import Fore, Style

from Game import Game


class Menu:
    def __init__(self):
        self.menu = self.start_menu()

    def start_menu(self) -> None:
        print(Fore.GREEN + "WITAJ W GRZE 'GOLF'" + Style.RESET_ALL)

    def new_game(self) -> None:
        """
        Funkcja wyświetla opcje gry i pozwala użytkownikowi na wybór

        :return: None
        """
        print()
        print(Fore.YELLOW + "wybierz formę gry:" + Style.RESET_ALL)
        print("1. gra jednosobowa")
        print("2. gra wieloosobowa")
        print("3. cofnij")
        opt = input(Fore.BLUE + "Wybieram: " + Style.RESET_ALL)
        game = Game()

        match opt:
            case "2":
                game.multi_player()
                self.show_options()
            case "1":
                game.single_player()
                self.show_options()
            case "3":
                self.show_options()

    def show_options(self) -> None:
        """
        Funcka wyświetla Menu i pozwala użytkownikowi na wybranie jednej z 4 opcji.

        :return: None
        """
        print()
        print(Fore.YELLOW + "wybierz opcje:" + Style.RESET_ALL)
        print("1. nowa gra")
        print("2. zasady gry")
        print("3. pokaz spis rozgrywek")
        print("4. koniec")
        opt = input(Fore.BLUE + "Wybieram: " + Style.RESET_ALL)

        match opt:
            case "1":
                self.new_game()
            case "2":
                self.show_rules()
                print()
                self.show_options()
            case "3":
                self.show_ranking()
                self.show_options()
            case "4":
                pass

    def show_ranking(self) -> None:
        """
        Funcka wyświetla ranking historii gier z pliku ranking.txt.

        :return: None
        """
        print()
        try:
            with open("ranking.txt", 'r') as file:
                content = file.read()
                if content.strip():
                    print(Fore.CYAN + "Spis rozgrywek:" + Style.RESET_ALL)
                    print(content)
                else:
                    print("Ranking jest pusty.")
        except FileNotFoundError:
            print("Plik nie został znaleziony.")

    def show_rules(self) -> None:
        """
        Funkcja wyświetla na konsoli zasady gry z pliku 'Rules.txt'.

        :return: None
        """
        try:
            with open('Rules.txt', 'r') as file:
                lines = file.readlines()
            for line in lines:
                if line.strip().startswith("ZASADY GRY 'Golf'"):
                    print(Fore.GREEN + Style.BRIGHT + line.strip() + Style.RESET_ALL)
                elif line.strip().startswith("Miłej zabawy!"):
                    print(Fore.GREEN + Style.BRIGHT + line.strip() + Style.RESET_ALL)
                elif line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
                    print(Fore.YELLOW + line.strip() + Style.RESET_ALL)
                elif line.strip().startswith(("a.", "b.", "c.", "d.")):
                    print(Fore.CYAN + "\t" + line.strip() + Style.RESET_ALL)
                elif line.strip().startswith("-"):
                    print(Fore.RED + "\t" + line.strip() + Style.RESET_ALL)
                else:
                    print(Fore.WHITE + line.strip() + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "Plik z zasadami nie został znaleziony")
