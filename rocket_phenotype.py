# Rocket engine phenotype
import random
from libraries.fuels.solid import database as fuels_db
import pandas as pd
import matplotlib.pyplot as plot
from libraries.materials import library
from dna import genify
import math
import random

random.seed(7)

fuels = dict()
materials = dict()
packings = [7, 12]


def add_fuel(name):
    fuels[name] = fuels_db.data[name]


def add_material(name):
    materials[name] = library.materials[name]

"""
Список топлив
"""
add_fuel('MGP')
add_fuel('NM-2')
add_fuel('SC')

add_fuel('PCA-1')
add_fuel('PCA-2')

add_fuel('PCA-3М')
add_fuel('PCA-4М')
add_fuel('PCA-5М')
add_fuel('PCA-6М')
add_fuel('PCA-7М')
add_fuel('PCA-8М')
add_fuel('PCA-9М')

add_fuel('PCK-1М')
add_fuel('PCL-1')
add_fuel('PCL-2М')
add_fuel('PCL-3М')
add_fuel('PCN-1М')
add_fuel('PCN-2М')
"""
КОНСТРУКЦИОННЫЕ СТАЛИ
"""
add_material('Steel 210')
add_material('Steel 30')
add_material('Steel 643')
add_material('Steel 26')
add_material('Steel 42')

"""
ЖАРОПРОЧНЫЕ И КОРРОЗИОННОСТОЙКИЕ
"""
add_material('Steel 12')
add_material('Steel 12T')
add_material('Steel 07')

"""
ТИТАНОВЫЕ
"""

            # new_population.append(Rocket(pressure, fuel, material, tau, packing))

class Rocket:
    def __init__(self, dna):# pressure, fuel, material, tau, packing=7, n=1.5):
        """

        :param pressure:
        :param fuel:
        :param packing:
        """

        '''
        НАЧАЛЬНЫЕ ПАРАМЕТРЫ
        '''
        self.dna = dna

        self.params = {'pressure': genify(range(4, 30), self.dna.genes[0]),
                       'fuel': genify(list(fuels.values()), self.dna.genes[1]),
                       'material': genify(list(materials.values()), self.dna.genes[2]),
                       'tau': genify([i / 10 for i in range(1, 15)], self.dna.genes[3]),
                       'packing': genify(packings, self.dna.genes[4])
                       }
        self.fullness = 0.5
        self.i_sum = 1275  # Н*с/ Суммарный импульс
        self.chamber_pressure = self.params['pressure'] * 1000000  # МПа, Давление в камере
        self.fuel = self.params['fuel']  # Тип топлива
        self.toc, self.isp = self.fuel.model.expression(self.chamber_pressure)  # К, м/с, Температура в камере и удельный импульс
        self.isp = self.isp * 9.8
        self.tau = self.params['tau']  # с, Время работы
        self.n = 1.1 * 1.35
        self.material = self.params['material']

        self.starting_params = {'_i_sum': 1275,
                                '_p_oc': self.chamber_pressure,
                                '_isp': self.isp,
                                '_tau': self.tau,
                                '_n': self.n,
                                '_weld': self.material.weld,
                                '_mdensity': self.material.density,
                                '_strength': self.material.strength,
                                '_toc': self.toc,
                                '_betta': self.fuel.B,
                                '_fdensity': self.fuel.density,
                                '_u0': self.fuel.linear_speed,
                                '_v': self.fuel.v}
        '''
        ПРИБЛИЖЕНИЯ
        '''

        '''
        ПЕРВИЧНЫЕ РАСЧЕТЫ
        '''
        self.P = self.i_sum / self.tau
        self.mass_flow = self.P / self.isp
        self.mass_fuel = self.mass_flow * self.tau

        self.u = self.fuel.linear_speed * pow(self.chamber_pressure / 98066.5, self.fuel.v)
        self.e = self.u * 0.001 * self.tau

        self.f_min = self.fuel.B * self.mass_flow / self.chamber_pressure
        self.d_min = math.sqrt(4 * self.f_min / math.pi)
        self.f_ch = 4 * self.f_min  # мм, Диаметр канала
        self.d_ch = math.sqrt(4 * self.f_ch / math.pi)
        self.per_ch = self.d_ch * math.pi

        self.d_fuel = 2 * self.e + self.d_ch
        self.d_shell = self.pack(self.params['packing'], self.d_fuel)

        self.length = self.mass_flow / (self.fuel.density * self.u * 0.001 * self.per_ch)

        self.delta_shell = self.chamber_pressure * self.d_shell * self.n / (2 * self.material.weld * 0.8 * self.material.strength)

        self.f_out = pow(self.d_shell + 2 * self.delta_shell, 2) * math.pi / 4
        self.f_in = pow(self.d_shell, 2) * math.pi / 4

        self.vol_shell = self.length * (self.f_out - self.f_in)
        self.mass_shell = self.vol_shell * self.material.density

        self.LD = self.length / self.d_shell

        self.final_params = {'P': round(self.P / 9.8, 1),
                      'Ro': round(self.fuel.density),
                      'e': round(self.e, 4),
                      'Dmin': round(self.d_min, 3),
                      'Dsh': round(self.d_shell, 3),
                      'G': round(self.mass_flow, 2),
                      'u': round(self.u, 1),
                      'dz': round(self.d_fuel, 3),
                      'L': round(self.length, 3),
                      'delta': round(self.delta_shell, 3),
                      'mass': round(self.mass_shell, 1),
                      'full_mass': round(self.mass_shell + self.mass_fuel, 1)}

    def show_params(self):
        dictionary = {'P': round(self.P / 9.8, 1),
                      'p': round(self.chamber_pressure / 1000000),
                      'Ro': round(self.fuel.density),
                      'e': round(self.e, 4),
                      'Toc': round(self.toc, 1),
                      'Isp': round(self.isp, 1),
                      'Dmin': round(self.d_min, 3),
                      'Dsh': round(self.d_shell, 3),
                      'G': round(self.mass_flow, 2),
                      'pack': round(self.params['packing']),
                      'u': round(self.u, 1),
                      'tau': round(self.tau, 2),
                      'u0': round(self.fuel.linear_speed, 2),
                      'v': round(self.fuel.v, 2),
                      'dz': round(self.d_fuel, 3),
                      'L': round(self.length, 3),
                      'delta': round(self.delta_shell, 3),
                      'mat_name': self.material.name,
                      'fuel_name': self.fuel.name,
                      'mass': round(self.mass_shell, 1),
                      'full_mass': round(self.mass_shell + self.mass_fuel, 1)}
        return dictionary

    def pack(self, num, d):
        if num == 12:
            self.fullness = 1
            return d * 4.055
        elif num == 7:
            self.fullness = 0
            return d * 3
        return None
