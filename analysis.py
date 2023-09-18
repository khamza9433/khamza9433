#importing modules
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import plotly.express as px

#reading the csv file
data = pd.read_csv("Apple-Fitness-Data.csv")

#printing the table
#print(data.head())

#Checking if data has any null values or not
#print(data.isnull().sum())

#finding step count over time
#fig1 = px.line(data, x="Time",y="Step Count",title="Step Count Over Time")
#fig1.show()

#Energy burned over time
#fig3 = px.line(data, x="Time",y="Energy Burned",title = "Energy Burnt Over Time")
#fig3.show()

#Walking speed over time
#fig4 = px.line(data, x="Time",y="Walking Speed",title="Walking Speed Over Time")
#fig4.show()

#Average step count per day
#average_step_count_per_day = data.groupby("Date")["Step Count"].mean().reset_index()

#fig5 = px.bar(average_step_count_per_day, x="Date", y="Step Count",title="Average Step Count per Day")
#fig5.update_xaxes(type='category')
#fig5.show()

#calulate walking efficiency
#data["Walking Efficiency"] = data["Distance"] / data["Step Count"]

#fig6 = px.line(data,x="Time",y="Walking Efficiency",title="Walking Efficiency Over Time")
#fig6.show()

#Creating time intervals

time_intervals = pd.cut(pd.to_datetime(data["Time"]).dt.hour, bins=[0,12,18,24], labels = ["Morning","Afternoon","Evening"],right=False)
data["Time Interval"] = time_intervals

fig7 = px.scatter(data, x="Step Count",y="Walking Speed",color="Time Interval",
title = "Step count and Walking Speed", trendline='ols')

fig7.show()



