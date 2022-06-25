from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User
from .models import Calc
from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.files import File
import os

def showSignUpForm(request):
    return render(request, 'signup_menu.html')

def showCalc(request):
    return render(request, 'butterfly.html')

def showRes(request):
    return render(request, 'results.html')

def SignUp(request):
    try:
        if request.method == "POST":
            user = User()
            checkLogin = request.POST.get("username")
            checkPass = request.POST.get("pass")
            if len(checkLogin) > 4 or len(checkPass) > 4:
                user.Login = request.POST.get("username")
                user.Password = request.POST.get("pass")
                user.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/CalcForm")
            else:
                messages.error(request, 'Login and password must be over 4 letters')
                return redirect('http://127.0.0.1:8000/')
    except IntegrityError:
        messages.error(request, 'User with this login is already exist')
        return redirect('http://127.0.0.1:8000/')

def butterfly_sum(num1, num2, denum1, denum2):
    try:
        ans_num=(num1*denum2)+(num2*denum1)
        ans_denum=denum2*denum1
        return [ans_num, ans_denum]
    except:
        ans_num='error'
        ans_denum='error'
        return [ans_num, ans_denum]

def butterfly_substract(num1, num2, denum1, denum2):
    try:
        ans_num=(num1*denum2)-(num2*denum1)
        ans_denum=denum2*denum1
        return [ans_num, ans_denum]
    except:
        ans_num='error'
        ans_denum='error'
        return [ans_num, ans_denum]

def Calc_butterfly(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        num_1 = request.POST.get('first_up')
        num_2 = request.POST.get('second_up')
        denum_1 = request.POST.get('first_dwn')
        denum_2 = request.POST.get('second_dwn')
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            rb = request.POST.get("RB", None)
            if rb in ["summing", "Subtraction"]:
                if rb == "summing":
                    if checkUserLogin is not None:
                        if num_1 == '' or num_2 == '' or denum_2 =='' or denum_1=='' or denum_1 =='0' or denum_2 =='0':
                            data = {
                                'username': username,
                                'password': password,
                                'first_up': num_1,
                                'first_dwn': denum_1,
                                'second_up': num_2,
                                'second_dwn': denum_2,
                                'ans_up': 'error',
                                'ans_dwn': 'error',
                            }
                            messages.error(request, 'Incorrect input')
                            return render(request, "butterfly.html", data)
                        else:
                            num_1 = int(num_1)
                            num_2 = int(num_2)
                            denum_1 = int(denum_1)
                            denum_2 = int(denum_2)
                            answer = butterfly_sum(num_1,num_2, denum_1, denum_2)
                            tmp = Calc.objects.create(First_Up=num_1, First_Dwn=denum_1, Second_Up=num_2,
                                                      Second_Dwn=denum_2, Answer_Up=answer[0], Answer_Dwn=answer[1], user_id=checkUserLogin.id)
                            data = {
                                'username': username,
                                'password': password,
                                'first_up': num_1,
                                'first_dwn': denum_1,
                                'second_up': num_2,
                                'second_dwn': denum_2,
                                'ans_up': answer[0],
                                'ans_dwn': answer[1],
                            }
                            return render(request, "butterfly.html", data)
                elif rb == "Subtraction":
                    if checkUserLogin is not None:
                        if num_1 == '' or num_2 == '' or denum_2 == '' or denum_1 == '' or denum_1 == '0' or denum_2 == '0':
                            data = {
                                'username': username,
                                'password': password,
                                'first_up': num_1,
                                'first_dwn': denum_1,
                                'second_up': num_2,
                                'second_dwn': denum_2,
                                'ans_up': 'error',
                                'ans_dwn': 'error',
                            }
                            messages.error(request, 'Incorrect input')
                            return render(request, "butterfly.html", data)
                        else:
                            num_1 = int(num_1)
                            num_2 = int(num_2)
                            denum_1 = int(denum_1)
                            denum_2 = int(denum_2)
                            answer = butterfly_substract(num_1,num_2, denum_1, denum_2)
                            tmp = Calc.objects.create(First_Up=num_1, First_Dwn=denum_1, Second_Up=num_2,
                                                      Second_Dwn=denum_2, Answer_Up=answer[0], Answer_Dwn=answer[1],
                                                      user_id=checkUserLogin.id)
                            data = {
                                'username': username,
                                'password': password,
                                'first_up': num_1,
                                'first_dwn': denum_1,
                                'second_up': num_2,
                                'second_dwn': denum_2,
                                'ans_up': answer[0],
                                'ans_dwn': answer[1],
                            }
                            return render(request, "butterfly.html", data)
        except User.DoesNotExist:
            messages.error(request, "Wrong login or password")
            return HttpResponseRedirect("http://127.0.0.1:8000/CalcForm")
    return HttpResponseRedirect("http://127.0.0.1:8000/CalcForm")

def checkUserDatas(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                datas = Calc.objects.filter(user_id=checkUserLogin.id)
                return render(request, "results.html", {"datas": datas})
            else:
                messages.error(request, "Wrong login or password")
                return HttpResponseRedirect("http://127.0.0.1:8000/Results")
        except User.DoesNotExist:
            messages.error(request, "Wrong login or password")
            return HttpResponseRedirect("http://127.0.0.1:8000/Results")
    return HttpResponseRedirect("http://127.0.0.1:8000/Results")


