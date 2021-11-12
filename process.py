import pandas as pd 
import regex


#Read the scraped data and store it in a dataframe 
d = pd.read_csv('scrape_results.csv')
info = d['list1_selection2'] #The info contains Ip, web host provider name, and the country location
#print(info)

ipaddr = []
country = []
webhosts = []

#Process the scarped data to extract the web hosts, Ip addr, and country 
for j in range(len(info)):
    i = info[j]
    #print(i)
    web = re.search('\n(.*)\n',i)
    web2 = web.group(1)
    webhosts.append(web2)
    addr = re.search("IP Address:(.*)",i)
    #print(addr)
    addr2 = addr.group(1).split()
    #print(addr2)
    length = len(addr2)
    ip1 = addr2[0]
    ipaddr.append(ip1)
    loc = addr2[length-1][:-1]
    country.append(loc)

#print(webhosts)
#print(ipaddr)
#print(country)

#Represent the extracted information in a dataframe
data = {'Web host': webhosts, 'IP Address': ipaddr, 'Country': country}
newdf = pd.DataFrame(data)
print(newdf)