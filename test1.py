@csrf_exempt#关闭CSRF检查
def users(request):
    # request.encoding = 'utf-8'
    print(request.GET.get('q'))#无参数则为None,1ky对多value时,默认取最后一个value
    print(len(request.GET))##可判断某请求的参数
    print(request.GET)#
    print(request.POST)#参数字典
    print(request)#所有信息
    print(request.path)#请求path
    print(request.method)#请求方法
    print(request.META)#header
    print(request.COOKIES)#cookie
    print(request.FILES)#附件
    print(request.is_secure())
    if 'q' in request.GET:
        userSet = User.objects.all()
        message = userSet[0].username + '你搜索的内容为: ' + request.GET['q'].encode('utf-8').decode('utf-8')
    else:
        message = '你提交了空表单'
    return HttpResponseServerError(message)

def error(request):
    pass
    HttpResponseNotFound('')
    HttpResponseForbidden('')
    HttpResponseServerError('')