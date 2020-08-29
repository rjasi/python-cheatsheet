"""
similar to namedtuple from collections but with updated syntax
"""

from typing import NamedTuple

def example():
    class Car(NamedTuple):
        color: str
        mileage: float
        automatic: bool

    car1 = Car('red', 3812.4, True)
    car1 # Car(color='red', mileage=3812.4, automatic=True)

    # immutable
    car1.color = 5 # error
    
