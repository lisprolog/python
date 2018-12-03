'''
empireofcode.com

this code makes sure that the troops aim at a single target.
'''
from battle import commander
from battle import ROLE
unit_client = commander.Client()

def nearest_enemy(data=None, **kwargs):
    towers = unit_client.ask_towers()
    if towers:
        near_tower = unit_client.ask_nearest_enemy([ROLE.TOWER])
        print("near_tower: "+str(near_tower));
        tower_id = near_tower["id"];
        print("tower_id: " + str(tower_id));
        unit_client.do_attack(tower_id);
        unit_client.when_item_destroyed(tower_id, nearest_enemy);
    else:
        print("attack_center: else");
        attack_center()
def attack_center(data=None, **kwargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
nearest_enemy()
