from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog_m
from django.utils import timezone
from .form import Blog_f

# Create your views here.
def begin(request):
    writings = Blog_m.objects.all() # writings란 변수에 우리가 만든 table의 모든 객체들 저장.
    return render(request, 'begin.html', {'writings':writings})

#Read
def detail(request,blog_id):
    select = get_object_or_404(Blog_m,pk = blog_id) #해당 키의 객체를 select에 담는다.
    return render(request, 'detail.html',{'select':select})

#Creat
def new(request):
    # editing = 0
    # return render(request, 'new.html',{'editing':editing})
#입력받은걸 넘기는 작업
    if request.method == 'POST':
        input_obj = Blog_f(request.POST, request.FILES)
        if input_obj.is_valid(): #전달받은 form값이 유효하다면 True 반환
            temp_save = input_obj.save(commit = False) #임시저장
            temp_save.pub_date = timezone.datetime.now()
            temp_save.save()
            return redirect ('begin')

#begin.html -> new.html로 넘어가는 작업. method 는 get
    else:
        form_obj = Blog_f()
        return render (request, 'new.html', {'form_obj':form_obj})
        

def create(request):
    new_writing = Blog_m() #객체 생성
    new_writing.title = request.POST['title']           #new.html에서 create로 보낸 data를 Post 방식으로 받아서 
    new_writing.body = request.POST['body']             #해당 객체의 table(해당하는 column들)안에 넣어줌.
    new_writing.pub_date = timezone.datetime.now()
    new_writing.save() #table 저장.
    return redirect('/blog/' + str(new_writing.id))

# Update
# def edit(request, select_id):
#     edit_writing = get_object_or_404(Blog_m, pk = select_id) #선택된 객체 불러오기
#     editing = 1
#     # select_id = select_id
#     return render(request, 'new.html', {'edit_writing':edit_writing,'editing':editing, 'select_id':select_id})
# # def update(request, select_id):

def edit (request, select_id):
    edit_writing = get_object_or_404(Blog_m, pk = select_id)
    return render(request, 'edit.html', {'edit_writing' : edit_writing})

def update(request, select_id):
    edit_writing = get_object_or_404(Blog_m, pk = select_id)
    edit_writing.title = request.POST['edit_title']
    edit_writing.body = request.POST['edit_body']
    edit_writing.pub_date = timezone.datetime.now()
    edit_writing.save()
    return redirect('/blog/' + str(select_id))

# Delete
def delete(request,select_id):
    item = get_object_or_404(Blog_m, pk = select_id)
    item.delete()
    return redirect('/')

