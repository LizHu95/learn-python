import pizza
pizza.makePizza(16, "pepperoni")
pizza.makePizza(12, "mushrooms","green peppers")

import pizza as p
p.makePizza(16, "pepperoni")
p.makePizza(12, "mushrooms","green peppers")

from pizza import makePizza
# from pizza import * 
makePizza(16, "pepperoni")
makePizza(12, "mushrooms","green peppers")

from pizza import makePizza as mp
mp(16, "pepperoni")
mp(12, "mushrooms","green peppers")