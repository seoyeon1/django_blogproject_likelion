from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
#목록들을 얻어올 떄 내용을 못가져오면 404 error를 보여줌, req를 처리하고 보여주는 거
from .models import Blog, Comment
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BlogForm #forms.py의 BlogForm을 가져옴.
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
    if request.method == 'POST':    #입력된 내용을 처리(POST)

        form = BlogForm(request.POST)#POST방식으로 들어온 data를 form에 넣어줌.
        if form.is_valid():
        #is_valid(): 입력돼야할 값이 다 입력됐는지, 형식에 맞게 다 잘 입력됐는지 체크(T/F)
            blog = form.save(comment = False)
        #form에서 title, body만 입력받고 날짜시간은 함수에서 직접 받을예정. So, blog객체를 가져옴:O & 바로 save:X
            blog.pub_date = timezone.datetime.now()#현재 날짜&시간(form에서 입력 받지 않았음)
            blog.save() #save
            return redirect('detail', pk=blog.pk)

    else:    #빈 page를 보여줌(GET)
        form = BlogForm()#form에 빈 객체를 담음.
    return render(request, 'blog/create.html', {'form':form})
    #요청이 들어오면 빈 입력공간(form)을 보내줌.(사전형태)
    

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
        if request.method == 'POST':
            post_id = comment.post.id
            comment.delete()
            return redirect('/blog/' + str(post_id))
        return HttpResponse('잘못된접근')




    