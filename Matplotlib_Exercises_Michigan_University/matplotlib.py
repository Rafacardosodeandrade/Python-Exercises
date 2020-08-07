import matplotlib as mpl 
mpl.get_backend()

#pyplot is scripting layer - simplifies access to the artist and backend layers

#backend use
from matplotlib.backends,backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.ass_subplot(111)
ax.plot(3,2,'.')
canvas.print_png('test.png')
%%html 
< img src = 'test.png' />

# another example
plt.figure()
plt.plot(3,2,'o')
ax = plt.gca()
ax.axis([0,6,0,10]) # here we use 4 parameters

# another example with multi points.
plt.figure()
plt.plot(1.5,1.5,'o')
plt.plot(2,2,'o')
plt.plot(2.5,2.5.'o')



