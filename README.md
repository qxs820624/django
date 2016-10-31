http://www.cnblogs.com/huangxm/p/5770735.html
django-admin.py startproject perm_test
cd perm_test
python manage.py startapp school

同步到数据库并创建superuser:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

启动服务
manage.py runserver


http://localhost:8000/admin 创建用户， 赋予staff_status权限可以登录

http://localhost:8000/school/students/ 查看student页面

用户权限的详细解释
http://www.cnblogs.com/esperyong/archive/2012/12/20/2825909.html
