apple <- read.csv("C:/Users/khamz/Downloads/Amazoncustreviews.csv", header = T)
str(apple)

library(tm)
corpus <- iconv(apple$reviews.text)
corpus <- Corpus(VectorSource(corpus))
inspect(corpus[1:100])

corpus <- tm_map(corpus, tolower)
inspect(corpus[1:100])

corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)

cleanset <- tm_map(corpus, removeWords, stopwords('english'))

cleanset <- tm_map(cleanset, stemDocument)
cleanset <- tm_map(cleanset, stripWhitespace)

#Create a worldcloud with the most occuring words

library(wordcloud)
w <- sort(rowSums(tdm), decreasing = TRUE)
set.seed(222)
wordcloud(words = names(w),
          freq = w,
          max.words = 150,
          random.order = F,
          min.freq = 5,
          colors = brewer.pal(8, 'Dark2'),
          scale = c(5, 0.3),
          rot.per = 0.7)