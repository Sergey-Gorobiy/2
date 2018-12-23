from room_module import Room

r1 = Room(float(input('Please enter the width of the room - ')), float (input('The lenght - ')), float (input('And the height - ')))
print('The full square of the room is ', round(r1.fullSquare (), 2))  # выведет 48.6
r1.addWD(float(input('Add the width of the window/door - ')), float (input('And the height - ')))
while input('If you need to add one more window/door, press - 1. Else - press any other key ') == '1':
	r1.addWD(float(input('Add the width of the window/door - ')), float(input('And the height - ')))
print('The work surface square is', round (r1.workSurface(), 2))  # выведет 44.6
print(r1.numberOfwallpapers (float (input('To know the needed number of wallpapers, enter the width of one wallpaper - ')), float (input('And the lenght - '))))