# library(philentropy)
# retrieve available distance metrics


JSD_tracking_one_SINK <- function(sources, sink){
  
  sources <- t(sources)
  
  JSD_dist <- vector(mode = 'numeric', 
                     length = ncol(sources))
  
  for(index in 1:ncol(sources)){
    source <- as.vector(sources[, index])
    JSD_dist[index] <- jsd(source, as.vector(sink[1, ]))
  }
  
  return(list(distances = JSD_dist, distribution = (1/JSD_dist)/sum(1/JSD_dist)))
}


rarefy <- function(x,maxdepth){
  
  
  if(is.null(maxdepth)) return(x)
  
  if(!is.element(class(x), c('matrix', 'data.frame','array')))
    x <- matrix(x,nrow=nrow(x))
  nr <- nrow(x)
  nc <- ncol(x)
  
  for(i in 1:nrow(x)){
    if(sum(x[i,]) > maxdepth){
      prev.warn <- options()$warn
      options(warn=-1)
      s <- sample(nc, size=maxdepth, prob=x[i,], replace=T)
      options(warn=prev.warn)
      x[i,] <- hist(s,breaks=seq(.5,nc+.5,1), plot=FALSE)$counts
    }
  }
  return(x)
}


jsd <- function(p,q){
  m <- (p + q)/2
  return((kld(p,m) + kld(q,m))/2)
}


kld <- function(p,q){
  nonzero <- p>0 & q>0
  return(sum(p[nonzero] * log2(p[nonzero]/q[nonzero])))    
}

