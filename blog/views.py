from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.views import generic, View
from .forms import CommentForm
from .models import Post, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6


class PostDetail(View):
    """
    Class for single blog post view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates view for a single blog post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('created_on')

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Creates view for a comments
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
            },
        )


def delete_comment(request, comment_id):
    """
    Delete a product in the store.
    """

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'comment successfully deleted')
    return redirect(reverse('blog'))
