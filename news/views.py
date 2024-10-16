from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm, ProfileForm, ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Home(generic.TemplateView):
    """This view is used to display the home page"""
    template_name = "index.html"


class PostList(generic.ListView):
    """ Create your views here. """
    model = Post
    """ Render list of post """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'browse_article.html'
    """ Seperate the pages """
    paginate_by = 8


class PostDetail(View):
    """ For post detail views """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        bookmarked = False
        if post.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True,
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "bookmarked": bookmarked,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Post comment """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        bookmarked = False
        if post.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True,
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class Profile(LoginRequiredMixin, generic.TemplateView):
    """Displays login user profile view """
    model = Profile
    template_name = 'profile.html'

    def __str__(self):
        return f"Profile {self.user}by{self.bio}"


class AddArticle(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    This view is used to allow logged in users to create a post
    """
    form_class = ArticleForm
    template_name = 'add_article.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of a posted article.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message method to add
        the article title into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class MyArticle(LoginRequiredMixin, generic.ListView):
    """
    Displays list of article created by a logged in
    user.
    """
    model = Post
    template_name = 'my_article.html'
    paginate_by = 8

    def get_queryset(self):
        """Override get_queryset to filter by user"""
        return Post.objects.filter(author=self.request.user)


class EditArticle(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    This view enables logged in users to edit their own posts
    """
    model = Post
    form_class = ArticleForm
    template_name = 'edit_article.html'
    success_message = "%(calculated_field)s was updated successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        A signed in user is set as the author of the article.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Block user from editing other's posts
        """
        post = self.get_object()
        return post.author == self.request.user

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add article title
        into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    """
    This view enables logged in users to delete their own posted articles.
    """
    model = Post
    template_name = 'delete_post.html'
    success_message = "Post deleted successfully"
    success_url = reverse_lazy('home')

    def test_func(self):
        """
        Prevent another user from deleting other's post
        """
        post = self.get_object()
        return post.author == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


class EditComment(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    This view is used to allow logged in users to edit their own comments
    """
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_message = "Comment edited successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username

    def get_success_url(self):
        """ Return to post detail view when comment updated sucessfully"""
        post = self.object.post

        return reverse_lazy('post_detail', kwargs={'slug': post.slug})


class DeleteComment(LoginRequiredMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_message = "Comment deleted successfully"

    def test_func(self):
        """
        Prevent another user from deleting user's comments
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """ Return to post detail view when comment deleted sucessfully"""
        post = self.object.post

        return reverse_lazy('post_detail', kwargs={'slug': post.slug})


class PostBookmark(LoginRequiredMixin, View):
    """
    Allows a logged in user to bookmark post.
    """
    def post(self, request, slug):
        """
        Checks if user exists in Post field database.
        If they exist remove them or add them to the database.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.bookmarks.filter(id=request.user.id).exists():
            post.bookmarks.remove(request.user)
            messages.success(self.request, 'Post removed from bookmarks')
        else:
            post.bookmarks.add(request.user)
            messages.success(self.request, 'Post added to bookmarks')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Bookmarked(LoginRequiredMixin, generic.ListView):
    """
    Allows logged in users view their bookmarked posts.
    """
    model = Post
    template_name = 'bookmarked.html'
    paginate_by = 8

    def get_queryset(self):
        """Get queryset to filter user bookmarks"""
        return Post.objects.filter(bookmarks=self.request.user.id)


class PostLike(LoginRequiredMixin, View):
    """
    Allows a logged in user to like post.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def about(request):
    return render(request, 'about.html')


def policy(request):
    return render(request, 'policy.html')
