# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:13:51 2020
Edited on Thurs Jul 21, 2022

@author: jburdick
@author: nlany
"""

# -*- coding: utf-8 -*-
#import packages
# import os
# import shutil
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import pathlib
from dash.dependencies import Input, Output
from datetime import datetime, timedelta
from scipy import signal
import ssl
import os
import getpass
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot


ssl._create_default_https_context = ssl._create_unverified_context

#point to data locations
user = getpass.getuser()
#point to folder with sample Marcell Experimental Forest Data. Preliminary unpublished, unreviewed raw datalogger files
dir_work = 'C:\\Users\\'+ user + '\\Box\\01. jacob.burdick Workspace\\MEF_items\\Scripts\\MEF_dashboard\\data'
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("data").resolve()
DATA_PATH = pathlib.Path(dir_work)

#read in check measurements
# check_df = pd.read_csv(dir_work + '\\check_measurements.csv', parse_dates=[['Date', 'Time']])
# check_df = check_df.dropna(subset = ['Measurement'])
# check_df = check_df.rename(columns = {'Date_Time': 'datetime'})
# check_df['datetime'] = pd.to_datetime(check_df['datetime'], format = '%m/%d/%Y %H%M')
# check_df = check_df.drop(columns = ['Notes'])



#Bogwell plots
#read Bogwell .dat files in using pandas library.  Skip program info row and other rows with abbreviated info. 
blf_wt = pd.read_csv(DATA_PATH.joinpath('BLF_met_BogLakeW.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s1_wt = pd.read_csv(DATA_PATH.joinpath('S1-EM3_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s2_wt = pd.read_csv(DATA_PATH.joinpath('S2bog_S2BW.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s3_wt = pd.read_csv(DATA_PATH.joinpath('S3_fenwell_S3FW.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s4_wt = pd.read_csv(DATA_PATH.joinpath('S4_bogwell_S4BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), engine = 'python', parse_dates = True)
s5_wt = pd.read_csv(DATA_PATH.joinpath('S5_bogwell_S5BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), engine = 'python', parse_dates = True)
s6_wt = pd.read_csv(DATA_PATH.joinpath('S6_bogwell_S6BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), parse_dates = True)


#call plotly figure object.  One figure for all bogwells. Each fig.add_trace adds new site
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=list(blf_wt.TIMESTAMP), y=list(blf_wt.WT_Elev), name = 'BLF_WTelev', showlegend = True, connectgaps=False))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'BLF'].datetime), 
#                y = list(check_df[check_df['Site'] == 'BLF'].Measurement), 
#                name = 'BLF_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'))
#     )
fig.add_trace(
    go.Scatter(x=list(s1_wt.TIMESTAMP), y=list(s1_wt.WT_Elev), name = 'S1_WTelev', showlegend=True, connectgaps=False, yaxis = 'y2'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S1_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S1_BW'].Measurement), 
#                name = 'S1_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y2')
    # )
fig.add_trace(
    go.Scatter(x=list(s2_wt.TIMESTAMP), y=list(s2_wt.WTElev), name = 'S2_WTelev', showlegend=True, connectgaps=False, yaxis = 'y3'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S2_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S2_BW'].Measurement), 
#                name = 'S2_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y3')
#     )
fig.add_trace(
    go.Scatter(x=list(s3_wt.TIMESTAMP), y=list(s3_wt.WTElev), name = 'S3_WTelev', showlegend=True, connectgaps=False, yaxis = 'y4'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S3_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S3_BW'].Measurement), 
#                name = 'S3_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y4')
#     )
fig.add_trace(
    go.Scatter(x=list(s4_wt.TIMESTAMP), y=list(s4_wt.WTElev), name = 'S4_WTelev', showlegend=True, connectgaps=False, yaxis = 'y5'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S4_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S4_BW'].Measurement), 
#                name = 'S4_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y5')
#     )
fig.add_trace(
    go.Scatter(x=list(s5_wt.TIMESTAMP), y=list(s5_wt.WTElev), name = 'S5_WTelev', showlegend=True, connectgaps=False, yaxis = 'y6'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S5_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S5_BW'].Measurement), 
#                name = 'S5_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y6')
#     )
fig.add_trace(
    go.Scatter(x=list(s6_wt.TIMESTAMP), y=list(s6_wt.WTElev), name = 'S6_WTelev', showlegend=True, connectgaps=False, yaxis = 'y7'))
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S6_BW'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S6_BW'].Measurement), 
#                name = 'S6_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'),
#                yaxis = 'y7')
#     )

#tweak interactive hover info, asthetics 
plot_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
graph_bg = "#082255"

fig.update_traces(
    hoverinfo="y+x+name"
    )
fig.update_layout(
    height=600,
    #width = 1200,
    margin = dict(l=80),
    template="seaborn",
    title_text="Peatland water table elevations",
    #paper_bgcolor= graph_bg,
    #plot_bgcolor= graph_bg
)

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig.update_layout(
    yaxis_title="Y Axis Title",
    xaxis=dict(
        domain=[0, 1]
    ),
    yaxis=dict(
    ),
    yaxis2=dict(
        overlaying="y",
        range = [1351,1353]
    ),
    yaxis3=dict(
        overlaying="y",
    ),
    yaxis4=dict(
        overlaying="y",
    ),
    yaxis5=dict(
        overlaying="y",
    ),
    yaxis6=dict(
        overlaying="y",
    ),
    yaxis7=dict(
        overlaying="y",
    ),      
)

fig.update_yaxes(visible=False, showticklabels=False)
fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': 'Water table elevation (ft)',
    'textangle' : -90,
    'x': 0.02,
    'xshift' : -60,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.6,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

# #display last year of values
# x_max = datetime.now()
# x_min = x_max - timedelta(days = 90)
x_min = '2021-07-01'
x_max = '2022-07-12'
fig.update_xaxes(range = [x_min, x_max])

# fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/bogwells.html')
print('updated bogwell figure')

#rename
fig_2 = fig
#plot(fig_2)



###
#####
#Streamflow plots. S5 should be added in.  S4N appending workflow needs updating
s2_Q = pd.read_csv(DATA_PATH.joinpath('S2_Weir_S2Streamflow.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s4N_Q = pd.read_csv(DATA_PATH.joinpath('S4N_weir_S4NStreamflow.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s6_Q = pd.read_csv(DATA_PATH.joinpath('S6_Weir_S6Streamflow.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
s5_Q = pd.read_csv(DATA_PATH.joinpath('S5_Weir_S5Streamflow.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#call plotly figure object
fig = make_subplots(rows = 1, cols = 1, shared_xaxes=True)

#add streamflow traces for each site
fig.add_trace(
    go.Scatter(x=list(s2_Q.TIMESTAMP), y=list(s2_Q.Stage), name = 'S2', showlegend = True, connectgaps=False), row = 1, col = 1)
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S2_weir'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S2_weir'].Measurement), 
#                name = 'S2_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'))
#     )
fig.add_trace(
    go.Scatter(x=list(s4N_Q.TIMESTAMP), y=list(s4N_Q.Stage), name = 'S4N', showlegend = True, connectgaps=False), row = 1, col = 1)
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S4N_weir'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S4N_weir'].Measurement), 
#                name = 'S4N_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'))
#     )
fig.add_trace(
    go.Scatter(x=list(s6_Q.TIMESTAMP), y=list(s6_Q.Stage), name = 'S6', showlegend = True, connectgaps=False), row = 1, col = 1)
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S6_weir'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S6_weir'].Measurement), 
#                name = 'S6_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'))
#     )
fig.add_trace(
    go.Scatter(x=list(s5_Q.TIMESTAMP), y=list(s5_Q.Stage), name = 'S5', showlegend = True, connectgaps=False), row = 1, col = 1)
# fig.add_trace(
#     go.Scatter(x = list(check_df[check_df['Site'] == 'S5_weir'].datetime), 
#                y = list(check_df[check_df['Site'] == 'S5_weir'].Measurement), 
#                name = 'S5_checks', showlegend = True, connectgaps = False, 
#                mode = 'markers', marker=dict(color='red', symbol = 'asterisk-open'))
#     )
#plot(fig)

fig.update_traces(
    hoverinfo="y+x+name"
    )
fig.update_layout(
    height=500,
    #width = 1200,
    margin = dict(l=80),
    template="seaborn",
    title = 'Streamflow (stage ft)',
)

#fig.update_yaxes(range=[-0.2, .75], row = 1, col = 1)
##display last 90 days
# x_max = datetime.now()
# x_min = x_max - timedelta(days = 90)
# fig.update_xaxes(range = [x_min, x_max])
fig.update_yaxes(range = [0,0.85])

fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': 'Streamflow (stage ft)',
    'textangle' : -90,
    'x': 0,
    'xshift' : -60,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.5,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/streamflow.html')
print('updated streamflow figure')
# hide range selectors
#rename
fig_3 = fig
#plot(fig_3)



###
#####
#PPT Plots
#North
df = pd.read_csv(DATA_PATH.joinpath('NorthWx_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df = df.set_index('TIMESTAMP')
df = df.resample('D').sum()
df.reset_index(inplace = True)

#call plotly figure object with x sublots
fig = make_subplots(rows = 3, cols = 1, vertical_spacing=.05, shared_xaxes=True, subplot_titles=('NorthWx_NOAH', 'NADP_NOAH', 'South_Wx_Noah'))
#add ppt trace
fig.add_trace(
    go.Bar(x=list(df.TIMESTAMP), y=list(df.ReportPCP), name = 'North NOAH', showlegend = False), row = 1, col = 1)

#NADP
df = pd.read_csv(DATA_PATH.joinpath('NADP_NOAH_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df = df.set_index('TIMESTAMP')
df = df.resample('D').sum()
df.reset_index(inplace = True)
#create copy of NADP dataframe for use with context plot
df_NADP = df.copy()

#add ppt traces
fig.add_trace(
    go.Bar(x=list(df.TIMESTAMP), y=list(df.ReportPCP), name = 'NADP NOAH', showlegend = False), row = 2, col = 1)

#South
df = pd.read_csv(DATA_PATH.joinpath('South_Wx_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df = df.set_index('TIMESTAMP')
df = df.resample('D').sum()
df.reset_index(inplace = True)

#add ppt traces
fig.add_trace(
    go.Bar(x=list(df.TIMESTAMP), y=list(df.ReportPCP), name = 'South NOAH', showlegend = False), row = 3, col = 1)

fig.update_traces(
    hoverinfo="y+x"
    )
fig.update_layout(
    height=900,
    #width = 1200,
    template="seaborn",
    title_text="Precipitation",
)

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': 'rainfail/SWE (inches)',
    'textangle' : -90,
    'x': 0,
    'xshift' : -50,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.5,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

#update x axis to display last n days of data, y axis to show reasonable range
fig.update_yaxes(range=[0, 1.8])
# x_max = datetime.now()
# x_min = x_max - timedelta(days = 90)
x_max = df.TIMESTAMP.iloc[-1]
x_min = x_max - timedelta(days = 90)
fig.update_xaxes(range = [x_min, x_max])

fig.update_layout(
    xaxis2 = dict(
        rangeselector = dict(
            visible = False))
    )

fig.update_layout(
    xaxis3 = dict(
        rangeselector = dict(
            visible = False))
    )

#fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/precipitation.html')
print('updated precip figure')
#plot(fig)
fig_4 = fig
#plot(fig_4)





###
#####
#Soil Temp plots. Update to require less lines to read in data.
#read NADP_aspen .dat file in as df using pandas module.  Skip program info row and other rows with abbreviated info.  Set header to proper row. engine = python needed not sure why though.  Parse dates.
df = pd.read_csv(DATA_PATH.joinpath('NADP_aspen_temp_AspenSoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#call plotly figure object with 2 sublots: 2 rows one column
fig = make_subplots(rows = 4, cols = 2, subplot_titles = ('NADP Aspen', 'S3','NADP Open','S4', 'Junction Fen','S5','S2','S6'), vertical_spacing=.06, shared_xaxes=True)

#add traces for aspen temps
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', connectgaps=False), row = 1, col = 1)

#read NADP_open .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('NADP_open_temp_OpenSoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 2, col = 1)

#read junction fen soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('Junction_fen_JFSoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 3, col = 1)

#read S2 soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('S2_bogwell_S2SoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 4, col = 1)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 4, col = 1)

#read S3 soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('S3_fenwell_S3SoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 1, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 1, col = 2)

#read S4 soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('S4_bogwell_S4SoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 2, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 2, col = 2)

#read S5 soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('S5_bogwell_S5SoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 3, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 3, col = 2)

#read S6 soil temp .dat file in as df using pandas
df = pd.read_csv(DATA_PATH.joinpath('S6_bogwell_S6SoilTemp.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#add open temp traces to second subplot
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_5), name = '5cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_10), name = '10cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_20), name = '20cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_30), name = '30cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_40), name = '40cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_50), name = '50cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_100), name = '100cm', showlegend=False, connectgaps=False), row = 4, col = 2)
fig.add_trace(
    go.Scatter(x=list(df.TIMESTAMP), y=list(df.SoilT_200), name = '200cm', showlegend=False, connectgaps=False), row = 4, col = 2)

#tweak interactive hover info and figure size and asthetics 
fig.update_traces(
    hoverinfo="y+x+name"
    )
fig.update_layout(
    height=900,
    #width = 1200,
    template="seaborn",
    title_text="soil temperature at listed depths",
)

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': 'temperature (celcius)',
    'textangle' : -90,
    'x': 0,
    'xshift' : -50,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.5,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

fig.update_layout(
    xaxis2 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis3 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis4 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis5 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis6 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis7 = dict(
        rangeselector = dict(
            visible = False))
)
fig.update_layout(
    xaxis8 = dict(
        rangeselector = dict(
            visible = False))
)
#set range and ticks
fig.update_yaxes(range=[-5, 25])
# x_max = datetime.now()
# x_min = x_max - timedelta(days = 90)
x_min = '2021-08-27'
x_max = '2021-10-24'
fig.update_xaxes(range = [x_min, x_max])



#fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/soil_temps.html')
print('updated soil temp figure')

soil_fig = fig
#plot(soil_fig)



###
#####
#batt_voltage plot
#build battery voltage dataframe
batt_df = pd.DataFrame(columns = ['TIMESTAMP','site','voltage'])
s1_batt = pd.read_csv(DATA_PATH.joinpath('S1-EM3_Table2.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','BattV_Min'], header = 0, parse_dates = True)
s1_batt = s1_batt.rename(columns = {'BattV_Min':'voltage'})
s1_batt['site'] = 's1_EM3'
batt_df = pd.concat([batt_df, s1_batt]) 

s3_batt = pd.read_csv(DATA_PATH.joinpath('S3_fenwell_S3FWMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
s3_batt = s3_batt.rename(columns = {'Batt_volt':'voltage'})
s3_batt['site'] = 's3_FW'
batt_df = pd.concat([batt_df, s3_batt])

s6_batt = pd.read_csv(DATA_PATH.joinpath('S6_bogwell_S6BWMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
s6_batt = s6_batt.rename(columns = {'Batt_volt':'voltage'})
s6_batt['site'] = 's6_bw'
batt_df = pd.concat([batt_df, s6_batt])

s6w_batt = pd.read_csv(DATA_PATH.joinpath('S6_Weir_S6ShelterT.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
s6w_batt = s6w_batt.rename(columns = {'Batt_Volt':'voltage'})
s6w_batt['site'] = 's6_w'
batt_df = pd.concat([batt_df, s6w_batt])

s2w_batt = pd.read_csv(DATA_PATH.joinpath('S2_Weir_ShelterT.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
s2w_batt = s2w_batt.rename(columns = {'Batt_Volt':'voltage'})
s2w_batt['site'] = 's2_w'
batt_df = pd.concat([batt_df, s2w_batt])

s2bw_batt = pd.read_csv(DATA_PATH.joinpath('S2_bogwell_S2BWMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
s2bw_batt = s2bw_batt.rename(columns = {'Batt_volt':'voltage'})
s2bw_batt['site'] = 's2_bw'
batt_df = pd.concat([batt_df, s2bw_batt])

df = pd.read_csv(DATA_PATH.joinpath('S4N_weir_S4NShelterT.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 's4N_w'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S6N_RO_S6N.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'S6N_RO'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('RAFES_Dat_1Hr.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','BattV_Min'], header = 0, parse_dates = True, engine = 'python', encoding = 'unicode_escape')

df = df.rename(columns = {'BattV_Min':'voltage'})
df['site'] = 'RAFES'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S2_Met_Station_Temp_15min.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','batt_volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'batt_volt':'voltage'})
df['site'] = 'S2_met'
batt_df = pd.concat([batt_df, df])


df = pd.read_csv(DATA_PATH.joinpath('S5_bogwell_S5BWMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_volt':'voltage'})
df['site'] = 'S5_bogwell'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S4_bogwell_S4BWMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_volt':'voltage'})
df['site'] = 'S4_bogwell'
batt_df = pd.concat([batt_df, df])

#new
df = pd.read_csv(DATA_PATH.joinpath('S2N_RO_S2N.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'S2N_RO'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('NorthWx_NorthMet.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','BattVolts'], header = 0, parse_dates = True)
df = df.rename(columns = {'BattVolts':'voltage'})
df['site'] = 'North_Wx'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('JB_temp_JB_PeatT.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'Jennies_Bog'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S2_forest_met_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','batt_volt_Min'], header = 0, parse_dates = True)
df = df.rename(columns = {'batt_volt_Min':'voltage'})
df['site'] = 'S2_forest_met'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S2N_soil_S2N-SOIL.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'S2N_Soil'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S2S_soil_S2S-SOIL.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'S2S_Soil'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('S2S_RO_S2S.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
df = df.rename(columns = {'Batt_Volt':'voltage'})
df['site'] = 'S2S_RO'
batt_df = pd.concat([batt_df, df])

df = pd.read_csv(DATA_PATH.joinpath('NADP_Met_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','batt_volt_Min'], header = 0, parse_dates = True)
df = df.rename(columns = {'batt_volt_Min':'voltage'})
df['site'] = 'NADP_Met'
batt_df = pd.concat([batt_df, df])


# df = pd.read_csv(DATA_PATH.joinpath('S4S_weir'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
# df = df.rename(columns = {'Batt_volt':'voltage'})
# df['site'] = 'S4S_weir'
# batt_df = pd.concat([batt_df, df])

# df = pd.read_csv(DATA_PATH.joinpath('S5Weir'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_volt'], header = 0, parse_dates = True)
# df = df.rename(columns = {'Batt_volt':'voltage'})
# df['site'] = 'S5_weir'
# batt_df = pd.concat([batt_df, df])

# df = pd.read_csv(DATA_PATH.joinpath('junction_fen'), skiprows = [0,2,3], na_values=('NAN'), usecols = ['TIMESTAMP','Batt_Volt'], header = 0, parse_dates = True)
# df = df.rename(columns = {'Batt_Volt':'voltage'})
# df['site'] = 'Junction_fen'
# batt_df = pd.concat([batt_df, df])

#plot batt voltage
batt_fig = px.line(batt_df, x='TIMESTAMP', y='voltage', color = 'site')

#tweak interactive hover info, asthetics 
batt_fig.update_traces(
    hoverinfo="y+x+name",
    connectgaps = False
    )
batt_fig.update_layout(
    height=700,
    #width = 1200,
    margin = dict(l=80),
    template="seaborn",
    title_text="battery voltage",
    yaxis_title="voltage (V)"
    ,
)

batt_fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#display last n days days of values
# x_max = datetime.now()
# x_min = x_max - timedelta(days = 60)
x_min = '2021-08-27'
x_max = '2021-10-24'
batt_fig.update_xaxes(range = [x_min, x_max])

y_max = 15
y_min = 10.4
batt_fig.update_yaxes(range = [y_min, y_max])



# batt_fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/battery_voltage.html')
print('updated battery voltage figure')
#plot(batt_fig)



###
#####
#Air temperatures/RH  Plots still need work, correct legend, labels, layout updates etc. etc.
NorthWx_Met = pd.read_csv(DATA_PATH.joinpath('NorthWx_NorthMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
SouthWx_Met = pd.read_csv(DATA_PATH.joinpath('South_Wx_SouthMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S2bog_Met = pd.read_csv(DATA_PATH.joinpath('S2_bogwell_S2BWMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S3fen_Met = pd.read_csv(DATA_PATH.joinpath('S3_fenwell_S3FWMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S4bog_Met = pd.read_csv(DATA_PATH.joinpath('S4_bogwell_S4BWMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S5bog_Met = pd.read_csv(DATA_PATH.joinpath('S5_bogwell_S5BWMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S6bog_Met = pd.read_csv(DATA_PATH.joinpath('S6_bogwell_S6BWMet.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#call plotly figure object
fig = make_subplots(rows = 3, cols = 1, vertical_spacing=.07, subplot_titles = ('Air Temp', 'RH','PAR'), shared_xaxes=True)

#add air temp traces for each site
fig.add_trace(
    go.Scatter(x=list(NorthWx_Met.TIMESTAMP), y=list(NorthWx_Met.AirT), name = 'NorthWx', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(SouthWx_Met.TIMESTAMP), y=list(SouthWx_Met.AirT), name = 'SouthWx', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2bog_Met.TIMESTAMP), y=list(S2bog_Met.AirT), name = 'Bog', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2bog_Met.TIMESTAMP), y=list(S2bog_Met.AirTBW), name = 'S2 Bogwell', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S3fen_Met.TIMESTAMP), y=list(S3fen_Met.AirT), name = 'S3 fenwell', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S4bog_Met.TIMESTAMP), y=list(S4bog_Met.AirT), name = 'S4 Bogwell', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S5bog_Met.TIMESTAMP), y=list(S5bog_Met.AirT), name = 'S5 Bogwell', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S6bog_Met.TIMESTAMP), y=list(S6bog_Met.AirT), name = 'S6 Bogwell', connectgaps=False), row = 1, col = 1)

#add RH traces for each site
fig.add_trace(
    go.Scatter(x=list(NorthWx_Met.TIMESTAMP), y=list(NorthWx_Met.RH), name = 'NorthWx', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(SouthWx_Met.TIMESTAMP), y=list(SouthWx_Met.RH), name = 'SouthWx', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2bog_Met.TIMESTAMP), y=list(S2bog_Met.RH), name = 'Bog', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2bog_Met.TIMESTAMP), y=list(S2bog_Met.RH), name = 'S2 Bogwell', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S3fen_Met.TIMESTAMP), y=list(S3fen_Met.RH), name = 'S3 fenwell', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S4bog_Met.TIMESTAMP), y=list(S4bog_Met.RH), name = 'S4 Bogwell', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S5bog_Met.TIMESTAMP), y=list(S5bog_Met.RH), name = 'S5 Bogwell', connectgaps=False), row = 2, col = 1)
fig.add_trace(
    go.Scatter(x=list(S6bog_Met.TIMESTAMP), y=list(S6bog_Met.RH), name = 'S6 Bogwell', connectgaps=False), row = 2, col = 1)

#add PAR traces for each site
fig.add_trace(
    go.Scatter(x=list(S2bog_Met.TIMESTAMP), y=list(S2bog_Met.PAR_Den), name = 'S2 Bogwell', connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(S3fen_Met.TIMESTAMP), y=list(S3fen_Met.PAR_Den), name = 'S3 fenwell', connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(S4bog_Met.TIMESTAMP), y=list(S4bog_Met.PAR_Den), name = 'S4 Bogwell', connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(S5bog_Met.TIMESTAMP), y=list(S5bog_Met.PAR_Den), name = 'S5 Bogwell', connectgaps=False), row = 3, col = 1)
fig.add_trace(
    go.Scatter(x=list(S6bog_Met.TIMESTAMP), y=list(S6bog_Met.PAR_Den), name = 'S6 Bogwell', connectgaps=False), row = 3, col = 1)

#plot(fig)

fig.update_traces(
    hoverinfo="y+x+name"
    )
fig.update_layout(
    height=900,
    #width = 1200,
    margin = dict(l=80),
    template="seaborn",
    title_text="Meteorology",
)

# x_max = datetime.now()
# x_min = x_max - timedelta(days = 90)
x_min = '2021-08-27'
x_max = '2021-10-24'
fig.update_xaxes(range = [x_min, x_max])
fig.update_yaxes(range=[-40, 40], row = 1, col = 1)
fig.update_yaxes(range=[0, 100], row = 2, col = 1)

fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': '',
    'textangle' : -90,
    'x': 0,
    'xshift' : -60,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.5,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
# hide range selectors
fig.update_layout(
    xaxis2 = dict(
        rangeselector = dict(
            visible = False))
    )
fig.update_layout(
    xaxis3 = dict(
        rangeselector = dict(
            visible = False))
    )
fig.update_layout(
    xaxis4 = dict(
        rangeselector = dict(
            visible = False))
    )
fig.update_layout(
    xaxis5 = dict(
        rangeselector = dict(
            visible = False))
    )

# fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/airT_RH_PAR.html')
print('updated AirT/RH figure')
#rename
fig_5 = fig

#plot(fig_5)



###
#####
#Runoff plot
S2S_RO = pd.read_csv(DATA_PATH.joinpath('S2S_RO_S2S.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S2N_RO = pd.read_csv(DATA_PATH.joinpath('S2N_RO_S2N.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
S6N_RO = pd.read_csv(DATA_PATH.joinpath('S6N_RO_S6N.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)

#call plotly figure object
fig = make_subplots(rows = 1, cols = 1, subplot_titles = ('Runoff Levels',))

#add RO stages for each site
fig.add_trace(
    go.Scatter(x=list(S2S_RO.TIMESTAMP), y=list(S2S_RO.Level_SUB), 
               name = 'S2S_SUB', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2S_RO.TIMESTAMP), y=list(S2S_RO.Level_SURF), name = 'S2S_SURF', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2N_RO.TIMESTAMP), y=list(S2N_RO.Level_SURF), name = 'S2N_SURF', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S2N_RO.TIMESTAMP), y=list(S2N_RO.Level_SUB), name = 'S2N_SUB', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S6N_RO.TIMESTAMP), y=list(S6N_RO.Level_SURF), name = 'S6N_SURF', connectgaps=False), row = 1, col = 1)
fig.add_trace(
    go.Scatter(x=list(S6N_RO.TIMESTAMP), y=list(S6N_RO.Level_SUB), name = 'S6N_SUB', connectgaps=False), row = 1, col = 1)
fig.add_hline(y=2.5,line_width=3, line_dash="dash", line_color = 'red',
              annotation_text="overfill level", 
              annotation_position="top right")
#plot(fig)
#print("plotly version: ", py.__version__)
fig.update_traces(
    hoverinfo="y+x+name"
    )
fig.update_layout(
    height=500,
    #width = 1200,
    margin = dict(l=80),
    template="seaborn",
)

# x_max = datetime.now()
# x_min = x_max - timedelta(days = 180)
x_min = '2022-04-14'
x_max = '2022-07-12'
fig.update_xaxes(range = [x_min, x_max])
fig.update_yaxes(range=[-0.1, 2.55], row = 1, col = 1)

fig.add_annotation({
    'font': {'size': 16},
    'showarrow': False,
    'text': 'Runoff stage ft',
    'textangle' : -90,
    'x': 0,
    'xshift' : -60,
    'xanchor': 'right',
    'xref': 'paper',
    'y': 0.5,
    'yanchor': 'middle',
    'yref': 'paper',
    'yshift': -30
})

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=14, label="2w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/runoff.html')
print('updated RO figure')
#rename
RO_fig = fig
#plot(RO_fig)




###
#####
#context plots. Returns water table elevations with historic ranges
#dataframe building
infile1  ="https://pasta.lternet.edu/package/data/eml/edi/562/2/671f15337a677da71852de506a8d9b05".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
           , names=[
                    "PEATLAND",     
                    "DATE",     
                    "WTE",     
                    "FLAG"    ]
          ,parse_dates=[
                        'DATE',
                ] 
            ,na_values={
                  'WTE':[
                          'NA',],
                  'FLAG':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata  
dt1.PEATLAND=dt1.PEATLAND.astype('category') 
# To help with dates, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(DATE_datetime=pd.to_datetime(dt1.DATE,errors='coerce')) 
dt1.WTE=pd.to_numeric(dt1.WTE,errors='coerce')  
dt1.FLAG=dt1.FLAG.astype('category') 

data = pd.DataFrame(columns = ['PEATLAND', 'min', 'max', '10', '25', '50', '75', '90'])
#loop through sites
site = 'S6'
for site in ['BOGLK', 'S2', 'S3', 'S4', 'S5', 'S6', 'S1']:
    df = dt1[dt1['PEATLAND'] == site] 
    df = df[['WTE', 'DATE_datetime']]
    #year_min = str(df['DATE_datetime'].dt.year.min())
    #year_max = str(df['DATE_datetime'].dt.year.max())
    #create new dataframe to house quantiles
    df_quant = pd.DataFrame(columns = ['PEATLAND','min', '10' , '25', '50', '75', '90', 'max'])
    
    #pivot by day of year and assign percentiles 
    df_quant['min'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).min()['WTE']
    df_quant['max'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).max()['WTE']
    df_quant['10'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).quantile(.1, numeric_only = True)['WTE']
    df_quant['25'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).quantile(.25, numeric_only = True)['WTE']
    df_quant['50']= df.groupby([df['DATE_datetime'].dt.dayofyear]).quantile(.50, numeric_only = True)['WTE']
    df_quant['75'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).quantile(.75, numeric_only = True)['WTE']
    df_quant['90'] = df.groupby([df['DATE_datetime'].dt.dayofyear]).quantile(.90, numeric_only = True)['WTE']
    df_quant['PEATLAND'] = site
    data = pd.concat([data, df_quant]) #data.concat(df_quant)

#load real time/sample data 

# blf_wt = pd.read_csv(DATA_PATH.joinpath('BLF_met_BogLakeW.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
# s1_wt = pd.read_csv(DATA_PATH.joinpath('S1-EM3_Table1.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
# s2_wt = pd.read_csv(DATA_PATH.joinpath('S2bog_S2BW.dat'), skiprows = [0,2,3],na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
# s3_wt = pd.read_csv(DATA_PATH.joinpath('S3_fenwell_S3FW.dat'), skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
# s4_wt = pd.read_csv(DATA_PATH.joinpath('S4_bogwell_S4BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), engine = 'python', parse_dates = True)
# s5_wt = pd.read_csv(DATA_PATH.joinpath('S5_bogwell_S5BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), engine = 'python', parse_dates = True)
# s6_wt = pd.read_csv(DATA_PATH.joinpath('S6_bogwell_S6BW.dat'), skiprows = [0,2,3], header = 0, na_values=('NAN'), parse_dates = True)
# filepaths = {'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\RealTimeData\\S6_bogwell_S6BW.dat':'S6',
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\annual_appended_logger_files\\2020\\S4_bogwell_S4BW.dat':'S4',
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\RealTimeData\\S3_fenwell_S3FW.dat':'S3',
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\RealTimeData\\S2_bogwell_S2BW.dat':'S2',
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\RealTimeData\\S1-EM3_Table1.dat':'S1', 
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\annual_appended_logger_files\\2020\\S5_bogwell_S5BW.dat':'S5',
#              'C:\\Users\\'+ user + '\\Box\\External-MEF_DATA\\DataDump\\RealTimeData\\BLF_met_BogLakeW.dat':'BOGLK'}


filepaths = {dir_work + '\\S6_bogwell_S6BW.dat':'S6',
             dir_work + '\\S4_bogwell_S4BW.dat':'S4',
             dir_work + '\\S3_fenwell_S3FW.dat':'S3',
             dir_work + '\\S2bog_S2BW.dat':'S2',
             dir_work + '\\S1-EM3_Table1.dat':'S1', 
             dir_work + '\\S5_bogwell_S5BW.dat':'S5',
             dir_work + '\\BLF_met_BogLakeW.dat':'BOGLK'}
df_wts = pd.DataFrame()

# k = dir_work + '\\S2_bogwell_S2BWMet.dat'
 
for k,v in filepaths.items():
    df_wt = pd.read_csv(k, skiprows = [0,2,3], na_values=('NAN'), header = 0, engine = 'python', parse_dates = True)
    df_wt=df_wt.assign(datetime=pd.to_datetime(df_wt.TIMESTAMP,errors='coerce'))
    df_wt['dayofyear'] = ''
    #assign day of year based on date
    for i in df_wt.index:
        df_wt.loc[i, 'dayofyear'] = df_wt.loc[i, 'datetime'].dayofyear
        #df_wt['dayofyear'][i] = df_wt['datetime'][i].dayofyear
    #initialize quantile columns
    df_wt['min'] = ''
    df_wt['max'] = ''
    df_wt['10']= ''
    df_wt['25']= ''
    df_wt['50']= ''
    df_wt['75']= ''
    df_wt['90']= ''

    #i=1
    for i in df_quant.index:     #assign quantile values to day of year by site
        df_wt.loc[df_wt.dayofyear == i, 'min'] = data[data['PEATLAND'] == v]['min'][i]
        df_wt.loc[df_wt.dayofyear == i, 'max'] = data[data['PEATLAND'] == v]['max'][i]
        df_wt.loc[df_wt.dayofyear == i, '10'] = data[data['PEATLAND'] == v]['10'][i]
        df_wt.loc[df_wt.dayofyear == i, '25'] = data[data['PEATLAND'] == v]['25'][i]
        df_wt.loc[df_wt.dayofyear == i, '50'] = data[data['PEATLAND'] == v]['50'][i]
        df_wt.loc[df_wt.dayofyear == i, '75'] = data[data['PEATLAND'] == v]['75'][i]
        df_wt.loc[df_wt.dayofyear == i, '90'] = data[data['PEATLAND'] == v]['90'][i]
    
    #convert ft to meters
    df_wt['PEATLAND'] = v
    df_wts = pd.concat([df_wts, df_wt]) #df_wts.concat(df_wt)
df_wts['WT_e'] = df_wts['WTElev'].fillna(0) + df_wts['WT_Elev'].fillna(0)
df_wts['WT_m'] = df_wts['WT_e'] * .3048
df_wtt = df_wts[['datetime', 'PEATLAND','WT_e','WT_m', 'dayofyear', 'min', 'max', '10', '25', '50', '75', '90']]
df_wtt.reset_index(inplace = True)
for i in df_wtt.index: #replace any zeros or blank values with nan
    if df_wtt.loc[i,'WT_m'] in [0, '0', '']:
        df_wtt.loc[i,'WT_m'] = np.nan



#Build WT context plot
for val_chosen in ['BOGLK', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']:
    dff = df_wtt[df_wtt["PEATLAND"] == val_chosen]
    min_date = dff['datetime'].min()
    max_date = dff['datetime'].max()
    fig = go.Figure()
    fig.update_layout(
        title_text = 'Peatland water table elevation at ' + val_chosen + ' peatland and seasonal historic water table range', title_x=0.5,
        yaxis_title = 'Water table elevation (m)',
        xaxis_title = 'Date',
        yaxis2=dict(
                    title = 'daily precip (in)',
                    overlaying='y',
                    side='right',
                    automargin = True,
                    range = [0,3]
                    ),
        legend=dict(
                    yanchor="top",
                    y=1,
                    xanchor="left",
                    x=1.065
                    )
        )
    fig.add_trace(go.Bar(
        x = df_NADP[(df_NADP['TIMESTAMP']>= min_date) & (df_NADP['TIMESTAMP']<= max_date)]['TIMESTAMP'], y = df_NADP[df_NADP['TIMESTAMP']>= min_date]['ReportPCP'],
        #visible = 'legendonly',
        yaxis = 'y2',
        name = 'NADP NOAHIV'
        ))
    #fig.update_yaxes(title_text="daily precip (in)", secondary_y=True)
    fig.add_trace(go.Scatter(
        x=dff['datetime'], 
        y= signal.savgol_filter(dff['min'], # smoothes data because day of year repeated over multiple times a day
                                53, # window size used for filtering
                                3), # order of fitted polynomial ,
        hoverinfo='skip',
        mode='lines',
        showlegend = False,
        line=dict(width=0, color='rgb(131, 90, 241)'),
        fill = None # define stack group
    ))
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['10'],
                               53, # window size used for filtering
                               3), # order of fitted polynomial ,
        hoverinfo='skip',
        mode='lines',
        name = 'min-10th percentile',
        line=dict(width=0, color='indianred'),
        fill = 'tonexty'
    ))
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['25'],
                               53, # window size used for filtering
                               3), # order of fitted polynomial ,
        name = '10-25th percentile',
        mode='lines',
        hoverinfo = 'skip',
        opacity = .1, 
        line=dict(width=0, color='darksalmon'),
        fill = 'tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['75'],
                               53, # window size used for filtering
                               3), # order of fitted polynomial ,
        name = '25-75th percentile',
        mode='lines',
        hoverinfo = 'skip',
        line=dict(width=0, color='darkseagreen'),
        fill = 'tonexty'
    ))
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['90'],
                               53, # window size used for filtering
                               3), # order of fitted polynomial ,
        name = '75-90th percentile',
        mode='lines',
        hoverinfo = 'skip',
        line=dict(width=0, color='cornflowerblue'),
        fill = 'tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['max'],
                               53, # window size used for filtering
                               3), # order of fitted polynomial ,
        name = '90th percentile-max',
        hoverinfo = 'skip',
        mode='lines',
        line=dict(width=0, color='darkblue'),
        fill = 'tonexty'
    ))
    
    #median line
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= signal.savgol_filter(dff['50'],
                               53, # window size used for filtering
                               4), # order of fitted polynomial ,
        name = 'median',
        mode='lines',
        line=dict(width=2, dash = 'dot', color='dimgrey'),
    ))
    
    #wtelev line
    fig.add_trace(go.Scatter(
        x=dff['datetime'], y= dff['WT_m'],
        name = val_chosen + '_WT',
        mode='lines',
        line=dict(width=2, color='black'),
    ))
    locals()[val_chosen + '_fig'] = fig
x_min = '2021-07-12'
x_max = '2022-07-12'
fig.update_xaxes(range = [x_min, x_max])
    
# fig.write_html('C:/Users/'+ user + '/Box/External MEF-WORKSPACE/Realtime_sensor_figures/water_table_elev_S6_historic.html')
print('updated water table context figure')
#plot(fig)
    
    

   
    


#######################################################
############################
###### Dash App build
print('building dashboard')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
site_list = ['Bog Lake', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']
server = app.server
tabs_styles = {
    'height': '24px'
}


app.layout = html.Div([
    html.H2(html.A([html.Img(
            style={
            'background-image': 'url("https://phenocam.sr.unh.edu/data/latest/boglakepeatland.jpg")',            
            'height' : 250,
            'width' : 1296,
            'background-position': '0% 23%',
            'background-size':'cover',
            'float' : 'none',
            'position' : 'relative',
            'padding-top' : 0,
            'padding-right' : 0
                },   
        ),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
        ], href = 'https://phenocam.sr.unh.edu/webcam/sites/boglakepeatland/', target="_blank"),
        ),
    html.H2('Marcell Experimental Forest dashboard'),        
    dcc.Tabs([
        dcc.Tab(label = 'Peatland Water Table Elevation', children =[
            dcc.Graph(id='graph-output', figure={}, style={"height": 450}),
            dcc.RadioItems(id = 'my-radioitem', 
                           value = 'Bog Lake',
                           options = [{'label':s, 'value':s} for s in site_list], 
                           labelStyle={'display': 'inline-block'}),
            dcc.Graph(figure = fig_2, style={"height": 450})
            ]),
        dcc.Tab(label = 'Streamflow', children = [
            dcc.Graph(figure = fig_3, style={"height": 500})]),
        dcc.Tab(label = 'Precipitation', children = [
            dcc.Graph(figure = fig_4, style={"height": 900})]),
        dcc.Tab(label = 'Runoff', children = [
            dcc.Graph(figure = RO_fig, style={"height": 500})]), 
        dcc.Tab(label = 'Meteorology', children = [
            dcc.Graph(figure = fig_5, style={"height": 900})]),
        dcc.Tab(label = 'Soil Temperature', children = [
            dcc.Graph(figure = soil_fig, style={"height": 900})]),
        dcc.Tab(label = 'Battery Voltage', children = [
            dcc.Graph(figure = batt_fig, style={"height": 700})])
        
        ])
    ])

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    [Input(component_id='my-radioitem', component_property='value')],
    # [Input(component_id='my-button', component_property='n_clicks')],
    # [State(component_id='my-dropdown', component_property='value')],
    prevent_initial_call=False
)
#val_chosen = 'S2'

#undefined variables are set above at the end of wt context plot "locals()[val_chosen + '_fig'] = fig"
#should update to remove dependancy to setting local variables in naming plot
def update_my_graph(value):
    if value == 'Bog Lake':
        return BOGLK_fig
    elif value == 'S1':
        return S1_fig
    elif value == 'S2':
        return S2_fig
    elif value == 'S3':
        return S3_fig
    elif value == 'S4':
        return S4_fig
    elif value == 'S5':
        return S5_fig
    elif value == 'S6':
        return S6_fig

if __name__ == '__main__':
    app.run_server()
    
