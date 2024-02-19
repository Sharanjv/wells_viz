import altair as alt
from vega_datasets import data


def plot_wells(wells_df):
    
    # Read in polygons from topojson
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white',
        tooltip=None
    ).properties(
        width=600,
        height=360
    ).project('albersUsa')
    
    wells_points = (alt.Chart(wells_df).mark_circle()
                .encode(latitude='latitude', longitude='longitude', 
                        color=alt.Color('gradient').scale(scheme='yelloworangered'),
                        tooltip=[alt.Tooltip('depth', title='Depth(m)'),
                                 alt.Tooltip('gradient', title='Gradient (C/m)', format='0.2f')])
                   ).properties(title='Wells Locations')
    chart= background + wells_points
    
    return chart