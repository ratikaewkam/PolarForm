import numpy as np
import matplotlib.pyplot as plt

def plot(z):
    real = z.real
    imag = z.imag

    # Create vectors
    X = np.array([real, 0])
    Y = np.array([0, imag])
    V = np.array([real, imag])

    # Create the plot
    fig, ax = plt.subplots()

    # Add the vectors (V, X, and Y) to the plot
    ax.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='g')
    ax.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='b')
    
    # Set the x-limits and y-limits of the plot
    ax.set_xlim([real-5, real+5])
    ax.set_ylim([imag-5, imag+5])
    
    # Show the plot along with the grid
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def polar_form(z):
    r = np.abs(z)
    phase = np.angle(z, deg=True)
    print("z={}".format(z))
    print('-> z={}(cos{}+isin{})\n'.format(round(r, 2), round(phase, 2), round(phase, 2)))

    # Plot the vectors
    plot(z)

polar_form(complex(2, 2))
polar_form(complex(np.sqrt(3), -1))
polar_form(complex(-1, np.sqrt(3)))
polar_form(complex(-4, -4*np.sqrt(3)))