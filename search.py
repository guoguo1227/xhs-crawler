import json
import requests
import sys
import time

from tool.util import get_headers, get_search_params, get_cookies, js

class Home:
    def __init__(self):
        self.cookies = get_cookies()
        self.headers = get_headers()
        self.params = get_search_params()
        self.url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"

    def search(self, keyword):
        # 遍历1-2页
        for i in range(1, 2):
            #替换搜索参数
            self.params['page'] = i
            self.params['keyword'] = keyword

            #替换请求header参数
            api = '/api/sns/web/v1/search/notes'
            ret = js.call('get_xsxt', api, self.params, self.cookies['a1'])

            self.headers['x-s'] = ret['X-s']
            self.headers['x-t'] = str(ret['X-t'])

            encodeData = json.dumps(self.params, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
            response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=encodeData)
            res = response.json()
            try:
                items = res['data']['items']
            except:
                print(f'搜索失败，结果为 {res}')
                sys.exit(1)
            #解析每条内容
            for note in items:
                try:
                    id = note['id']
                    title = note['note_card']['display_title']
                    userId = note['note_card']['user']['user_id']
                    print(f"小红书ID:{id},标题:{title},用户ID：{userId}")
                except Exception as e:
                    print(f"Catch an exception: {e}")
            #sleep防止被限
            time.sleep(5)

    def main(self):
        keyword = "AI"
        try:
            home.search(keyword)
        except Exception as e:
            print(f'搜索：{keyword}失败 {e}')

if __name__ == '__main__':
    home = Home()
    home.main()
