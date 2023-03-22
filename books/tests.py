from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.book = Book.objects.create(
      title='A good title',
      subtitle='An excellent subtitle',
      author='Tom Doe',
      isbn='12344567890123',)

  # all tests must start with test_.
  def test_book_content(self):
    self.assertEqual(self.book.title, "A good title")
    self.assertEqual(self.book.subtitle, "An excellent subtitle")
    self.assertEqual(self.book.author, "Tom Doe")
    self.assertEqual(self.book.isbn, "12344567890123")

  def test_book_listview(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "excellent subtitle")
    self.assertTemplateUsed(response, "books/book_list.html")


