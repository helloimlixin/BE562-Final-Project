C1 = 0
C1 <- read.delim("B9/B9_IDC.txt")
C1 = C1[-1,]
C1 = C1[,-12]


colnames(C1) <- c("chrom1","chrom2","gene1","gene2","gene3","gene4","gene5","gene6","gene7","gene8","cellnum")


i=0
j=0
k=0
l=0
m=0

for (i in 1:(nrow(C1))){
  for (j in 1:(nrow(C1))){
    if ((C1$gene1[j] == C1$gene1[i]) && (C1$gene2[j] == C1$gene2[i]) && (C1$gene3[j] == C1$gene3[i]) && (C1$gene4[j] == C1$gene4[i]) && (C1$gene5[j] == C1$gene5[i]) && (C1$gene6[j] == C1$gene6[i]) && (C1$gene7[j] == C1$gene7[i]) && (C1$gene8[j] == C1$gene8[i]) && (i!=j)){
      C1$cellnum[i] = C1$cellnum[i] + C1$cellnum[j]
      C1$cellnum[j] = 0
      
    }
  }
}

C1 <- C1[order(C1$cellnum),]

for (k in 1:(nrow(C1))){
  if (C1$cellnum[k] == 0){
    l = l + 1
  }
}

for (m in 1:(l)){
  C1 <- C1[-1,]
}

C1 <- C1[do.call(order, c(data.frame(C1[,3:11]))),]

write.table(C1, file="P_B9_IDC.txt", row.names=FALSE)

