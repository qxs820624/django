#coding=utf-8

from django.shortcuts import render

# Create your views here.
from blog.models import Blogs, Author
from django.shortcuts import render_to_response
from django.template import RequestContext

def ShowBlogs(request):
	userinfo = Author.objects.first()
	blog_list = Blogs.objects.all().order_by('-publish_time')
	#print(blog_list)
	for blog in blog_list:
		print(', '.join(['%s:%s' % item for item in blog.__dict__.items()]))
	return render_to_response('blog_index.html')
	#return render_to_response('blogs.html', {'userinfo': userinfo, 'blogs':blog_list}, context_instance=RequestContext(request))

def Create(request):
	return

def Modify(request):
	return


def Delete(request):
	return

#----------------------------------------------------------------------
def Article(request, blog_id = ""):
	""""""
	#title=request.POST["blog_title"]
	#author=request.POST["blog_author"]
	userinfo = Author.objects.first()
	blog_list = Blogs.objects.get(id = blog_id)
	return render_to_response('article.html',{'userinfo': userinfo,'article':blog_list})

#----------------------------------------------------------------------
def ArticleByAuthor(request, blog_author = ""):
	""""""
	#title=request.POST["blog_title"]
	#author=request.POST["blog_author"]
	userinfo = Author.objects.first()
	blog_list = Blogs.objects.filter(blog_author__nickname__exact = blog_author)
	return render_to_response('article.html',{'userinfo': userinfo,'article':blog_list})



def lists(request):
	return render(request, 'python_list.html')


def news(request):
	return render(request, 'news.html')

def python(request):
	python_blog = BlogBody.objects.filter(blog_type='Python')[::-1]
	return render(request, 'python_list.html', {'python_blog': python_blog})


def abouttest(request):
	test_blog = BlogBody.objects.filter(blog_type='abouttest')[::-1]
	return render(request, 'test_list.html', {'test_blog': test_blog})


def mytalk(request):
	mytalk_blog = BlogBody.objects.filter(blog_type='mytalk')[::-1]
	return render(request, 'mytalk_list.html', {'mytalk_blog': mytalk_blog})


def diary(request):
	diary_blog = BlogBody.objects.filter(blog_type='diary')[::-1]
	return render(request, 'diary_list.html', {'diary_blog': diary_blog})


# 新增文章时调用add_article跳转新增页面,sub_article则吧新增文章处理后自动跳转到文章内容页详情
def add_article(request):
	return render(request, 'add_article.html')


def sub_article(request):
	cursor = connection.cursor()
	if request.method == 'POST':
		mytype = request.POST['article_type']
		title = request.POST['article_title']
		# body = markdown(request.POST['article_editor'])
		body = request.POST['article_editor']
		markdown = request.POST['article_markdown']
		print(markdown)
		updb = BlogBody(blog_title=title, blog_ismarkdown=markdown, blog_body=body, blog_type=mytype, blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='点点寒彬', blog_clicknum=1, blog_like=0)
		updb.save()
		cursor.execute('select max(id) from grzx_blogbody where blog_type = %s ', [mytype])
		new_id = cursor.fetchone()
		return redirect('/grzx/article/' + str(new_id[0]) + '/')


# 处理文章删除和编辑
def del_article(request, blog_body_id):
	BlogBody.objects.get(id=blog_body_id).delete()
	return redirect('/')


def edit_article(request):
	pass
