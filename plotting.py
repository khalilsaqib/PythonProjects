from FACE_DETECTION_IN_VIDEO import df
from bokeh.plotting import figure ,show,output_file
from bokeh.models import HoverTool,ColumnDataSource
from datetime import datetime as dt
df["S_String"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["E_String"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)
p=figure(x_axis_type='datetime',height=500,width=600,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@S_String"),("End","@E_String")])
p.add_tools(hover)
q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("MOTION GRAPH.html")
show(p)
