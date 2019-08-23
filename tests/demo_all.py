import swapi
import argparse
from swapi.exceptions import ResourceDoesNotExist
import pytest

    #去除重複的species
def dedup_list(li):
    result_list=[]
    for item in li:
        if not item in result_list:
            result_list.append(item)
    return result_list
	    
    #species數量
def species_count_by_film(num):
    try:
        film_num = swapi.get_film(num)
        species = film_num.get_species()
        li_1 = species.items
        li_2 = dedup_list(li_1)
        print("不同的species有幾個:", len(li_2))
    except ResourceDoesNotExist:
        print("No such film")

    #根據episode排序film_name
def film_sort_by_episode():
    for film in swapi.get_all("films").order_by("episode_id"):
        print(film.title)

    #列出超過speed的vehicles
def vehicles_speed_over(sp):
    vehicle = swapi.get_all("vehicles")
    vehicle_name = vehicle.items
    for vn in vehicle_name:
        try:
            if int(vn.max_atmosphering_speed) > sp:
                print(vn)
        except ValueError:
            print(vn, "的max_atmosphering_speed不是數字")
                
def demo():
    if num is not None:
        species_count_by_film(num)
    elif sp is not None:
        vehicles_speed_over(sp)
    else:
        film_sort_by_episode()

if __name__=='__main__':
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
    sp = args.sp

    demo()