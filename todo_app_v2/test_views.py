from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = self.create_user()

    def create_user(self):
        return self.user_manager.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)

    def test_todo_detail_view(self):
        todo = self.user.todo_set.create(title='Test Todo', description='This is a test todo')
        response = self.client.get(reverse('todo_detail', args=[todo.pk]))
        self.assertEqual(response.status_code, 200)

    def test_create_todo_view(self):
        response = self.client.post(reverse('create_todo'), {
            'title': 'New Todo',
            'description': 'This is a new todo'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.count() == 1)

    def test_delete_todo_view(self):
        todo = self.user.todo_set.create(title='Test Todo', description='This is a test todo')
        response = self.client.post(reverse('delete_todo', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.count() == 1)

    def test_update_todo_view(self):
        todo = self.user.todo_set.create(title='Test Todo', description='This is a test todo')
        response = self.client.post(reverse('update_todo', args=[todo.pk]), {
            'title': 'Updated Todo',
            'description': 'This is an updated todo'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.get(pk=todo.pk).title == 'Updated Todo')