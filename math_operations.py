import math

DELTA = 24

# Over Rate calculation
def over_rate(DVDI, DI):
    overRate = DVDI * (math.pow((DI + 1), 1/252) - 1)
    return overRate

# Fair Price calculation
def fair_price(overRate, USDBRL):
    fairPRice = ((USDBRL * overRate) / 100 ) + USDBRL
    return fairPRice

# Opening calculation
def opening(DOLFUT, USDX):
    openingPrice = ((DOLFUT * USDX) / 100) + DOLFUT
    return openingPrice

# Maximum Opening first hour price calculation
def max_opening(openingPrice, overRate, DELTA):
    maxOpen = ((openingPrice * overRate) / 100) + openingPrice + DELTA
    return maxOpen

# Minimum Opening first hour price calculation
def min_opening(maxOpen, DELTA):
    minOpen = maxOpen - (2 * DELTA)
    return minOpen
