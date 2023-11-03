from Class.Enigma import Enigma
from Class.Rotors import Rotor
from Class.Reflector import Reflector

enigma = Enigma()

print('Choose rotor position between those (rotor are place from right to left):')
print(*(f'{rotor.name} : {rotor.value}' for rotor in Rotor), sep='\n')
rotor_place = input('Enter order with whitespace : ')
enigma.set_initial_rotor_place(rotor_place, Rotor)

print('Choose rotor position between those (rotor are place from right to left):')
print(*(f'{reflector.name} : {reflector.value}' for reflector in Reflector), sep='\n')
reflector_choice = input('Enter order with whitespace : ')
enigma.set_initial_reflector(reflector_choice, Reflector)

plugin = input('Enter your pair to swap key with whitespace, 10 pair max (example : AE IO BD) : ')
enigma.set_plugin_board(plugin)

rotor_pos = input('Enter 3 position of rotor between 0 and 25 separate by whitespace, one for each : ')
enigma.set_initial_rotor_position(rotor_pos)

message = input('Enter your message without whitespace : ')
print(enigma.output_message(message))
