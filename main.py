import numpy as np

def polar_form(z):
    r = np.abs(z)
    phase = np.angle(z, deg=True)
    print("z={}".format(z))
    print('-> z={}(cos{}+isin{})\n'.format(round(r, 2), round(phase, 2), round(phase, 2)))

polar_form(complex(2, 2))
polar_form(complex(np.sqrt(3), -1))
polar_form(complex(-1, np.sqrt(3)))
polar_form(complex(-4, -4*np.sqrt(3)))