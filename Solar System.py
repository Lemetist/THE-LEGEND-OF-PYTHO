from math import pi
from random import choice as ch

planets = {
 2440: 'Mercury',
 6052: 'Venus',
 6371: 'Earth',
 3390: 'Mars',
 58232: 'Saturn'
}

print(ch(list(planets.values())))