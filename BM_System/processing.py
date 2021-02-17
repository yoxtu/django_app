import uuid

# make mail_info
def Import_mail_template(name = "null",email = "null",stunum = "null"):
    value = ["アカウント名:","ユーザメール:","学生番号:"]
    info_list = [str(name),str(email),str(stunum)]
    info = "\n\n----------------info----------------\n\n"
    for i in range(len(value)):
        info += value[i] + info_list[i] + "\n"
    return info
# print(Import_mail_template("yoxtu","yoxut11231123@gmail.com"))

# str,str → list
def make_list(book_title=""):
    if book_title == '':
        return []
    else:
        book_title = str(book_title)
        list_title = book_title.split(",")
        return list_title

print(make_list("None"))

# list → str,str
def make_text(book_list):
    if book_list == []:
        return ''
    date = str(book_list[0])
    for j in range(1,len(book_list)):
        date += "," + str(book_list[j])
    return date

# list内のデータが引数の単語と一致する場合:F
# list内のデータが引数の単語と一致しない場合:T
def serch_list(id_list,obj_id):
    for k in id_list:
        if k == obj_id:
            return False
    return True

# make token
def set_submit_token(request):
    #ハッシュ値生成
    submit_token = str(uuid.uuid4())
    #セッションにトークンを格納
    request.session['submit_token'] = submit_token
    #クライアント用に同じ値のトークンを返す
    return submit_token

# check token
def exist_submit_token(request):
    #クライアントから送信されたトークンを取得
    token_in_request = request.POST.get('submit_token')
    #一度使用したトークンをセッションから破棄
    token_in_session = request.session.pop('submit_token', '')

    if not token_in_request:
        return False    
    if not token_in_session:
        return False

    return token_in_request == token_in_session

def list_check(t_list,check = None):
    re_list = []
    for l in t_list:
        if str(l) != str(check):
            re_list.append(l)
    
    return re_list

