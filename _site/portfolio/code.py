import plotly.express as px


experience_dict = {'Programming Language': ['C++', 'Fortran', 'OPEN MPI', 'OpenMP', 'R', 'Linux/bash','Matlab','Python'], 'Years of Experience (As of January 2023)': [15,4,3,2,15,21,10,12]}

fig = px.bar(experience_dict, x='Programming Language', y='Years of Experience (As of January 2023)',color_discrete_sequence=['rgba(0,0,0,0.16)'])


fig.update_layout(
    paper_bgcolor = "rgba(0,0,0,0.16)",
    plot_bgcolor = "rgba(0,0,0,0.16)",
    font_color = "rgba(0,0,0,0.7)",
    font_family = 'verdana',
    font_size = 20,
    )
fig.write_html("skills.html")


