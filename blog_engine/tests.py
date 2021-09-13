from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .models import BlogModel
from .views import index, post, create, delete_all


class TestBlogModel(TestCase):

    def setUp(self):
        self.blog = BlogModel.objects.create(
            Heading="Timetable"
        )

    def test_str_returns_heading(self):
        """
        This will test if the '__str__()' function
        returns the 'heading' of the blog object.
        """
        self.assertEqual(self.blog.__str__(), "Timetable")


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.blog1 = BlogModel.objects.create(
            Heading="Now"
        )
        self.blog2 = BlogModel.objects.create(
            Heading="Then"
        )

    def test_index_view_template_used(self):
        """
        Test if the response was good and the template used
        """
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_index_view_returns_correct_context(self):
        """
        Test if the index view returns the correct number
        of queryset to the template
        """
        response = self.client.get(reverse("index"))

        self.assertEqual(len(response.context['all_blogs']), 2)

    
class TestPostView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.blog = BlogModel.objects.create(
            Heading="data"
        )

    def test_post_view_raises_404_with_invalid_pk(self):
        """
        Test if the view will raise a 404 not found
        if the pk sent isn't traced to an object
        """
        response = self.client.get(reverse("post", args=[2]))

        self.assertEqual(response.status_code, 404)

    def test_post_view_works_with_valid_pk(self):
        """
        Test if the view will raise a 200 response
        if the pk sent is traced to an object
        """
        response = self.client.get(reverse("post", args=[1]))

        self.assertEqual(response.status_code, 200)
    
    def test_post_view_template_used(self):
        """
        Test if the template used
        """
        response = self.client.get(reverse("post", args=[1]))

        self.assertTemplateUsed(response, "post.html")

    def test_post_view_returns_correct_context(self):
        """
        Test if the post view returns the correct blog object
        to the template for rendering
        """
        response = self.client.get(reverse("post", args=[1]))
        blog = BlogModel.objects.get(pk=1)

        self.assertEqual(response.context['post'], blog)


class TestCreateView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.create = reverse("create-post")

    def test_create_view_GET(self):
        """
        Test if the create view will render the correct 
        template on a GET request
        """
        response = self.client.get(self.create)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createpost.html")

    def test_create_view_POST(self):
        """
        Test if the create view will create a blog post
        """
        response = self.client.post(
            self.create, 
            {
                'heading': "New post",
                'content': "This is a meeting for year 2"
            }
        )
        query_set = BlogModel.objects.all()

        self.assertEqual(len(query_set), 1)

    def test_create_view_POST_redirects(self):
        """
        Test if the create view after creating a blog post
        will redirect to the correct url
        """
        response = self.client.post(
            self.create, 
            {
                'heading': "New post",
                'content': "This is a meeting for year 2"
            }
        )
        first = BlogModel.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("post", args=[first.id]))


class TestDeleteView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.delete_all = reverse("delete_all")
        self.blog1 = BlogModel.objects.create(
            Heading="Now"
        )
        self.blog2 = BlogModel.objects.create(
            Heading="Then"
        )

    def test_delete_view_deletes_all_blogs(self):
        """
        Test if the 'delete_all' view will delete
        all blog posts in the database
        """
        response = self.client.get(self.delete_all)
        query_set = BlogModel.objects.all()

        self.assertQuerysetEqual(query_set, [])

    def test_delete_view_redirects(self):
        """
        Test if the 'delete_all' view will redirect
        the user to a particular url
        """
        response = self.client.get(self.delete_all)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))


class TestBlogEngineUrls(SimpleTestCase):
    
    def setUp(self):
        self.index = reverse("index")
        self.post = reverse("post", args=[1])
        self.create = reverse("create-post")
        self.delete_all = reverse("delete_all")

    def test_index_url(self):
        """
        Test index url handling function
        """
        the_resolved = resolve(self.index)

        self.assertEqual(the_resolved.func, index)
        self.assertEqual(the_resolved.url_name, "index")

    def test_post_url(self):
        """
        Test post url handling function
        """
        the_resolved = resolve(self.post)

        self.assertEqual(the_resolved.func, post)
        self.assertEqual(the_resolved.url_name, "post")

    def test_create_url(self):
        """
        Test create url handling function
        """
        the_resolved = resolve(self.create)

        self.assertEqual(the_resolved.func, create)
        self.assertEqual(the_resolved.url_name, "create-post")

    def test_delete_all_url(self):
        """
        Test delete_all url handling function
        """
        the_resolved = resolve(self.delete_all)

        self.assertEqual(the_resolved.func, delete_all)
        self.assertEqual(the_resolved.url_name, "delete_all")
