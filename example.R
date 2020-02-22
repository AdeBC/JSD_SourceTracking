library(philentropy)
# retrieve available distance metrics



#
P <- 1:10/sum(1:10)
Q <- 20:29/sum(20:29)
x <- rbind(P,Q)
JSD(x)



sink <- array(1:200, dim = c(50,4))
sources <- array(1:1000, dim = c(50,5,4))
source_names <- array(c('aa','bb','cc','dd','ee'), dim = c(5,4))
sink_names <- array(c('11','22','33','44'))

JSD_tracking(sources = sources, sink = sink, source_names = source_names, sink_names = sink_names)



