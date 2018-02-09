## Generate GIF By Matplotlib

Under this directory, you can download these files and run it, then you will find how it works by reading these easy code and consider running results. before you run it, please make sure you have installed `numpy`, `matplotlib ` and `ImageMagick` lib in your runing environment.

But I want to make a simple introduce for you. there are two ways to draw graph with `matplotlib.animation`. 

one is update coordinates when to plot next frame.

```
fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)

line, = ax.plot(x, np.sin(x))

def init():
    line.set_ydata(np.sin(x))
    return line,

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,

animation = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
```

a trap is you must name plot graph with comma end. In above example, the name is `line,`

![](https://raw.githubusercontent.com/mk43/python-practice/master/matplotlib/generateGIF/resetvalue.gif)

another way is clean the front frame and plot the next frame on. In short, It's redraw the graph.

```
fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)

def init():
    return ax.plot(x, np.sin(x))

def animate(i):
    try:
        ax.lines.pop(1)
    except Exception:
        pass
    line = ax.plot(x, np.sin(x + i / 10.0), 'r')
    return line,

animation = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
```

this way has no more limitations, you can do what you want freely.

![](https://raw.githubusercontent.com/mk43/python-practice/master/matplotlib/generateGIF/redraw.gif)

I provide a machine learning demo by using liner regression to simulate linear function. you can help yourself understand it by reading source code I posted.

[see more](http://fitzeng.org/2018/02/08/MatplotlibGenerateGif/)


![](https://raw.githubusercontent.com/mk43/python-practice/master/matplotlib/generateGIF/linearregression.gif)

![](https://raw.githubusercontent.com/mk43/python-practice/master/matplotlib/generateGIF/linearregression.png)