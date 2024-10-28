from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) # Timestamp on creation


    def __str__(self):
        return self.title #return post title for easy identification
    
class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment on {self.post.title}"
    

#This platform will allow users to create , read, update , and delete blog posts. 
# Each post can have comments, allowing for a one-to-many relationship(one post can have many comments).


# Comment Model: allow users to comment on posts, with each comment linked to a specific post.
