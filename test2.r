install.packages('sqldf')
library('sqldf')
a <- read.csv('C:\\Users\\진수빈\\Downloads\\RepairExample_English.csv')
head(a)
summary(a)
str(a)
time <- a['timestamp']
time
time_date <- as.character(time)
str(time_date)
time_date
install.packages('anytime')
library('anytime')
newtime <-as.Date(time, format="%Y-%m-%d %H:%M:%S")
as.Date(time, format = "%m/%d/%Y")
