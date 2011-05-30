#!/usr/bin/env python
#
# Requires python-adns
# http://linux-101.org
#
 
# List of DNS Servers
servers = ("201.193.78.6","201.193.78.7","200.91.75.5","200.91.75.6")
 
# Number of times to loop through
runs = 1
 
# Number of queries to perform on each run against each server. Must be an even number for ease of calculating the Median value in the resultant dataset.
queries = 1000
 
# Print a message every X number of queries
printCount = 100
 
 
import adns
import sys
import time
 
totalStart = time.time()
urlFile = open("sites.txt", "r")
urlList = urlFile.readlines()
 
run = 0
while run < runs:
    for server in servers:
        s = adns.init(adns.iflags.noautosys,sys.stderr, "nameserver " + server)
        if run == 0:
            resultsDataFile = open("DNS-Results-" + server + ".csv", "w")
        else:
            resultsDataFile = open("DNS-Results-" + server + ".csv", "a")
        count = 0
        quickestTime = 999999.9
        longestTime = 1.0
        averageTime = 999999.9
        totalTimeMS = 999999.9
        print "Server: " + server + ""
        print "Run: " + str(run + 1) + ""
        while count < queries:
            timeStart = time.time()
            resolve = s.synchronous(urlList[count].strip(), adns.rr.A)
            # For asynchronis queries use below line
            #resolve = s.submit(urlList[count].strip(), adns.rr.A)
            timeEnd = time.time()
            timeTaken = timeEnd - timeStart
            # Multiply by 1000 to get milliseconds from seconds. (Not sure windows has this kind of Granularity)
            timeTakenMS = timeTaken * 1000
            resultsDataFile.write(str(timeTakenMS) + "\n")
            count = count + 1
            if count % printCount == 0:
                print "Complete DNS Queries: " + str(count) + " "
        print "\n"
    run = run + 1
    resultsDataFile.close()
    print "\nRun " + str(run) + " complete\n"    
urlFile.close()
 
# At this point all data has been collected, now we just do the maths.
print "\n\nData recorded!\n"
print "\nProcessing... \n\n"
 
resultsFile = open("DNS-Results.txt", "w")
for server in servers:
    serverResultsFile = open("DNS-Results-" + server + ".csv", "r")
    serverResultsList = serverResultsFile.readlines()
    serverResultsList.sort()
    totalQueries = queries * runs
    totalQueryTime = 0
    for i in serverResultsList:
        totalQueryTime += float(i)
    medianPosition = totalQueries / 2
    median = serverResultsList[medianPosition].strip()
    meanQueryTime = totalQueryTime / totalQueries
    minQueryTime = serverResultsList[0].strip()
    maxQueryTime = serverResultsList[-1].strip()
    print ("Server: \t" + server)
    print ("Total Queries: \t" + str(totalQueries))
    print ("Total Time: \t" + str(totalQueryTime) + " ms")
    print ("Min Time: \t" + str(minQueryTime) + " ms")
    print ("Max Time: \t" + str(maxQueryTime) + " ms")
    print ("Mean Time: \t" + str(minQueryTime) + " ms (Average Time)")
    print ("Median Time: \t" + str(median) + " ms (Middle Value) \n\n")
    resultsFile.write("Server: \t" + server + "\n")
    resultsFile.write("Total Queries: \t" + str(totalQueries) + "\n")
    resultsFile.write("Total Time: \t" + str(totalQueryTime) + " ms" + "\n")
    resultsFile.write("Min Time: \t" + str(minQueryTime) + " ms" + "\n")
    resultsFile.write("Max Time: \t" + str(maxQueryTime) + " ms" + "\n")
    resultsFile.write("Mean Time: \t" + str(minQueryTime) + " ms (Average Time)" + "\n")
    resultsFile.write("Median Time: \t" + str(median) + " ms (Middle Value)" + "\n\n")
resultsFile.close()
 
totalEnd = time.time()
total = totalEnd - totalStart
print "Total time taken = " + str(total) + " seconds \n"
