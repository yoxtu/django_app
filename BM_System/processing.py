
def Import_mail_template(name = "null",email = "null",stunum = "null"):
    value = ["アカウント名:","ユーザメール:","学生番号:"]
    info_list = [str(name),str(email),str(stunum)]
    info = "\n\n----------------info----------------\n\n"
    for i in range(len(value)):
        info += value[i] + info_list[i] + "\n"
    return info
# print(Import_mail_template("yoxtu","yoxut11231123@gmail.com"))

# title,title→[title,title]
def make_list(book_title=""):
    book_title = str(book_title)
    list_title = book_title.split(",")
    return list_title

def make_text(book_list):
    date = str(book_list[0])
    for i in range(1,len(book_list)):
        date += "," + str(book_list[i])
    return date
    
# Profile_obj_book_title_Prototype = "状態確認用No.100000"

# print("1" + Profile_obj_book_title_Prototype)

# Profile_obj_book_title = "状態確認用No.64328467"

# lender_list = make_list(Profile_obj_book_title_Prototype)

# print("2" + str(lender_list))

# if len(lender_list) < 3:
#     lender_list.append(Profile_obj_book_title)
#     print("3" + str(lender_list))
#     print( "4" + make_text(lender_list))




