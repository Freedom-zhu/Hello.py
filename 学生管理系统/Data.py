import json
import os

login_id = 0
user = {}
student_list = []


def init():
    global user, student_list
    if os.path.exists("user.json"):
        f = open("user.json", "r", encoding='utf-8')
        user = json.loads(f.read())
        f.close()
    if os.path.exists("info.json"):
        f = open("info.json", "r", encoding='utf-8')
        student_list = json.loads(f.read())
        f.close()


def save_file():
    f = open("user.json", "w", encoding='utf-8')
    f.write(json.dumps(user, ensure_ascii=False))
    f.close()
    f = open("info.json", "w", encoding='utf-8')
    f.write(json.dumps(student_list, ensure_ascii=False))
    f.close()


def login():
    global login_id
    login_id = 0
    name = input("请输入用户名：")
    password = int(input("请输入密码："))
    for user_name in user:
        if user_name == name:
            if password == user[user_name]:
                if user_name == "admin":
                    login_id = 1
                else:
                    login_id = 2
            else:
                print("密码错误")
    if login_id == 1:
        print("管理员登录")
    elif login_id == 2:
        print("教师登录")
    elif login_id == 0:
        print("未找到该用户")


def logout():
    global login_id
    login_id = 0
    print("退出成功")


def enroll():
    global user
    name = input("请输入注册用户名：")
    password = int(input("请输入注册的密码："))
    if name in user:
        print("用户存在")
    else:
        user[name] = password
        save_file()
        print("注册成功")


def delete():
    global user
    name = input("请输入要删除的用户名：")
    if name in user:
        del user[name]
        save_file()
        print("删除成功")
    else:
        print("用户不存在")


def save_student_info():
    global student_list
    name = input("请输入学生姓名：")
    student_class = input("请输入学生班级：")
    grades = input("请输入学生成绩：")
    student_id = input("请输入学生学号：")
    all_student_id = all_student()
    if student_id not in all_student_id:
        data = {
            'name': name,
            'student_class': student_class,
            'grades': grades,
            'student_id': student_id
        }
        student_list.append(data)
    else:
        print("学生信息重复")
    save_file()
    print("保存成功")


def all_student():
    all_student_id = []
    for student in student_list:
        all_student_id.append(student["student_id"])
    return all_student_id


def input_student_info(select):
    global student_list
    if select == 1:
        print("%-15s\t%-15s\t%-15s\t%-15s\t" % ("name", "class", "grades", "student_id"))
        for student in student_list:
            print("%-15s\t%-15s\t%-15s\t%-15s\t" \
                  % (student["name"], student["student_class"], student["grades"], student["student_id"]))
    else:
        inquire_id = input("请输入学号：")
        num = 0
        print("%-15s\t%-15s\t%-15s\t%-15s\t" % ("name", "class", "grades", "student_id"))
        for student_id in all_student():
            if inquire_id == student_id:
                print("%-15s\t%-15s\t%-15s\t%-15s\t" \
                      % (student_list[num]["name"], student_list[num]["student_class"],\
                         student_list[num]["grades"], student_list[num]["student_id"]))
            else:
                num += 1


def revise_student_info(select):
    inquire_id = input("请输入学号：")
    num = 0
    global student_list
    if inquire_id not in all_student():
        print("没有该学生")
    else:
        for student_id in all_student():
            if inquire_id == student_id and select == 1:
                print("请输入修改后的信息:")
                name = input("请输入学生姓名：")
                student_class = input("请输入学生班级：")
                grades = input("请输入学生成绩：")
                student_list[num]["name"] = name
                student_list[num]["student_class"] = student_class
                student_list[num]["grades"] = grades
                save_file()
                print("修改成功")
            elif inquire_id == student_id and select == 2:
                del student_list[num]
                save_file()
                print("删除成功")
            else:
                num += 1
