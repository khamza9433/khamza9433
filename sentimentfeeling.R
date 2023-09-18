apple <- read.csv("C:/Users/khamz/Downloads/Amazoncustreviews.csv", header = T)


library(tm)
library(syuzhet)

#Get the emotions of the text and put them in a table

corpus <- iconv(apple$reviews.text)
s <- get_nrc_sentiment(corpus)
head(s)