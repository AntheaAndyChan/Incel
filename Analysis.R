setwd("C:\\Users\\anthe\\Documents\\GitHub\\Incel")

dat<- read.csv("coding_data_processed_October_LIWC.csv")
dat$"Dissatisfaction.w..Fam" <- NULL

sum(is.na(dat$"Hegemony_Conflict"))
dat<-dat[!is.na(dat$"Hegemony_Conflict"),]

Farrell<-dat[c((which(colnames(dat)=="Hegemony_Conflict"):which(colnames(dat)=="Total.Misogyny")))]
Farrell <- round((Farrell * 100),3)
summary(Farrell)

dat<-dat[c((which(colnames(dat)=="Sentiment.Valence")),
           (which(colnames(dat)=="Analytic"):which(colnames(dat)=="Tone")),
           (which(colnames(dat)=="affect"):which(colnames(dat)=="filler"))
)]
dat<-cbind(Farrell,dat)
summary(dat)
write.csv(dat, "Ready.csv")

dat2<-dat2[c((which(colnames(dat)=="submission_title"):which(colnames(dat)=="is_submitter"))
)]


write.csv(dat2, "Ready2.csv")



#write.csv(dat, "FeaturesOnly.csv")


mydata <- scale(dat) # standardize variables 


#Cluster Analysis
d <- dist(mydata, method = "euclidean") # distance matrix

# Ward Hierarchical Clustering


fit <- hclust(d, method="ward.D2")
plot(fit) # display dendogram
groups <- cutree(fit, k=5) # cut tree into 5 clusters
# draw dendogram with red borders around the 5 clusters
rect.hclust(fit, k=5, border="red") 
# Visualize
plot(fit, cex = 0.5)

#Agglomerative Method
# Compute with agnes
library(cluster) 
hc2 <- agnes(d, method = "complete")

# Agglomerative coefficient
hc2$ac

# methods to assess
m <- c( "average", "single", "complete", "ward")
names(m) <- c( "average", "single", "complete", "ward")

# function to compute coefficient
ac <- function(x) {
  agnes(df, method = x)$ac
}

map_dbl(m, ac)

hc3 <- agnes(df, method = "ward")
pltree(hc3, cex = 0.6, hang = -1, main = "Dendrogram of agnes") 

# K-Means Clustering with 5 clusters
fit <- kmeans(mydata, 5)

# vary parameters for most readable graph 
clusplot(mydata, fit$cluster, color=TRUE, shade=TRUE,
         labels=2, lines=0)

# Centroid Plot against 1st 2 discriminant functions
library(fpc)
plotcluster(mydata, fit$cluster) 