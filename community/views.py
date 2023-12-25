from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserPost, Comment
from .forms import UserPostForm
from django_ai_codebot.constants import programming_languages

# Create your views here.
@login_required
def posts(request):
    
    if request.method == "POST":
        form = UserPostForm(request.POST)
        if form.is_valid():
            # Save the form data as a new UserPost object
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts')
    else:        
        # fetch every single community post
        response = UserPost.objects.all()        
        form = UserPostForm()
        
        context = {
            "languages": programming_languages,
            "response": response,
            "uid": request.user.id,
            "form": form
        }
        return render(request, 'posts.html', context)

@login_required
def delete_post(request, post_id):
    post = UserPost.objects.filter(pk=post_id)
    post.delete()
    messages.success(request, "Deletion Successful!")
    return redirect('posts')
    
@login_required
def edit_post(request, post_id):
    
    user_post = UserPost.objects.get(pk=post_id)
    if request.method == "POST":
        form = UserPostForm(request.POST, instance=user_post)
        
        if form.is_valid():
            form.save()
        return redirect('posts')
    else:
        form = UserPostForm(instance=user_post)
    
    return render(request, 'edit_post.html', {"form": form, "id": post_id})
       
@login_required
def reply(request, post_id):
    if request.method == "POST":
        
        code = request.POST['code']        
        
        if code:
            user_post = get_object_or_404(UserPost, pk=post_id)
                
            comment = Comment(content=code, user=request.user, user_post=user_post)  
            comment.save()
            return redirect('posts')
        else:
            messages.info(request, 'You must provide code to reply to a question')
            return redirect('posts')
    
    return render(request, 'posts.html')
    