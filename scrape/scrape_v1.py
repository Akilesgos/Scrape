import requests
from bs4 import BeautifulSoup


base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc_url = 'Irvine,+CA'
current_page = 0
while current_page < 10:    #  loop for go throught all pages
  print (current_page)
  url = base_url + loc_url + '&start=' + str(current_page)
  yelp_r = requests.get(url)
  yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
  businesses = yelp_soup.findAll('div', {'class':"biz-listing-large"})
  base_url_for_ech = ''
  file_path = 'yelp-{loc_url}_3.txt'.format(loc_url=loc_url)
  with open (file_path, 'a') as texfiles:   #  write data to txt.file
    for item in businesses:    #  we get nessesery information
      movie_link = item.findAll('a', {'class':"biz-name js-analytics-click"})[0].get('href')
      base_url_for_personal_web = 'https://www.yelp.com'+ str(movie_link)
      print(base_url_for_personal_web)
      personal_web_requests = requests.get(base_url_for_personal_web)
      personal_web_soup = BeautifulSoup(personal_web_requests.text, 'html.parser')
      businesses_personal_web = personal_web_soup.findAll('div', {'class':"mapbox-text"})
      for data in businesses_personal_web:
        try:
          webpage = data.findAll('a',{'target':"_blank"})[0].text
          print(webpage)
        except:
          address = None
        phone = data.findAll('span',{'class':'biz-phone'})[0].text
        print(phone)
        try:
          address = data.findAll('address')[0].text
          print(address)
        except:
          address = None
        page_line = '{webpage}\n{phone}\n{address}\n'.format(
          webpage = webpage,
          phone = phone,
          address = address
            )
        texfiles.write(page_line)
  current_page+=10



  current_page = 0
  while current_page < 201:    #  loop for go throught all pages
    print (current_page)
    url = base_url + loc_url + '&start=' + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class':"biz-listing-large"})
    file_path = 'yelp-{loc_url}_2.txt'.format(loc_url=loc_url)
    with open (file_path, 'a') as texfiles: # write data to txt.file
      for biz in businesses:    #  we get nessesery information
        title = biz.findAll('a', {'class':'biz-name'})[0].text
        print (title)
        second_line = ''
        first_line = ''
        try:
          phone = biz.findAll('span',{'class':'biz-phone'})[0].getText().strip(" \n\t\r")
        except:
          phone = None
        print (phone)
        try:
          address = biz.findAll('address')[0].contents # search adress but mistake out of range
          for item in address:# get more cleaner data
            if 'br' in str(item):
              second_line += item.getText() # formating string
            else:
              first_line = item.strip(' \n\t\r') # formating string
          print (first_line)
          print (second_line)
        except:
          address = None
        page_line = '{title}\n{address_1}\n{address_2}\n{phone}\n'.format(
          title = title,
          address_1 = first_line,
          address_2 = second_line,
          phone = phone
          )
        texfiles.write(page_line)
    current_page+=10
print(look_up_loc('Irvine','CA'))


