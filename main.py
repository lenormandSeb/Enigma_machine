from Class.Enigma import Enigma
from Class.Rotors import Rotor
from Class.Reflector import Reflector

enigma = Enigma()

rotor_list = Rotor.get_rotor_list()
reflector_list = Reflector.get_reflector_list()

print('Choose rotor position between those (rotor are place from right to left):')
for index, a in enumerate(rotor_list):
    print('{0} : {1}'.format(index, a))
rotor_place = input('Enter order with whitespace : ')
enigma.set_initial_rotor_place(rotor_place, rotor_list)

print('Choose rotor position between those (rotor are place from right to left):')
for index, a in enumerate(reflector_list):
    print('{0} : {1}'.format(index, a))
reflector_choice = input('Enter order with whitespace : ')
enigma.set_initial_reflector(reflector_choice, reflector_list)

plugin = input('Enter your pair to swap key with whitespace, 10 pair max (example : AE IO BD) : ')
enigma.set_plugin_board(plugin)

rotor_pos = input('Enter 3 position of rotor between 0 and 25 separate by whitespace, one for each : ')
enigma.set_initial_rotor_position(rotor_pos)

message = input('Enter your message without whitespace : ')

print(enigma.output_message(message))
