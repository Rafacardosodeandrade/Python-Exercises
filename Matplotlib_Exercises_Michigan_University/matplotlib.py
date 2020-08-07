import matplotlib as mpl 
mpl.get_backend()

#pyplot is scripting layer - simplifies access to the artist and backend layers

#backend use
from matplotlib.backends,backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
