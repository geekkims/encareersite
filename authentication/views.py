from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import account_activation_token
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import threading

# Create your views here.
class EmailThread(threading.Thread):
 
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)
    
class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'},status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exist,kindly choose another one'},status=409)
        return JsonResponse({'username_valid':True})

class EmailValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        email=data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'email is invalid'},status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email already exist,kindly choose another one'},status=409)
        return JsonResponse({'email_valid':True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # GET USER DATA
        # VALIDATE
        # create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }

                link = reverse('activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})

                email_subject = 'Activate your account'

                activate_url = 'http://'+current_site.domain+link

                email = EmailMessage(
                    email_subject,
                    'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
                    'info@techspace.co.ke',
                    [email],
                )
                EmailThread(email).start()
                messages.success(request, 'Account successfully created')
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')



class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')
        
        


class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            user=auth.authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request,'Welcome, '+user.username +' You are Now Logged In')
                    return redirect('expenses')

                messages.error(request,'Account is not active, please check your email')
                return render(request,'authentication/login.html')

            messages.error(request,'Invalid credentials,Kindly Check')
            return render(request,'authentication/login.html')
        messages.error(request,'All Fields are Required.kindly Fill')
        return render(request,'authentication/login.html')



class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'You are logged out successfully')
        return redirect('login')


class RequestPasswordResetEmail(View):
    def get(self,request):
        return render(request,'authentication/reset-password.html')

    def post(self,request):
        email = request.POST['email']

        context={
            'values':request.POST
        }

        if not validate_email(email):
            messages.error(request,'Please Supply a valid Email')
            return render(request,'authentication/reset-password.html',context)
        current_site = get_current_site(request)
        user= User.objects.filter(email=email)
        if user.exists():
            email_contents = {
                    'user': user[0],
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                    'token': PasswordResetTokenGenerator().make_token(user[0]),
                }

            link = reverse('reset-user-password', kwargs={
                            'uidb64': email_contents['uid'], 'token': email_contents['token']})

            email_subject = 'Password Resest Link'

            reset_url = 'http://'+current_site.domain+link

            email = EmailMessage(
                email_subject,
                'Hi there, Please click the link below to reset your password \n'+reset_url,
                'info@techspace.co.ke',
                [email],
            )
            EmailThread(email).start   
        messages.success(request,"Kindly check your email for the password link ")
        return render(request,'authentication/reset-password.html',context)
        


# class CompletePasswordReset(View):
#     def get(self, request, uidb64, token):

#         context ={
#             "uidb64":uidb64,
#             "token":token,
#         }
#         return render(request,'authentication/set-new-password.html',context)
#     def post(self,request,uidb64,token):

#         context ={
#         "uidb64":uidb64,
#         "token":token,}

#         password=request.POST['password']
#         password2=request.POST['password2']

#         print(password)

#         if password!=password2:
#             messages.error(request,'Password do not match')
#             return render(request,'authentication/set-new-password.html',context)
#         if len(password)<6:
#             messages.error(request,'Password should be six characters or more')
#             return render(request,'authentication/set-new-password.html',context)

#         try:
#             user_id=force_str(urlsafe_base64_decode(uidb64))

#             user=User.objects.get(pk=user_id)
#             user.password = password
#             user.save()
#             messages.success(request,'Password reset successful.You can Login now with the password')
#             return redirect('login')
#         except Exception as identifier:
#             messages.info(request,'Something went wrong,try again') 
#             return render(request,'authentication/set-new-password.html',context)

    
        

        # return render(request,'authentication/set-new-password.html',context)

class CompletePasswordReset(View):
    def get(self, request, uidb64, token):
        context = {'uidb64': uidb64, 'token': token}
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(
                    request,  'Link is no longer valid,please request a new one')
                return render(request, 'authentication/reset-password.html', status=401)

        except Exception as identifier:
                pass

        return render(request, 'authentication/set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {'uidb64': uidb64, 'token': token}
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if len(password) < 6:
                messages.error(
                    request,'Password should be at least 6 characters long')
                return render(request, 'authentication/set-new-password.html', context, status=400)
            if password != password2:
                messages.error(
                    request,  'Passwords must match')
                return render(request, 'authentication/set-new-password.html', context, status=400)
            user.set_password(password)
            user.save()
            messages.info(
                request,  'Password changed successfully,login with your new password')
            return redirect('login')
        except DjangoUnicodeDecodeError:
            messages.error(
                request,  'Something went wrong,you could not update your password')
            return render(request, 'authentication/set-new-password.html', context, status=401)