import swapi
import argparse
from swapi.exceptions import ResourceDoesNotExist
import pytest

def dedup_list(li):
    result_list = []
    for item in li:
        if not item in result_list:
            result_list.append(item)
    return result_list

def species_count_by_film(num):
    #if num >= 1 and num <= 7:
    film_num = swapi.get_film(num)
    species = film_num.get_species()
    list_species_items = species.items
    dedup_list_species_items = dedup_list(list_species_items)
    #print("不同的species有幾個:", len(li_2))
    return len(dedup_list_species_items)

def film_sort_by_episode():
    film_list = []
    for film in swapi.get_all('films').order_by('episode_id'):
        film_list.append(film.title)
    #print(film.title)
    return film_list

def vehicles_speed_over(speed):
    vehicle = swapi.get_all('vehicles')
    vehicle_names = vehicle.items
    vn_list = []
    for vn in vehicle_names:
        if vn.max_atmosphering_speed == 'unknown':
            continue
        if int(vn.max_atmosphering_speed) > speed:
            vn_list.append(vn.name)
            #print(vn.name)
    return vn_list

def demo():
    if num is not None:
        species_count_by_film(num)
    elif speed is not None:
        vehicles_speed_over(speed)
    else:
        film_sort_by_episode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--num', type=int, metavar='<num>',
                        help='which film you want to calculate species')
    parser.add_argument('--sp', type=int, metavar='<sp>',
                        help='max_atmosphering_speed is over')
    parser.add_argument('--sort', help='sort by episode', action='store_true')
    args = parser.parse_args()
    num = args.num
    speed = args.sp

    demo()

class Testdemo:
    def test_film_species_count(self):
        assert species_count_by_film(6) == 20

    def test_film_not_in_range(self):
        with pytest.raises(ResourceDoesNotExist):
            species_count_by_film(8)
        #assert str(e.value) == 'Resource must be 1-7'

    def test_film_sort_by_episode(self):
        assert film_sort_by_episode() == ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith',
                                          'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi',
                                          'The Force Awakens']
    def test_vehicles_speed_over(self):
        assert vehicles_speed_over(1000) == ['T-16 skyhopper', 'TIE/LN starfighter', 'Storm IV Twin-Pod cloud car',
                                             'TIE/IN interceptor', 'Vulture Droid', 'Droid tri-fighter',
                                             'Geonosian starfighter']
