import requests
import re


class Parser:
    def __init__(self):
        self.s = requests.Session()

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
            'cookie': '',
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

    def is_text_in(self, searching_word, incoming_text):
        re_query = '\\b{}\\b'.format(searching_word)
        if re.search(re_query, incoming_text):
            return True
        return False

    def get_messages(self, guid):
        page_size = 500

        query_data = '{"guid":"' + guid + '","pageSize":' + str(
            page_size) + ',"startRowIndex":0,"startDate":null,"endDate":null,"messageNumber":null,"bankruptMessageType":null,"bankruptMessageTypeGroupId":null,"legalCaseId":null,"searchAmReport":true,"searchFirmBankruptMessage":true,"searchFirmBankruptMessageWithoutLegalCase":false,"searchSfactsMessage":true,"searchSroAmMessage":true,"searchTradeOrgMessage":true,"sfactMessageType":null,"sfactsMessageTypeGroupId":null}'
        headers = {
            'method': 'POST',
            'scheme': 'https',
            'authority': 'fedresurs.ru',
            'path': '/backend/companies/publications',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://fedresurs.ru',
            'Cookie': '',
            'Content-Length': '455',
            'Accept-Language': 'ru',
            'Host': 'fedresurs.ru',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
            'Referer': 'https://fedresurs.ru/company/ca48285e-8e7c-43d0-aced-798b759c5949?attempt=1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'}
        res = self.s.post('https://fedresurs.ru/backend/companies/publications', data=query_data.encode('utf-8'),
                          headers=headers)
        res_json = res.json()
        number_of_messages = res_json["found"]
        if (int(number_of_messages) > page_size):
            # get all messages
            query_data = '{"guid":"ca48285e-8e7c-43d0-aced-798b759c5949","pageSize":' + number_of_messages + ',"startRowIndex":0,"startDate":null,"endDate":null,"messageNumber":null,"bankruptMessageType":null,"bankruptMessageTypeGroupId":null,"legalCaseId":null,"searchAmReport":true,"searchFirmBankruptMessage":true,"searchFirmBankruptMessageWithoutLegalCase":false,"searchSfactsMessage":true,"searchSroAmMessage":true,"searchTradeOrgMessage":true,"sfactMessageType":null,"sfactsMessageTypeGroupId":null}'
            res = self.s.post('https://fedresurs.ru/backend/companies/publications',
                              data=query_data.encode('utf-8'),
                              headers=headers)
            res_json = res.json()

        return res_json["pageData"]
