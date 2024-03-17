from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.memory = {}

        for country in self.__data:
            for area in country.areas:
                for sity in area.areas:
                    self.memory[sity.id] = f"{country.name} {area.name} {sity.name}"
                self.memory[area.id] = f"{country.name} {area.name}"
            self.memory[country.id] = f"{country.name}"


    def _apply_geocoding(self, area_id: str) -> str:
        area_id = str(area_id)
        return self.memory.get(area_id, 'Что-то пошло не так')