import Ui
import Data
while True:
    Data.init()
    Ui.home_page()
    select = int(input("请选择："))
    if select == 0:
        break
    elif select == 1:
        Ui.login_page()
        select1 = int(input("请选择："))
        if select1 == 0:
            continue
        if select1 == 1:
            Data.login()
        elif select1 == 2:
            Data.logout()
        elif select1 == 3:
            if Data.login_id == 1:
                Data.enroll()
            else:
                print("请登录管理员账号：")
                Data.login()
                if Data.login_id == 1:
                    Data.enroll()
        elif select1 == 4:
            if Data.login_id == 1:
                Data.delete()
            else:
                print("请登录管理员账号：")
                Data.login()
                if Data.login_id == 1:
                    Data.delete()
    elif select == 2:
        if Data.login_id == 1 or Data.login_id == 2:
            Data.save_student_info()
        else:
            print("请登录管理员或教师账号：")
            Data.login()
            if Data.login_id == 1 or Data.login_id == 2:
                Data.save_student_info()
    elif select == 3:
        Ui.info_page()
        select3 = int(input("请选择："))
        if select3 == 0:
            continue
        elif select3 == 1:
            Data.input_student_info(select3)
        elif select3 == 2:
            Data.input_student_info(select3)
    elif select == 4:
        Ui.revise_page()
        select4 = int(input("请选择："))
        if select4 == 0:
            continue
        elif select4 == 1:
            if Data.login_id == 1 or Data.login_id == 2:
                Data.revise_student_info(select4)
            else:
                print("请登录管理员或教师账号：")
                Data.login()
                if Data.login_id == 1 or Data.login_id == 2:
                    Data.revise_student_info(select4)
        elif select4 == 2:
            if Data.login_id == 1 or Data.login_id == 2:
                Data.revise_student_info(select4)
            else:
                print("请登录管理员或教师账号：")
                Data.login()
                if Data.login_id == 1 or Data.login_id == 2:
                    Data.revise_student_info(select4)
