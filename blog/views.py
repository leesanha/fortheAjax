from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-id') # 객체 묶음 가져오기
    return render(request, 'blog/home.html', {'blogs':blogs})
    # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blogs 객체도 함께 넘겨주도록 하겠다.

def detail(request, blog_id) : 
    blog_detail = get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'blog/detail.html', {'blog':blog_detail})
    # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blog 객체도 함께 넘겨주도록 하겠다.


# C - new(새로운 글을 작성할 수 있는 공간 띄워주기)
def new(request):
    return render(request, 'blog/new.html')


# C - create(새로운 글 작성해주기)
def create(request):
    blog = Blog() # 객체 틀 하나 가져오기
    blog.title = request.GET['title']  # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 객체 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

#  U - edit(기존 글을 수정할 수 있는 페이지 띄워주기)
def edit(request,blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'blog/edit.html', {'blog':blog})

# U - update(기존 글 객체 가져와서 수정하기)
def update(request,blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.title = request.GET['title'] # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))


# D - delete(기존 글 객체 가져와서 삭제)
def delete(request, blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.delete()
    return redirect('home') # home 이름의 url 로