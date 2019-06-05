from django.shortcuts import render, get_object_or_404, redirect, HttpResponse#목록들을 얻어올 떄 내용을 못가져오면 404 error를 보여줌, req를 처리하고 보여주는 거
from .models import Blog, Comment
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
#template

def home(request):
    blogs = Blog.objects#admin에서 쓴 글목록들을 blogs라고 알려줌?
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3) #blog list를 3개씩 구분
    page = request.GET.get('page') #req한 페이지를 get방식으로 얻어온 page라는 변수에 넣고
    posts = paginator.get_page(page)#가져온 페이지가 뭔가 post로 
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})#blogs라는 키값을 blogs라는 value값으로 사용
# @login_required
def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() #Blog class의 객체 blog
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#현재
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))
    return render(request, 'edit.html', {'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')
@login_required
def comment_add(request, blog_id):
    if request.method == 'POST':
        post = Blog.objects.get(pk = blog_id)
        comment =Comment()
        comment.user = request.user
        comment.body = request.POST['body']
        comment.post = post
        comment.save()
        return redirect('/blog/' + str(blog_id))
    else:
        return HttpResponse('잘못된 접근')
@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.body = request.POST['body']
            comment.save()
            return redirect('/blog/' + str(comment.post.id))
        elif request.method=='GET':
            context = {
                'comment' : comment
            }
            return render(request, 'comment_edit.html', context)
@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
            comment.delete()
            return redirect('/blog/' + str(comment.post.id))




    