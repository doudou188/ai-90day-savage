class StudentManager(object):
    def __init__(self):
        self.students = []
    
    def add_student(self, name, score):
        student = {'name':name,'score':score}
        self.students.append(student)
        print(f'添加学生：{name},分数：{score}')

    def delete_student(self, name):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print(f'删除学生:{name}')
                return
        print(f'未找到学生：{name}')

    def update_student(self, name, new_score):
        for student in self.students:
            if student['name'] == name:
                student['score'] = new_score
                print(f'更新学生:{name},新分数：{new_score}')
                return
        print(f'未找到学生：{name}')

    def show_student(self):
        print('\n当前学生列表：')
        for student in self.students:
            print(f'姓名：{student['name']},分数:{student['score']}')
    
#测试代码
if __name__ == '__main__':
    manager = StudentManager()

    manager.add_student('张三', 90)
    manager.add_student('李四', 85)

    manager.show_student()

    manager.update_student('张三', 95)

    manager.delete_student('李四')

    manager.show_student()


