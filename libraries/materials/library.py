materials = dict()


class Material:
    def __init__(self, name, strength, density, weld):
        self.params = {'sigma_v': strength * 9800000,
                       'density': density,
                       'weld': weld}

        self.name = name
        self.strength = strength * 9800000
        self.density = density
        self.weld = weld


def add_material(name, strength, density, weld):
    materials[name] = Material(name, strength, density, weld)


"""
КОНСТРУКЦИОННЫЕ СТАЛИ
"""
add_material('ВКС-210', 195, 8010, 0.92)
add_material('30ХГСА', 160, 7770, 0.95)
add_material('ЭИ643', 190, 7810, 0.92)
add_material('КВК-26', 140, 7870, 0.9)
add_material('КВК-42', 190, 7870, 0.9)

"""
ЖАРОПРОЧНЫЕ И КОРРОЗИОННОСТОЙКИЕ
"""
add_material('12Х18Н9', 56, 7920, 0.95)
add_material('17Х18Н9', 60, 7850, None)
add_material('12Х18Н9Т', 85, 7900, 0.96)
add_material('07Х16Н6', 110, 7750, 0.92)

"""
ТИТАНОВЫЕ
"""
add_material('ВТ-1-00', 47, 4500, 0.9)
add_material('ВТ-9', 140, 4510, 0.9)

