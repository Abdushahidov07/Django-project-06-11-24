from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy


# Create your views here.

# CRUD CVB USER

class UserListView(ListView):
    model = User
    template_name = "alluser.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "detailuser.html"
    context_object_name = "user"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = Skills.objects.filter(user_id=self.kwargs["pk"])
        return context

class UserCreateView(CreateView):
    model = User
    template_name = "createuser.html"
    fields = ("f_name","l_name","username","age","email","phone_number","profile_pic","password")
    success_url = reverse_lazy("home")

class UserUpdateView(UpdateView):
    model = User
    template_name = "updateuser.html"
    fields = ("f_name","l_name","username","age","email","phone_number","profile_pic","password")
    success_url = reverse_lazy("home")

    
class UserDeleteView(DeleteView):
    model = User
    template_name = "deleteuser.html"
    context_object_name = "user"
    success_url = reverse_lazy("home")



# CRUD CVB Category


# class UserListView(ListView):
#     model = User
#     template_name = "users.html"
#     context_object_name = "users"

# class UserCreateView(CreateView):
#     model = User
#     template_name = "createuser.html"
#     fields = ("f_name","l_name","username","age","email","phone_number","profile_pic","password")
#     success_url = reverse_lazy("home")

# class UserUpdateView(UpdateView):
#     model = User
#     template_name = "updateuser.html"
#     fields = ("f_name","l_name","username","age","email","phone_number","profile_pic","password")
#     success_url = reverse_lazy("home")

    
# class UserDeleteView(DeleteView):
#     model = User
#     template_name = "deleteuser.html"
#     context_object_name = "user"
#     success_url = reverse_lazy("home")



# CRUD CVB Skills

class SkillsListView(ListView):
    model = Skills
    template_name = "skillss.html"
    context_object_name = "skills"

class SkillsDetailView(DetailView):
    model = Skills
    template_name = "detailskills.html"
    context_object_name = "skill"

class SkillsCreateView(CreateView):
    model = Skills
    template_name = "createskills.html"
    fields = ("skill_name","description","category_id","user_id")
    success_url = reverse_lazy("alluser")

class SkillsUpdateView(UpdateView):
    model = Skills
    template_name = "updateskills.html"
    fields = ("skill_name","description","category_id","user_id")
    success_url = reverse_lazy("alluser")

    
class SkillsDeleteView(DeleteView):
    model = Skills
    template_name = "deleteskills.html"
    context_object_name = "skill"
    success_url = reverse_lazy("alluser")



# CRUD CVB Problems

class ProblemsListView(ListView):
    model = Problems
    template_name = "home.html"
    context_object_name = "problems"

class ProblemsDetailView(DetailView):
    model = Problems
    template_name = "detailproblems.html"
    context_object_name = "problem"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applications"] = Application.objects.filter(problems_id=self.kwargs["pk"])
        return context

class ProblemsCreateView(CreateView):
    model = Problems
    template_name = "createproblems.html"
    fields = ("title","description","user_id","category_id","city_id","region_id","street_id","img","status")
    success_url = reverse_lazy("home")

class ProblemsUpdateView(UpdateView):
    model = Problems
    template_name = "updateproblems.html"
    fields = ("title","description","user_id","category_id","city_id","region_id","street_id","img","status")
    success_url = reverse_lazy("home")

    
class ProblemsDeleteView(DeleteView):
    model = Problems
    template_name = "deleteproblems.html"
    context_object_name = "problem"
    success_url = reverse_lazy("home")


# CRUD CVB Application


class ApplicationListView(ListView):
    model = Application
    template_name = "allapplication.html"
    context_object_name = "applications"

class ApplicationDetailView(DetailView):
    model = Application
    template_name = "detailapplication.html"
    context_object_name = "application"

class ApplicationCreateView(CreateView):
    model = Application
    template_name = "createapplication.html"
    fields = ("user_id","message","price","status","duration",)
    def form_valid(self, form):
       problem =Problems.objects.filter(id=self.kwargs["pk"]).first()
       if problem:
            form.instance.problems_id = problem
            return super().form_valid(form)  
       else:
            return self.form_invalid(form)

    success_url = reverse_lazy("home")

class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = "updateapplication.html"
    fields = ("user_id","message","price","status","duration",)
    success_url = reverse_lazy("allapl")

    
class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = "deleteapplication.html"
    context_object_name = "application"
    success_url = reverse_lazy("allapl")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "detailcategory.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["problems"] = Problems.objects.filter(category_id=self.kwargs["pk"])
        return context
    context_object_name = "category"


class CategoryListView(ListView):
    model = Category
    template_name = "allcategory.html"
    context_object_name = "categorys"
