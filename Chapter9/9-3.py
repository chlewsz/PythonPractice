from admin import Admin


# zhangsan = User('张', '三', 30, '男')
# zhangsan.describe_user()
# zhangsan.greet_user()
# zhangsan.increment_login_attempts()
# zhangsan.read_login_attempts()
# zhangsan.increment_login_attempts()
# zhangsan.read_login_attempts()
# zhangsan.increment_login_attempts()
# zhangsan.read_login_attempts()
# zhangsan.reset_login_attempts()
# zhangsan.read_login_attempts()



admin = Admin('admin', 'super', 30, '男')
admin.privileges.show_privileges()