# 作者：hogwarts_cy
# 时间：2023/10/31 9:51


"""
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息

1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*				学生管理系统			 *")
    print("*  	    1. 添加新学生信息              *")
    print("* 	    2. 通过学号修改学生信息		 *")
    print("*		3. 通过学号删除学生信息		 *")
    print("*		4. 通过姓名删除学生信息		 *")
    print("* 	    5. 通过学号查询学生信息          *")
    print("*		6. 通过姓名查询学生信息          *")
    print("*		7. 显示所有学生信息             *")
    print("*		8. 退出系统			  		 *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
"""

# 使用列表保存所有学生信息的列表
students = []


# 定义一个用来显示菜单的函数
def menu():
    print("****************************************")
    print("*				学生管理系统			  *")
    print("*  	    1. 添加新学生信息                *")
    print("* 	    2. 通过学号修改学生信息		   *")
    print("*		3. 通过学号删除学生信息		   *")
    print("*		4. 通过姓名删除学生信息		   *")
    print("* 	    5. 通过学号查询学生信息           *")
    print("*		6. 通过姓名查询学生信息           *")
    print("*		7. 显示所有学生信息              *")
    print("*		8. 退出系统			  		  *")
    print("****************************************")


# 定义一个启动函数，用来管理学生管理系统的所有代码。
# 每一个选项都会使用一个函数来完成，通过start()函数进行管理。
# 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
def start():
    while True:
        menu()
        select_op = input("输入编号选择操作：")
        if select_op == "1":
            sid = input("请输入学号：")
            name = input("请输入姓名：")
            age = input("请输入年龄：")
            gender = input("请输入性别：")
            add_student(sid, name, age, gender)

        elif select_op == "2":
            sid = input("请输入需要修改信息的学生学号：")
            modify_student(sid)

        elif select_op == "3":
            sid = input("请输入需要删除的学生学号：")
            delete_student_by_sid(sid)

        elif select_op == "4":
            name = input("请输入需要删除的学生姓名：")
            delete_student_by_name(name)

        elif select_op == "5":
            sid = input("请输入需要查询的学生学号：")
            search_student_by_sid(sid)

        elif select_op == "6":
            name = input("请输入需要查询的学生姓名：")
            search_student_by_name(name)

        elif select_op == "7":
            show_all_student()

        elif select_op == "8":
            break
        else:
            print("请输入正确的数字！")


# 选项 1. 添加新学生信息
def add_student(sid, name, age, gender):
    for student in students:
        if sid == student['sid']:
            print("该学生已存在，请重新添加！")
            return False    # 学号重复，添加失败

        try:
            sid = int(sid)
        except ValueError:
            print("学号必须为整数，请输入正确的学号！")
            return False    # 学号为非整数，添加失败

        if not name:
            print("姓名不能为空，请输入正确的姓名！")
            return False    # 姓名为空，添加失败

        try:
            age = int(age)
        except ValueError:
            print("年龄必须为整数，请输入正确的年龄！")
            return False    # 年龄为非整数，添加失败

        if not gender:
            print("性别不能为空，请输入正确的性别！")
            return False    # 性别为空，添加失败

    # 每个学生信息使用字典形式保存
    new_student = {
        'sid': sid,
        'name': name,
        'age': age,
        'gender': gender
    }
    students.append(new_student)
    print(f"添加学生成功：学号{sid}，姓名{name}，年龄{age}，性别{gender}")
    return True # 添加成功


# 选项 2. 通过学号修改学生信息
def modify_student(sid):
    for student in students:
        if sid == student['sid']:
            new_name = input("请输入新的姓名：")
            new_age = input("请输入新的年龄：")
            new_gender = input("请输入新的性别：")
            student['name'] = new_name
            student['age'] = new_age
            student['gender'] = new_gender

            if not new_name:
                print("姓名不能为空，请输入正确的姓名！")
                return False    # 姓名为空，修改失败

            try:
                new_age = int(new_age)
            except ValueError:
                print("年龄必须为整数，请输入正确的年龄！")
                return False    # 年龄为非整数，修改失败

            if not new_gender:
                print("性别不能为空，请输入正确的性别！")
                return False    # 性别为空，修改失败

            print(f"学号{sid}学生的信息修改成功！")
            return True # 修改成功

    print("该学生不存在，请重新输入！")
    return False    # 学号不存在，修改失败


# 选项 3. 通过学号删除学生信息
def delete_student_by_sid(sid):
    for student in students:
        if sid == student['sid']:
            students.remove(student)
            print(f"学号{sid}的学生已经删除成功！")
            return True     # 删除成功
    print("该学生不存在，请重新输入！")
    return False    # 学号不存在，删除失败


# 选项 4. 通过姓名删除学生信息
def delete_student_by_name(name):
    count = 0   # 用来记录删除成功的学生数量
    for student in students[:]:
        if student["name"] == name:
            students.remove(student)
            count += 1
    if count > 0:
        print(f"学生{name}删除成功")
        return True  # 删除成功
    print("该学生不存在，请重新输入！")
    return False  # 姓名不存在，删除失败


# 选项 5. 通过学号查询学生信息
def search_student_by_sid(sid):
    for student in students:
        if sid == student['sid']:
            print(f"查询学生信息为：学号{sid}，"
                  f"姓名{student['name']}，"
                  f"年龄{student['age']}，"
                  f"性别{student['gender']}")
            return True     # 查询成功
    print("该学生不存在，请重新输入！")
    return False    # 学号不存在，查询失败


# 选项 6. 通过姓名查询学生信息
def search_student_by_name(name):
    found_students = []     # 用来记录查询的学生信息
    for student in students:
        if student["name"] == name:
            found_students.append(student)
    if found_students:
        print('查询学生信息为：')
        for student in students:
            print(f"学号：{student['sid']}，"
                  f"姓名：{student['name']}，"
                  f"年龄：{student['age']}，"
                  f"性别：{student['gender']}")
        return found_students   # 查询成功
    print("该学生不存在，请重新输入！")
    return None  # 姓名不存在


# 选项 7. 显示所有学生信息
def show_all_student():
    if len(students) == 0:
        print("暂无学生记录！")
    else:
        print('查询学生信息为：')
        for student in students:
            print(f"学号：{student['sid']}，"
                  f"姓名：{student['name']}，"
                  f"年龄：{student['age']}，"
                  f"性别：{student['gender']}")


if __name__ == '__main__':
    start()
