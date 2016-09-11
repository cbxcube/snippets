#!/usr/bin/env python3

# This script will parse details about weather from idnes.cz 
# using urrlib and regexp python3 modules

 
# imports


# url definitions
'''
Import of /usr/lib/python3.4/datetime.py is required to 
determine url for ppozitra, p3, p4, p5 items.
Item URL consist of baseurl+p1-5 string
'''


# daylinks tupples
'''
Tuples are faster than lists. if defining constant values
'''

today=datetime()
datetupple = ('dnes','zitra','p3','p4','p5')
seq=0
for i in datestring:
	seq+=1


	
baseurl = "http://pocasi.idnes.cz/"
dataurl = datestring

#dataurl = {'q':'basic',
#	  	   'submit':'search'}
'''
real urls on idnes.cz

pdnes = "http://pocasi.idnes.cz/?d=dnes"
pzitra = "http://pocasi.idnes.cz/?d=zitra"
ppozitra = "http://pocasi.idnes.cz/?d=13.9.2016%2015:00"
p3 = "http://pocasi.idnes.cz/?d=14.9.2016%2015:00"
p4 = 
p5 = 
'''

'''
page http://pocasi.idnes.cz?d=dnes offers strings containing
required data about current and next days. String contains 
also ling to weather gif.

String is here : 
	<p>
    <img class="fl" alt="jasno" src="http://g.idnes.cz/p/pocasi/chmi/j.gif">
    <span>úterý 29 °C</span>
    </p>
'''

# regexs 
 '''
Fastest way how to get weather data from idnes.cz is using regexp
This is eliminating overhead with url manipulation and date
counting for  
<span>úterý 29 °C</span>
'''
