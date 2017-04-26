# Select csv file of foldx analysis
openFile = file.choose()
mydata = read.csv(openFile, sep = '\t')
# View the data
mydata
# Histogram of free energy change in mutants
hist(mydata$total.energy, main='Free Energy Change of Mutatants', xlab = 'Free Energy Change', ylab = 'Frequency', border = 'black', col = 'gray', prob=TRUE, ylim=c(0,.15))
lines(density(mydata$total.energy), type='h')
# Normalize free energy change in mutants
normalized_mutation = mydata$total.energy/mydata$mutations
normalized_mutation
# Histogram of normalized free energy change in  mutants
hist(normalized_mutation, main='Normalized Free Energy Change of Mutants', xlab = 'Free Energy Change', ylab = 'Frequency', border = 'black', col = 'gray', prob=TRUE)
lines(density(normalized_mutation), type='h')
