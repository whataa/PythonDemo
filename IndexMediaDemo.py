import urllib.parse
import urllib.request


def request_ajax_data(url, data, referer=None, **headers):
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
    if referer:
        req.add_header('Referer', referer)
    if headers:
        for k in headers.keys():
            req.add_header(k, headers[k])
    params = urllib.parse.urlencode(data).encode(encoding='UTF8')
    response = urllib.request.urlopen(req, params)
    jsonText = response.read()
    print(jsonText.decode("utf8"))
    # return json.loads(jsonText)


ajaxRequestBody = {
    "callCount": "1",
    "page": "/xww/news2_mt.html",
    "httpSessionId": "975427C79D9B08A548341A01E174503A",
    "scriptSessionId": "A483A99F4F9BA40117A6D93A1C2D9EEE430",
    "c0-scriptName": "newsAjax",
    "c0-methodName": "getXwlist",
    "c0-id": "0",
    "c0-param0": "string:infoCont_140590539291880913_145802377061914235",
    "c0-param1": "Object_Object:{}",
    "c0-param2": "string:1000020114",
    "batchId": "0",

}

ajaxResponse = request_ajax_data(
    'http://www.cdut.edu.cn/xww/dwr/call/plaincall/newsAjax.getXwlist.dwr',
    ajaxRequestBody,
)
