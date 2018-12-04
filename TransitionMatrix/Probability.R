# function to read copy number transition data from the txt file generated from the tree
function.readfromtree <- function(m)
{
  data<- read.delim(m, sep=" ")
  data=data[,-9]
  data=data[,-9]
  data=data[,-18]
  data=data[,-18]
  colnames(data) <- c("rootgene1","rootgene2","rootgene3","rootgene4","rootgene5","rootgene6","rootgene7","rootgene8","rootcellcount","offsgene1","offsgene2","offsgene3","offsgene4","offsgene5","offsgene6","offsgene7","offsgene8","offscellcount","changeprobe1","changeprobe2","changeprobe3","changeprobe4","changeprobe5","changeprobe6","changeprobe7","changeprobe8","changeprobenumber")
  data$changeprobe1 <- as.numeric(gsub("\\[","",data$changeprobe1))
  data$changeprobe8 <- as.numeric(gsub("\\]","",data$changeprobe8))
  return(data)
}

data <- function.readfromtree("tree_topology_patient_1.txt")

#generate exmpty vector, 8 vector each contains transition probability information for each gene probe
a <- matrix(c(rep(0, times=18*18)), nrow=18, ncol=18)
colnames(a) <- c("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","total")
rownames(a) <- c("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","total")
ProbeProbMatrix <- list(a,a,a,a,a,a,a,a)

i <- j <- k <- l <- m <- n <- o <- p <- q <- 0 

# add the cell number to each entry of the copy number transition matrix. 
# The row stands for the original copy number, 
# the column stands for the copy number after the transition
for (i in 1:(nrow(data))){
  for (j in 1:8){
    if (data[i,18+j] == 1){
      ProbeProbMatrix[[j]][data[i,j]+1,data[i,9+j]+1] = ProbeProbMatrix[[j]][data[i,j]+1,data[i,9+j]+1] + data[i,18]
    }
  }
}

# get the sum of the number of cells in cop number transition matrix
for (k in 1:8){
  for (l in 1:17){
    ProbeProbMatrix[[k]][18,l] = sum(ProbeProbMatrix[[k]][,l])
  }
  for (m in 1:17){
    ProbeProbMatrix[[k]][m,18] = sum(ProbeProbMatrix[[k]][m,])
  }
}

# from the sum and each entry, calculate normalized probabilities
for (n in 1:8){
  for (o in 1:17){
    for (p in 1:17){
      if ((ProbeProbMatrix[[n]][o,18]) == 0) next
      ProbeProbMatrix[[n]][o,p] = round((ProbeProbMatrix[[n]][o,p])/(ProbeProbMatrix[[n]][o,18]), digits=3)
    }
  }
}

# ouput of 8 txt files. Each represent a gene probe with the probability matrix of copy number transitions
for (q in 1:8){
  write.table(ProbeProbMatrix[[q]], file=paste("Probe",q,"_ProbMatix_CNV.txt",sep=""))
}
