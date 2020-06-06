import pycrunchbase, time, csv, simplejson as json, os, numpy as np,requests, json, re, urllib2, csv, os

# Add academic API code here
cb = pycrunchbase.CrunchBase('')

#make a list of founder hyperlinks from a csv file.  
#This file comes from the Crunchbase Daily CSV Export "People" spreadsheet.
founders = []
f = open('founders.csv', 'rU')
csv_f = csv.reader(f, dialect=csv.excel_tab)
for row in csv_f:
    founders.append(row[0])

education={}
jobs={}
founded_cos={}
bday={}
start={}
end={}

#Crunchbase API only allows 2500 requests per day
for i in range(2500):
	try:
		pers=cb.person(founders[i])
		bday[founders[i]]=pers.born_on
		print bday[founders[i]]
#Get all jobs from the founder's page
		r=len(pers.jobs)
		jobs[founders[i]]=[]
		start[founders[i]]=[]
		end[founders[i]]=[]
		#founders have multiple jobs and r is different for each person
		for j in range(r):
			try:
				jobs[founders[i]].append(pers.jobs[j])
				print jobs[founders[i]]
				start[founders[i]].append(pers.jobs[j].started_on)
				end[founders[i]].append(pers.jobs[j].ended_on)
			except Exception as error:
				print error
				continue
#Scrape the founded companies from the person's profile
		s=len(pers.founded_companies)
		founded_cos[founders[i]]=[]
		for k in range(s):
			try:
				founded_cos[founders[i]].append(pers.founded_companies[k])
				print founded_cos[founders[i]]
			except Exception as error:
				print error
				continue
#Scrape the education from each founder's profile
		t=len(pers.degrees)
		education[founders[i]]=[]
		for l in range(t):
			try:
				education[founders[i]].append(pers.degrees[t])
				print education[founders[i]]
			except Exception as error:
				print error
				continue
	except Exception as error:
			print error
			continue
	time.sleep(5)
		
#export jobs, degrees, birth dates, founded companies
test = open("bdays.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in bday.items():
    wr.writerow([key, value])
test.close()

test = open("jobs.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in jobs.items():
    wr.writerow([key, value])
test.close()

test = open("startdates.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in start.items():
    wr.writerow([key, value])
test.close()

test = open("enddates.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in end.items():
    wr.writerow([key, value])
test.close()

test = open("education.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in education.items():
    wr.writerow([key, value])
test.close()

test = open("foundedcos.csv", 'wb')
wr = csv.writer(test, dialect='excel')
for key, value in founded_cos.items():
    wr.writerow([key, value])
test.close()


