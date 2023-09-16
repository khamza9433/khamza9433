apple <- read.csv("C:/Users/khamz/Downloads/Amazoncustreviews.csv", header = T)


library(tm)
library(syuzhet)

corpus <- iconv(apple$reviews.text)

#This is to analyse the words in the review and give them a value on whether they are positive or negative
s <- get_nrc_sentiment(corpus)

#Create a barchart with the emotions and how often they occur

head(s)

barplot(colSums(s),
        las = 2,
        col = rainbow(10),
        ylab = 'Count',
        main = 'Sentiment Scores Tweets')
