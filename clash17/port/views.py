from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from port.models import Users,Question

# Create your views here.

def home(request):
	return render(request,'loginpage.html')

def signup(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		if User.objects.filter(username=username).exists() is False:
			user = User.objects.create_user(username = username, password = password)
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				user1 = Users.objects.create(username = username, password = password, user = user)
				user1.save()
				return render(request, 'questionpage.html')
			else:
				return render(request,'loginpage.html',{'message':'Caanot be authenticated!'})
		else:
			return render(request, 'loginpage.html', {'message': 'Username exists!'})


def log_in(request):
	if request.method=="POST":	
		username = request.POST['username1']
		password = request.POST['password1']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return render(request, 'questionpage.html')
		else:
			return render(request, 'loginpage.html',{'message':'User is not registered!'})

def log_out(request):
	if request.user.is_authenticated():
		logout(request)
		return render(request, 'loginpage.html', {'message':'Logged out!'})


def leaderboard(request):
	if request.user.is_authenticated():
		q = Users.objects.order_by('-q_no')
		return render(request, 'upvote.html', { 'q':q })

def questions(request):
	if request.user.is_authenticated():
		return render(request,'questionpage.html')

def submit(request):
	if request.user.is_authenticated():
		user = User.objects.get(id = request.user.id)
		u = Users.objects.get(user = user)
		qt = request.POST['tbox']
		print(qt)
		qtext = Question.objects.create(question_text = qt, op1 = request.POST['option1'], op2 = request.POST['option2'], op3 = request.POST['option3'], op4 = request.POST['option4'], correct_ans = int(request.POST['option']), question = u)
		qtext.save()
		u.q_no = u.q_no + 1
		u.save()
		return render(request, 'questionpage.html',{'message':'Submitted!'})

def qlist(request):
	u = User.objects.get(id = request.user.id)
	u1 = Users.objects.get(user = u)
	q = Question.objects.filter(question = u1)
	return render(request, 'ques.html',{'q':q})


def edit(request, question_id):
	u = User.objects.get(id=request.user.id)
	user = Users.objects.get(user=u)
	q = Question.objects.get(id=question_id, question=user)
	return render(request, "questionEdit.html", {'q' : q} )

def save(request, question_id):
	if request.user.is_authenticated():
		user = User.objects.get(id=request.user.id)
		u = Users.objects.get(user=user)
		qt = request.POST['tbox']
		print(qt)
		qtext = Question.objects.get(id = question_id, question = u)
		qtext.question_text = qt
		qtext.op1 = request.POST['option1']
		qtext.op2 = request.POST['option2']
		qtext.op3 = request.POST['option3']
		qtext.op4 = request.POST['option4']
		qtext.correct_ans = int(request.POST['option'])
		qtext.save()
		return render(request, 'ques.html', {'q': Question.objects.filter(question = u)})


def add(request):
	return render(request, 'questionpage.html')























