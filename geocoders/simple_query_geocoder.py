from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        node = API.get_area(area_id)
        adress = node.name

        if node.parent_id is None:  # Если страна попадается сразу
            return adress

        while node := API.get_area(node.parent_id):

            adress = node.name + ' ' + adress

            if node.parent_id is None:
                break

        return adress


