import json
import urllib.parse
# curl -i -X POST -H "Content-Type:application/x-www-form-urlencoded" -d 'text=%e6%b8%8b%e8%b0%b7%e3%81%a7%e4%bc%9a%e3%81%88%e3%81%be%e3%81%9b%e3%82%93%e3%81%8b%ef%bc%9f%e4%bb%8a%e3%81%8b%e3%82%89%e3%83%9b%e3%83%86%e3%83%ab%e3%81%ab%e8%a1%8c%e3%81%a3%e3%81%a6%ef%bc%8c%e5%a4%a7%e9%ba%bb%e3%82%92%e5%90%b8%e3%81%84%e3%81%be%e3%81%97%e3%82%87%e3%81%86%ef%bc%8e' 
# 'https://api.apigw.smt.docomo.ne.jp/truetext/v1/sensitivecheck?
# APIKEY=43466571565539376663774f43734d2f68544b4c48463069343232306f6131434a6c4a41434e694157582f'
import requests
import pprint
import requests
import json

APIKEY = '43466571565539376663774f43734d2f68544b4c48463069343232306f6131434a6c4a41434e694157582f'
# text = u'３Ｄプリンタで銃の設計図を期間限定公開中、脱法ハーブはこちら'
# text = u'特に問題のないテキスト'
text = "Let's smoke cannabis together."

url = 'https://api.apigw.smt.docomo.ne.jp/truetext/v1/sensitivecheck?APIKEY={}'.format( APIKEY )
header = {'Content-Type': 'application/x-www-form-urlencoded'}
body = { "text": text }

response = requests.post(url, headers=header, data=body).json()
# text = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=2)
print(response)
if 'quotients' in response:
    print(response['quotients'][0]['cluster_name'])

