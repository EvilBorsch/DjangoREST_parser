import requests


class Parser:
    def __init__(self):
        self.s = requests.Session()
        self.cookie = ''

    def get_fedResourse_cookie(self):
        try:
            self.s.get('https://fedresurs.ru/')
        except requests.exceptions.SSLError:
            print("too many connects to fed resourse server")

        part_cookie = self.s.cookies.get('fedresurscookie')
        self.cookie = '_ym_uid=1590268569135036460; _ym_d=1590268569; _ym_isad=1; fedresurscookie={}; _ym_visorc_44970568=w'.format(
            part_cookie)
        print('cookie ', self.cookie)

    def get_companys_list_by_name(self, company_name):
        query_data = '{"entitySearchFilter":{"regionNumber":null,"onlyActive":true,"startRowIndex":0,"pageSize":15,"code":null,"name":"' + company_name + '","legalCase":null},"isCompany":null,"isFirmBankrupt":null,"isSro":null,"isFirmTradeOrg":null,"isSroTradePlace":null,"isTradePlace":null}'

        hed = {
            'authority': 'fedresurs.ru',
            'method': 'POST',
            'path': '/backend/companies/search',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,ru-GB;q=0.8,ru;q=0.7,en-US;q=0.6',
            'content-length': '264',
            'content-type': 'application/json',
            'cookie': self.cookie,
            'origin': 'https://fedresurs.ru',
            'referer': 'https://fedresurs.ru/search/entity?name=%25D1%2580%25D0%25BE%25D0%25BC%25D0%25B0%25D1%2588%25D0%25BA%25D0%25B0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        res2 = self.s.post('https://fedresurs.ru/backend/companies/search', data=query_data.encode('utf-8'),
                           headers=hed)
        json_data = res2.json()
        return json_data["pageData"]

    def get_guid(self, company_name):
        json_data = self.get_companys_list_by_name(company_name)
        page_data = json_data[0]  # because we looking only for first company ( I can parse all if u want)

        for i in page_data:
            print("key ", i, "val ", page_data[i])

        guid = page_data["guid"]
        return guid
