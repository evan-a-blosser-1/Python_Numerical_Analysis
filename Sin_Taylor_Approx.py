import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)


terms = [1, 3, 5, 7, 9]
def taylor(x, terms=10):
    """ This calcualtes the appproximation of a sine wave, by term
    """
    y = np.zeros(len(x))
    for n in range(terms):
        y += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return y

plt.figure(figsize=(10,8))
for n in terms:
    print(n)
    y = taylor(x, terms=n)
    label = f'{n} Terms'
    plt.plot(x,y, label=label)
    
plt.plot(x,np.sin(x), color='black', label='Actual Sine Wave',linestyle='dashed')
plt.title('Taylor Series Approximation of Sine Wave')
plt.xlabel(r'$x$', fontsize=24)
plt.ylabel(r'$y$', fontsize=24)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid()
plt.show()

