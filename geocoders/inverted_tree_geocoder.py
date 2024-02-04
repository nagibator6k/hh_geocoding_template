import dataclasses

from api import TreeNode, API
from geocoders.geocoder import Geocoder


@dataclasses.dataclass
class InvertedNode:
    name: str
    parent_id: str | None


# Инверсия дерева
class InvertedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    """
        TODO:
        - Сделать функцию, создающую словарь (на основе data)
        [id -> родительская_нода (InvertedNode)] для всех area_id
        - Сделать функцию, создающую словарь (на основе созданного словаря)
        [id -> полный_путь] для всех area_id
    """

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Возвращать данные из словаря с путями
        """
        raise NotImplementedError()
