import pytest
from swapi.exceptions import ResourceDoesNotExist
import demo

class Testdemo:
    def test_film_species_count(self):
        assert demo.species_count_by_film(6) == 20


    def test_film_not_in_range(self):
        with pytest.raises(ResourceDoesNotExist):
            demo.species_count_by_film(8)


    def test_film_sort_by_episode(self):
        assert demo.film_sort_by_episode() == ['The Phantom Menace',
                                               'Attack of the Clones',
                                               'Revenge of the Sith',
                                               'A New Hope',
                                               'The Empire Strikes Back',
                                               'Return of the Jedi',
                                               'The Force Awakens']


    def test_vehicles_speed_over(self):
        assert demo.vehicles_speed_over(1000) == ['T-16 skyhopper',
                                                  'TIE/LN starfighter',
                                                  'Storm IV Twin-Pod cloud car',
                                                  'TIE/IN interceptor',
                                                  'Vulture Droid',
                                                  'Droid tri-fighter',
                                                  'Geonosian starfighter']
