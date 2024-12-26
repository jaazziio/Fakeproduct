from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import FeedBack, LoginTable, ManufactureTable, ProductTable
from sampleApp.form import  AddProductForm, UserRegForm, manufactureform


# Create your views here.
class LoginPage(View): 
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        UserName = request.POST['UserName']
        PassWord = request.POST['PassWord']
        login_obj = LoginTable.objects.get(UserName=UserName, PassWord=PassWord)
        if login_obj.type == "admin":
            return HttpResponse('''<script>window.location="/AdminDashboardPage/"</script>''')
    
class AddPage(View):
    def get(self,request):
     return render(request,"add.html")
class AdminDashboardPage(View): 
    def get(self, request):
        return render(request, "admindashboard.html")
class ApprovePage(View):
     def get(self, request):
        return render(request, "approve.html")
     
class UserReg(View):
     def get(self, request):
        return render(request, "Register.html")
     def post(self, request):
         form = manufactureform(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponse('''<script>alert("registered");window.location=("/")</script>''')
class Manufacture(View):
    def get(self, request):
        return render(request, "manufacture.html")
    def post(self, request):
         print("hhhhh")
         form = manufactureform(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponse('''<script>alert("registered");window.location=("/")</script>''')
class Viewmanufacture(View):
    def get(self,request):
        v=ManufactureTable.objects.all()
        return render(request,'viewmanufacture.html',{'v':v})
class AddProduct(View):
    def get(self, request):
        return render(request, "add.html")
    def post(self, request):
         print("hhh")
         form = AddProductForm(request.POST,request.FILES)
         if form.is_valid():
             form.save()
             return HttpResponse('''<script>alert("added");window.location=("/")</script>''')
         
class ViewAddProduct(View):
    def get(self,request):
        v=ProductTable.objects.all()
        return render(request,'viewaddproduct.html',{'v':v})



class viewFeedBack(View):
    def get(self,request):
        v=FeedBack.objects.all()
        return render(request,'feedback.html',{'v':v})
    
    


         

    

