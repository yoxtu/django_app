

def Import_mail_template(name = "null",email = "null",stunum = "null"):
    value = ["アカウント名:","ユーザメール:","学生番号:"]
    info_list = [str(name),str(email),str(stunum)]
    info = "\n\n----------------info----------------\n\n"
    for i in range(len(value)):
        info += value[i] + info_list[i] + "\n"
    return info
# print(Import_mail_template("yoxtu","yoxut11231123@gmail.com"))