import soco
print(soco.__version__)
my_zone = soco.SoCo('192.168.1.101')
for i in soco.discover():
    print(i.player_name)