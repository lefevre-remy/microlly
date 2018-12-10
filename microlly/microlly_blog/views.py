from django.shortcuts import render, get_object_or_404, redirect
from microlly_blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from microlly_blog import forms
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'microlly_blog/index.html', {'latests_posts':posts})

def post_details (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'microlly_blog/details.html', {'post':post})

@login_required(login_url = "/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.PostCreate(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('microlly_blog:index')
    else:
        form = forms.PostCreate()
    return render(request, 'microlly_blog/post_create.html', {'form':form})

@login_required(login_url = "/accounts/login/")
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = forms.PostEdit(request.POST or None, instance=post)
    if request.user != post.author:
        return redirect('microlly_blog:index')
    if request.method =='POST':
        if form.is_valid():
            post.save()
            return redirect('microlly_blog:index')
    context = {
        "form":form,
        "post":post,
    }
    return render(request, 'microlly_blog/details.html', context)

###Affichage des post liés à un utilisateur
#def post_user (request, author):
#   récupérer le user actuel <= en fait osef, on peut regarder les posts sans être co
#   ça favorisme le stalk
#   récuprer tous les posts avec filtre =>.filter()
#   dont le user est le créateur .object.all().filter(author=author)
#   retourner un template avec le dictionnaire de données contenant les posts
def list_post_user(request, author):
    if author:
        posts = Post.objects.filter(author=author)
        return render(request, 'microlly_blog/list_post_user.html', {'list_posts_user':posts})
    else:
        redirect('microlly_blog:index')

###Suppresion d'un post
#def post_delete(request, pk):
#   créer une instance du post à supprimer,
#   vérifier que le post.author == request.author sinon => return PermissionDenied
#   post.delete
#   rediriger vers l'index.

def post_delete (request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        redirect('microlly_blog:index')
    if request.method == 'POST':
        post.delete
        return redirect('microlly_blog:index')
    else:
        form = forms.PostEdit(request.POST or None, instance=post)
    return render(request, 'microlly_blog/index.html', {'form':form})