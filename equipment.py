from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: int
    stamina_per_turn: int


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:
    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        return [w for w in self.equipment.weapons if w.name == weapon_name][0]

    def get_armor(self, armor_name) -> Optional[Armor]:
        return [a for a in self.equipment.armors if a.name == armor_name][0]

    def get_weapons_names(self) -> list:
        return [w.name for w in self.equipment.weapons]

    def get_armors_names(self) -> list:
        return [a.name for a in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> Optional[EquipmentData]:
        equipment_file = open("./data/equipment.json", encoding="utf-8")
        data = json.load(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        return equipment_schema().load(data)
