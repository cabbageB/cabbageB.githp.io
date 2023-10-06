from pymysql import Connection


class MysqlUtil:
    def __init__(self):
        # 获取到mysql数据库的连接对象
        self.cone = Connection(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 默认端口为3306
            user='root',  # 默认账户名
            password='hdl',  # 登录密码
            autocommit=True
        )


    def getInformation_dict(self):
        """
        获取数据库信息，返回学生字典列表
        :param cone: 数据库连接对象
        :return: dict
        """
        self.cursor = self.cone.cursor()
        self.cone.select_db("student")

        # 使用游标对象执行执行sql语句
        self.cursor.execute("SELECT *FROM test")
        # 获取查询结果
        results = self.cursor.fetchall()

        studentList = []
        for result in results:
            student_dict = {
                "姓名": result[0],
                "性别": result[1],
                "年龄": result[2],
                "学号": result[3],
                "电话": result[4],
                "家庭地址": result[5]
            }
            studentList.append(student_dict)
        return studentList

    # 删除数据库中的指定学生
    def dele_student(self, name: str):
        self.cursor.execute(f"DELETE FROM test WHERE 姓名='%s'" % name)

    # 新增学生到数据库中
    def add_student(self, stu_tuple: tuple):
        self.cursor.execute(f"INSERT INTO test VALUES('%s','%s',%d,'%s','%s','%s')" % stu_tuple)

    # 修改数据库中的学生信息
    def update_student(self, name: str, stu_tuple: tuple):
        self.cursor.execute(f"UPDATE test SET `姓名` = '{stu_tuple[0]}',"
                            f"`性别` = '{stu_tuple[1]}',"
                            f"`年龄` = {stu_tuple[2]},"
                            f"`学号` = '{stu_tuple[3]}',"
                            f"`电话` = '{stu_tuple[4]}',"
                            f"`家庭地址` = '{stu_tuple[5]}'"
                            f" WHERE `姓名` = '{name}'")


if __name__ == '__main__':
    cone = MysqlUtil()
    studentList = cone.getInformation_dict()
    print(studentList)
