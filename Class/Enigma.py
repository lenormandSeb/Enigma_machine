class Enigma:
    def __init__(self):
        self.plainMessage = None
        self.plugBoard = {}
        self.rotor_place = []
        self.rotor_position = []
        self.reflector = []

    def set_initial_rotor_place(self, rotor_list, rotor: tuple):
        for r_p in rotor_list.split():
            self.rotor_place.append(rotor.__getitem__(int(r_p)))

    def set_initial_reflector(self, choice, reflector: tuple):
        self.reflector = reflector.__getitem__(int(choice))

    def set_plugin_board(self, plugin_list):
        if self.is_not_valid_plugin(plugin_list):
            raise ValueError('you can not use a letter already swap or have more than 10 pair')

        self.plugBoard = plugin_list.split()

    def is_not_valid_plugin(self, plugins) -> bool:
        used_letter = set()
        for pair in plugins.split():
            for letter in pair:
                if letter in used_letter:
                    return True
                used_letter.add(letter)
        return False

    def set_initial_rotor_position(self, rotor_position):
        for rotor in rotor_position.split():
            self.rotor_position.append(int(rotor))

    def udpate_rotor_position(self):
        if self.rotor_position[2] == 25:
            self.rotor_position[1] = int(self.rotor_position[1]) + 1
            self.rotor_position[2] = 0
        else:
            self.rotor_position[2] = int(self.rotor_position[2]) + 1

        if self.rotor_position[1] == 25:
            self.rotor_position[0] = int(self.rotor_position[0]) + 1
            self.rotor_position[1] = 0

        if self.rotor_position[0] == 25:
            self.rotor_position[0] = 0

    def set_plain_message(self, plain_message: str):
        self.plainMessage = plain_message

    def output_message(self, message: str) -> str:
        output = []
        for letter in message:
            self.udpate_rotor_position()
            letter = self.do_swap_letter(letter)
            for iteration in range(3):
                letter = self.rotor(letter, iteration=iteration)
            letter = self.rotor(letter=letter, reflector=True)
            for iteration in range(3):
                letter = self.rotor(letter=letter, iteration=iteration, revert=True)
            letter = self.do_swap_letter(letter)
            output.append(letter)

        return "".join(output)

    def rotor(self, letter: str, iteration: int = 0, reflector: bool = False, revert: bool = False) -> str:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        rotor_choice = self.rotor_place
        rotor_position = self.rotor_position

        if not revert:
            rotor_choice = self.rotor_place[::-1]
            rotor_position = self.rotor_position[::-1]

        if reflector:
            rotor_choice = [self.reflector]
            rotor_position = [0]

        letter = letter.upper()

        if alphabet.index(letter) + int(rotor_position[iteration]) > 25 and not revert:
            return rotor_choice[iteration][alphabet.index(letter) + int(rotor_position[iteration]) - 26]

        if revert:
            return alphabet[rotor_choice[iteration].index(letter) - int(rotor_position[iteration])]
        return rotor_choice[iteration][alphabet.index(letter) + int(rotor_position[iteration])]

    def do_swap_letter(self, letter: str) -> str:
        for plug in self.plugBoard:
            if letter.upper() == plug[0]:
                return plug[1]
            if letter.upper() == plug[1]:
                return plug[0]
        return letter
