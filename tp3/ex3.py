def convertion_temps(h, m, s):
    return h * 3600 + m * 60 + s


def temps_ecoule(h1, m1, s1, h2, m2, s2):
    return abs(convertion_temps(h1, m1, s1) - convertion_temps(h2, m2, s2))


def convertion_distance(km, m, cm):
    return m + km * 1000 + cm / 100


def vitesse(km, m, cm, h, min, s):
    return convertion_distance(km, m, cm) / convertion_temps(h, min, s)
