from typing import Any
from django.shortcuts import render
from .models import Post
from .forms import commentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
# Create your views here.


#ListView provides a built-in way to display multiple records from a model.
class PostListView(ListView):
    model=Post
    template_name='blog/post_list.html'
    context_object_name='posts' #access posts in template with this name


#DetailView handles showing details of a single model instance. We also include the comment
# form here for simplicity.


class PostDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'
    context_object_name='post'

    def post(self,request,*args,**kwargs):  #this method overrides the default post method of the DetailView class.
        form=commentForm(request.POST) #This lines creats an instance of commentForm , passing in request.POST , which contains the submitted form data.
        #By doing this, the form instance(form) is populated with the data from the POST request.
        #post is called when a POST request is made to the view, typically when a form is submitted. In this case, it's handling the submission of a comment form.
        
        if form.is_valid(): #it checks whether the form data is valid based on the validation rules  defined in commentForm.
            comment=form.save(commit=False) # it creates a Comment object but doesn't save it to the database yet.
            #commit=False argument allows you to modify the Comment object before commiting it to the database. Here, we need to associate the comment with the correct post.
            comment.post=self.get_object()  #it retrieves the specific Post object that this DetailView is displaying.
            #By setting comment.post = self.get_object(), we associate the comment with the current post, establishing the foreign key relationship.
            comment.save() # This save the comment object to the database,including the association with the current Post established in the previous line.
            return redirect('post_detail',pk=self.get_object().pk) # by setting this one, we associate the comment with the current post,establishing the foreign key relationship.
        return self.get(request,*args,**kwargs)
    




    def get_context_data(self,**kwargs):  #this line defines a method name get_context_data. This method is used to add custom data to the context dictionary, which is passed to the template.
        context = super().get_context_data(**kwargs)
        context['comment_form']=commentForm() #add comment form to context
        return context
    
    


# **kwargs allows any additional keyword arguments to be passed to this method, making it flexible and able to accept different types of data.

# self represents the instance of the view class where this method is defined.


# context = super().get_context_data(**kwargs)  calls the get_context_data method of the parent class(DetailView in this case)

# get_context_data from the parent class creates and returns the default context data that the view provides , typically containing the primary model data (Post object for a DetailView)


# This approach allows you to pass multiple data items to a template seamlessly, enabling a richer more interactive user experience.



# Create , Update and Delete Views

class PostCreateView(CreateView):
    model=Post
    fields=['title','content']

    template_name='blog/post_form.html'
    success_url=reverse_lazy('post_list') #Redirect to post list after creation



class PostUpdateView(UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog/post_form.html'
    success_url=reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model=Post
    template_name='blog/post_confirm_delete.html'
    success_url=reverse_lazy('post_list')





