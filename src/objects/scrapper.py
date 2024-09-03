import requests

class Scrapper():
    def __init__(self):
        '''Получение необходимых данных для подключения к БД(Notion)'''
        self.headers = None
    def api_request(self, param):
        match param:
            case '':
                pass

    def _read_text_block(self, page_id) :
        url = "https://api.notion.com/v1/blocks/{}/children"
        requests.get(url, headers=self.headers)
