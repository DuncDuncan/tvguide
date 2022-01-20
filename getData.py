channels = ['Rai 1', 'Rai 2', 'Rai 3', 'Rete 4', 'Canale 5', 'Italia 1', 'La 7', 'TV 8', 'Nove', '20 Mediaset', 'Rai 4', 'Iris', 'Rai 5', 'Rai Movie', 'Rai Premium', 'Cielo', 'La 7d', 'La 5', 'Real Time', 'Focus', 'Giallo', 'Top Crime', 'Dmax', 'Rai Storia', 'Mediaset Extra', 'Italia 2', 'Blaze', 'Boing', 'Boomerang', 'Caccia & Pesca', 'Comedy Central', 'Crime Investigation', 'Dea Junior', 'Dea Kids', 'Discovery', 'Discovery Science', 'Eurosport 1', 'Eurosport 2', 'Food Network', 'Fox', 'Gambero Rosso', 'History', 'LaEffe', 'Nat Geo Wild', 'National Geographic', 'Nick Junior', 'Nickelodeon', 'Pesca & Caccia', 'Primafila 1', 'Primafila 2', 'Primafila 3', 'Primafila 4', 'Primafila 5', 'Rai Gulp', 'Rai Scuola', 'Rai Sport', 'Rai Sport +', 'Rai Yoyo', 'Rsi La1', 'Rsi La2', 'Sky Atlantic', 'Sky Cinema Action', 'Sky Cinema Collection', 'Sky Cinema Comedy', 'Sky Cinema Drama', 'Sky Cinema Due', 'Sky Cinema Family', 'Sky Cinema Romance', 'Sky Cinema Suspence', 'Sky Cinema Uno', 'Sky Sport', 'Sky Sport Arena', 'Sky Sport F1', 'Sky Sport Football', 'Sky Sport MotoGP', 'Sky Sport NBA', 'Sky Sport Uno', 'Sky Uno', 'Tg Com 24']

import requests

import xml.etree.ElementTree as ET



def fetch():
  print ('fetch start')

  url = "http://116.202.210.205/test/it_generic_full_lite.xml"
  #url = "https://www.w3schools.com/xml/cd_catalog.xml"

  xml_data = requests.get(url).content

  xml_data = str(xml_data)

  xml_data.replace("b'","")
  xml_data.replace("</tv>'","")

  xml_data = xml_data[2:len(xml_data)-1]

  print(xml_data[0:100])
  print('fetch end')

  return xml_data

  #f = open("data.txt", "w")
  #f.write(xml_data)
  #f.close()




def reduce(xml_data):
  #print ('meow',xml_data[0:10])
  #tree = ET.parse('data.txt')
  
  #tree = ET.parse(xml_data)
  #root = tree.getroot()
  root = ET.fromstring(xml_data)

  s0 = '<TV>'
  for channel in channels:
    print (channel)
    s = ''
    for x in root:
      if x.tag=="programme":
        if x.attrib["channel"]==channel:
          y = str(ET.tostring(x))
          s += y[2:len(y)-1]
    s0 += s
  s0 += '</TV>'
  
  #s0  = s0.decode('string_escape')
  s0 = s0.replace('\\','')

  f = open("data.txt", "w")

  #print (s0[0:10])
  
  f.write(s0)


  #print ('reduce end')
 


data = fetch()

reduce(data)
