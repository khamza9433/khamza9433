#To read the csv file

csvfile1 <- read.csv("C:/Users/khamz/Downloads/Amazoncustreviews.csv", header = T)

# This is to isolate the text and then we will look clean it up so it is just words

library(tm)
corpus <- iconv(csvfile1$reviews.text)


corpus <- Corpus(VectorSource(corpus))
inspect(corpus[1:100])

#Change text to lower caps

corpus <- tm_map(corpus, tolower)
inspect(corpus[1:100])

#Remove punctuation and special characters

corpus <- tm_map(corpus, removePunctuation)

#Remove numbers
corpus <- tm_map(corpus, removeNumbers)

#remove filler words such as the, as

cleanset <- tm_map(corpus, removeWords, stopwords('english'))

#create a matrix of the 10 most occuring words

tdm <- TermDocumentMatrix(cleanset)
tdm <- as.matrix(tdm)
tdm[1:10, 1:20]