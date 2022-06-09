import numpy as np
import PIL
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    y1 = np.sin(3.5 * np.pi * (x - i))
    y2 = y1 + y
    line.set_data(x, y2)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
anim.save('D:\\PycharmProjects\\Визуалайзер\\Saves\\1.gif', writer='imagemagick', fps=30)

plt.show()