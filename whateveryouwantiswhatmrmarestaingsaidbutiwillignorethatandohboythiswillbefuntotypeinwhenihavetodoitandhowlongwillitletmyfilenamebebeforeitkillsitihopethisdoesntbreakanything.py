# code,state,category,number students
# AL,Alabama,state,1
# AK,Alaska,state,2
# AZ,Arizona,state,25
# AR,Arkansas,state,1
# CA,California,state,0
# CO,Colorado,state,11
# CT,Connecticut,state,3
# DE,Delaware,state,0
# FL,Florida,state,11
# GA,Georgia,state,0
# HI,Hawaii,state,13
# ID,Idaho,state,2
# IL,Illinois,state,7
# IN,Indiana,state,4
# IA,Iowa,state,2
# KS,Kansas,state,4
# KY,Kentucky,state,2
# LA,Louisiana,state,3
# ME,Maine,state,1
# MD,Maryland,state,4
# MA,Massachusetts,state,5
# MI,Michigan,state,4
# MN,Minnesota,state,4
# MS,Mississippi,state,5
# MO,Missouri,state,4
# MT,Montana,state,2
# NE,Nebraska,state,3
# NV,Nevada,state,23
# NH,New Hampshire,state,1
# NJ,New Jersey,state,2
# NM,New Mexico,state,9
# NY,New York,state,14
# NC,North Carolina,state,1
# ND,North Dakota,state,1
# OH,Ohio,state,3
# OK,Oklahoma,state,3
# OR,Oregon,state,13
# PA,Pennsylvania,state,6
# RI,Rhode Island,state,1
# SC,South Carolina,state,1
# SD,South Dakota,state,1
# TN,Tennessee,state,2
# TX,Texas,state,11
# UT,Utah,stawte,14
# VT,Vermont,state,1
# VA,Virginia,state,5
# WA,Washington,state,13
# WV,West Virginia,state,2
# WI,Wisconsin,state,2
# WY,Wyoming,state,2

import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig=go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['number students'].astype(float),
    locationmode='USA-states',
    colorscale='ice',#earth, prgn, ocy, hdv, icefire, purd, purp, jet, hot, plotly3, grey, rainbow
    colorbar_title='the least used amtrak stations in west virginia or something like that',
))

fig.update_layout(
    geo_scope='usa',
    title_text="Map of visted states"
)



fig.show()