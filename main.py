import bs4 as bs
import urllib.request
from prettytable import PrettyTable

state = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Punjab', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Rajasthan', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

i=1
for it in state:
    print(i,"-",it)
    i+=1

print("Enter the index number of the state whose weather information needs to be obtained")
j=int(input())
st=state[j-1]

source = urllib.request.urlopen("https://www.yr.no/place/India/"+st.replace(' ','_')).read()
soup = bs.BeautifulSoup(source,'lxml')
#print(soup)

tables = soup.find_all("tbody")
#print(tables[1])
#tab_row = tables.find_all("tr")
#tab_hdr = tables.find_all("th")
#print(tab_hdr)

tab_hdr = []
tab_row = []

for tr in tables:
    hdr = tr.find_all("th")
    for h in hdr:
        #tab_hdr.append(h.getText())
        tl = h.find_all("a")
        for y in tl:
            #print(y)
            tab_hdr.append(y.text)

#print(tab_hdr)
#t = PrettyTable(tab_hdr)
t = PrettyTable()
t.add_column("Cities:",["Temperature tomorrow:", "Day after tmrw:", "The next day:"])

ct = 0
for f in tables:
    tb = f.find_all("tr")
    for tr in tb:
        td = tr.find_all("span", {"class": ["temperature plus"]})
        col = []
        for i in td:
            col.append(i.text)
        #print(col)
        if(len(col)>0):
            t.add_column(tab_hdr[ct],col)
            ct+=1
print("\nThe weather forecast for important cities in the state for the next 3 days are as follows:\n")
print(t)

