from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from dropbox.models import File
from dropbox.forms import LoginForm, AddFileForm, NewUserForm

from mptt.admin import MPTTModelAdmin


def register_user_view(request):
    html = 'generic_form.htm'
    page = 'register'
    if request.method == "POST":

        form = NewUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = NewUserForm()

    return render(request, html, {'form': form, 'page': page})



def login_view(request):
    html = 'generic_view.html'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home'))
            )


# def tree_view(request):
#     return render(request, "genres.html", {'genres': File.objects.all()})


@login_required
def new_file_view(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddFileForm(request.user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                folder=data['folder'],
                parent=data['parent'],
                user=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddFileForm(request.user)
    return render(request, html, {'form': form})


@login_required
def tree_view(request):
    html = 'files.html'

    files = File.objects.filter(user=request.user)
    return render(request, html, {
        'files': files,
        'user': request.user
    })


# class EditTreeView(FormView):
#     template_name = 'generic_form.html'
#     form_class = 
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))