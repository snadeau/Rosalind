#Scott Nadeau
#Rosalind
#Mendel's First Law

YY = float(2)
Yy = float(2)
yy = float(0)

total = YY + Yy + yy

prob_YY = YY / total
prob_Yy = Yy / total
prob_yy = yy / total

prob_YY_YY = prob_YY * ((YY-1) / (total-1))
prob_YY_Yy =  prob_YY * (Yy / (total-1))
prob_Yy_YY =  prob_Yy * (YY / (total-1))
prob_YY_yy =  prob_YY * (yy / (total-1))
prob_yy_YY =  prob_yy * (YY / (total-1))
prob_Yy_Yy = prob_Yy * ((Yy-1) / (total-1))
prob_Yy_yy =  prob_Yy * (yy / (total-1))
prob_yy_Yy =  prob_yy * (Yy / (total-1))
prob_yy_yy = prob_yy * ((yy-1) / (total-1))

print prob_YY_YY+prob_YY_Yy+prob_Yy_YY+prob_YY_yy+prob_yy_YY+prob_Yy_Yy+prob_Yy_yy+prob_yy_Yy+prob_yy_yy # should equal 1

prob_Y = prob_YY_YY + prob_YY_Yy + prob_Yy_YY + prob_YY_yy + prob_yy_YY + (.75 * prob_Yy_Yy) + (.5 * prob_Yy_yy) + (.5 * prob_yy_Yy)

print prob_Y # probability of a dominant allele in offspring given random mating of two individuals in the population
