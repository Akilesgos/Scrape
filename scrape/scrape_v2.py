import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc_url = 'Irvine,+CA'  # we gdivede url by 2-3 path 1) base_url without
# querry 2) querry 3) pages
current_page = 0
while 201 > current_page:  # loop for go throught all pages
    print(current_page)
    url = base_url + loc_url + '&start=' + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class': "biz-listing-large"})
    file_path = 'yelp-{loc_url}_2.txt'.format(loc_url=loc_url)
    with open(file_path, 'a') as texfiles:  # write data to txt.file
        for biz in businesses:  # we get nessesery information
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            #  take all titles from web
            print(title)
            second_line = ''
            first_line = ''
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[
                    0].getText().strip(" \n\t\r")
            except:
                phone = None
            print(phone)
            try:
                address = biz.findAll('address')[
                    0].contents  # search adress but mistake out of range
                for item in address:  # get more cleaner data
                    if 'br' in str(item):
                        second_line += item.getText()  # formating string
                    else:
                        first_line = item.strip(' \n\t\r')  # formating string
                print(first_line)
                print(second_line)
            except:
                address = None
            page_line = '{title}\n{address_1}\n{address_2}\n{phone}\n'.format(
                title=title,
                address_1=first_line,
                address_2=second_line,
                phone=phone
                )
            texfiles.write(page_line)
    current_page += 10


def look_up_loc(city, state=None):
    base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
    firs_city = str(city)
    if state is None:
        first_state = ''
    else:
        first_state = str(state)
    loc_url = firs_city + ',+' + state
    current_page = 0
    while current_page < 201:    # loop for go throught all pages
        print(current_page)
        url = base_url + loc_url + '&start=' + str(current_page)
        yelp_r = requests.get(url)
        yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
        businesses = yelp_soup.findAll('div', {'class': "biz-listing-large"})
        file_path = 'yelp-{loc_url}_2.txt'.format(loc_url=loc_url)
        with open(file_path, 'a') as texfiles:    #  write data to txt.file
            for biz in businesses:    #  we get nessesery information
                title = biz.findAll('a', {'class': 'biz-name'})[0].text
                #  take all titles from web
                print(title)
                second_line = ''
                first_line = ''
                try:
                    phone = biz.findAll('span', {'class': 'biz-phone'})[
                        0].getText().strip(" \n\t\r")
                except:
                    phone = None
                print(phone)
                try:
                    address = biz.findAll('address')[0].contents
                    for item in address:    #  get more cleaner data
                        if 'br' in str(item):
                            second_line += item.getText()    # formating string
                        else:
                            first_line = item.strip(
                                ' \n\t\r')    #  formating string
                    print(first_line)
                    print(second_line)
                except:
                    address = None
                page_line = '{title}\n{address_1}\n{address_2}\n{phone}\n'.format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    phone=phone
                    )
                texfiles.write(page_line)
        current_page += 10

print(look_up_loc('Irvine', 'CA'))


    #   the same result
def look_up_loc(city, state=None):
    global empty_address
    base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
    firs_city = str(city)
    if state == None:
        first_state = ''
    else:
        first_state = str(state)
    loc_url = firs_city + ',+' + state
    current_page = 0
    while current_page < 201:
        #  loop for go throught all pages
        print(current_page)
        url = base_url + loc_url + '&start=' + str(current_page)
        yelp_r = requests.get(url)
        yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
        businesses = yelp_soup.findAll('div', {'class': "biz-listing-large"})
        file_path = 'yelp-{loc_url}_2.txt'.format(loc_url=loc_url)
        with open(file_path, 'a') as texfiles:    #  write data to txt.file
            for biz in businesses:    #  we get nessesery information
                title = biz.findAll('a', {'class': 'biz-name'})[0].text
                #  take all titles from web
                print(title)
                second_line = ''
                first_line = ''
                try:
                    phone = biz.findAll('span', {'class': 'biz-phone'})[
                        0].getText().strip(" \n\t\r")
                except:
                    phone = None
                print(phone)
                try:
                    if len(biz.findAll('address')) > 0:
                        address = biz.findAll('address')[
                            0].contents
                        for item in address:  # get more cleaner data
                            if 'br' in str(item):
                                second_line += item.getText()
                                #  formating string
                            else:
                                first_line = item.strip(
                                    ' \n\t\r')
                                #  formating string
                        print(second_line)
                        print(first_line)
                    else:
                        empty_address = \
                        biz.findAll('div', {'class': "biz-parent-container"})[
                            0].text
                        print(empty_address)
                except:
                    empty_address = None
                page_line = '{title}\n{address_1}\n{address_2}\n{empty_address}\n{phone}\n'.format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    empty_address=empty_address,
                    phone=phone
                    )
                texfiles.write(page_line)
        current_page += 10


print(look_up_loc('Irvine', 'CA'))


for key in db:
    print(key, '=>', db[key])
