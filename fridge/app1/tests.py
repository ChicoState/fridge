from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse
from app1 import forms
from app1.views import *
from app1.forms import SignUpForm
from django.test import RequestFactory
from mixer.backend.django import mixer
from django.test import Client
from django.contrib.auth.models import User, AnonymousUser



# *********************************
# Model Creation
# *********************************

# Create a basic item
class ItemCreate(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Item.objects.create(author=self.user, food_title="milk", food_type="dairy")

    def testItemCreate(self):
        foodItem = Item.objects.get(food_title="milk")
        self.assertEqual(foodItem.food_type, "dairy")

class testToggleItems(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Item.objects.create(author=self.user, food_title="milk", food_type="dairy")

class testGetItems(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(author=self.user, image="avatar.png") 


class testDeleteItems(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def testItemDeleteRecipe(self):
        item = Item.objects.create(author=self.user, food_title="milk", food_type="dairy") 
        self.client.login(username="testuser", password="12345")
        self.client.post(path='/delete_recipe/' + str(item.id) + '/')

        recipe_count = Item.objects.filter(id=item.id).count()
        self.assertEqual(recipe_count, 1)

# **********************
# Test Create Items
# **********************

class testCreateItem(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def testRecipeCreate(self):

        recipe_form = {
            "food_title": "milk",
            "food_type": "dairy",
            "photos": "test.png",
            "price": 3 
        }
        self.client.login(username="testuser", password="12345")
        self.client.post(path='/create_recipe/', data=recipe_form)

        recipe_count = Item.objects.filter(food_title="milk").count()
        self.assertEqual(recipe_count, 0)

# **********************
# Test Edit Item
# **********************

class testEditItem(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', 
        password='12345')
    
    def testEdit_item(self):
        recipe = Item.objects.create(author=self.user, food_title="milk", 
        photos="test.png", food_type="dairy") 
        edit_item_form = {
            "food_title": "milk",
            "food_type": "dairy",
            "photos": "test.png",
            "price": 3 
        }
        
        self.client.login(username="testuser", password="12345")
        self.client.post(path='/update_item/' + str(recipe.id) + '/', 
        data=edit_item_form)

        edited_item = Item.objects.get(id=recipe.id)
        self.assertEqual(edited_item .food_title, "milk")

# *************************
# Test Registration
# *************************

class testRegistrationSuccess(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
       
    def testRegistrationSuccess(self):
        registration_form = {
            "username": "brent_de", 
            "email": "brent_de@gmail.com",
            "password1": "ilovepizza12345",
            "password2": "ilovepizza12345"
        }

        response = self.client.post(path='/signup/', data=registration_form, follow=True)
        self.assertEqual(response.status_code, 200)
        logged_in = self.client.login(username="brent_de", password="ilovepizza12345")
        self.assertTrue(logged_in)

class testRegistrationFailFormInvalid(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
       
    def testRegistrationFailFormInvalid(self):
        registration_form = {
            "username": "brent_de", 
            "email": "brent_de@gmail.com",
            "password1": "ilovepizza12345"
        }

        response = self.client.post(path='/signups/', data=registration_form, follow=True)
        self.assertEqual(response.status_code, 404)
        logged_in = self.client.login(username="brent_de", password="ilovepizza12345")
        self.assertFalse(logged_in)

class testRegistrationPasswordsDontMatch(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
       
    def testRegistrationPasswordsDontMatch(self):
        registration_form = {
            "username": "brent_de", 
            "email": "brent_de@gmail.com",
            "password1": "ilovepizza12345",
            "password2": "ilovepizza"
        }

        response = self.client.post(path='/signup/', data=registration_form, follow=True)
        self.assertEqual(response.status_code, 200)
        logged_in = self.client.login(username="brent_de", password="ilovepizza12345")
        self.assertFalse(logged_in)

# **********************
# Test Logout
# **********************
class testLogout(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def testLogout(self):
        self.client.login(username="testuser", password="12345")
        self.client.get(path='/logout/')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_createProfile_url(self):
        user=User.objects.create(username = 'batman')
        user.set_password('thisisrobin')
        user.save()
        #self.client.login(username='batman', password = 'thisisrobin')
        c = Client()
        logged_in = c.login(username='batman', password='thisisrobin')
        response= self.client.post(reverse('profile_update'))
        self.assertTrue(logged_in)
        self.assertEquals(response.status_code, 302)

    def test_createcause_url(self):
        User.objects.create(username = 'batman', password = 'thisisrobin')
        self.client.login(username='batman', password = 'thisisrobin')
        response= self.client.post(reverse('password_change_done'))
        self.assertEquals(response.status_code, 302)

class home_view_test(TestCase):
    def test_Sanity(self):
        self.assertEqual(True,True)
	    
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)
    
    def test_view_url_by_name(self):
        response= self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 302)

    def test_view_url_by_name(self):
        response= self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 404)

    def test_view_url_by_name(self):
        response= self.client.get(reverse('chart'))
        self.assertEquals(response.status_code, 200)

        #VIEWS TESTING
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
        username='testuser', email='test@test.com', password='supersecretpass')
        self.user_id = self.user.id

    def test_index_view_authenticated(self):
        request = self.factory.get('/index.html')
        request.user = self.user
        response = list_item(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_unauthenticated(self):
        request = self.factory.get('/index.html')
        request.user = AnonymousUser()
        response = list_item(request)
        self.assertEqual(response.status_code, 302) 
    
    def test_submit_view(self):
        request = self.factory.get('/search.html')
        request.user = self.user
        response = search(request)
        self.assertEqual(response.status_code, 200)

    def test_submit_view(self):
        request = self.factory.get('/signup.html')
        request.user = self.user
        response = signup(request)
        self.assertEqual(response.status_code, 200)

    def test_submit_view(self):
        request = self.factory.get('/my_account.html')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_view_about_unauthenticated(self):
        request = self.factory.get('/about.html')
        request.user = AnonymousUser()
        response = about(request) 
        self.assertEqual(response.status_code, 302)

    def test_view_login(self):
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_register(self):
        request = self.factory.get('/signup/')
        response = signup(request) 
        self.assertEqual(response.status_code, 200)

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        
        
    def test_url_available_by_name(self):  
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, 302)

class TestItem:
    def test_item(self):
       item = mixer.blend("myapp.MyModel")
       assert item.pk == 1, "Should create a MyModel instance"
 
            #FORM TESTING
class TestSignupForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com", password="passwordlol")

    def test_empty_form(self):
         form = SignUpForm()
         self.assertIn("username", form.fields)
         self.assertIn("email", form.fields)
         self.assertIn("password1", form.fields)
         self.assertIn("password2", form.fields)

    # Check form has correct data as email is Char field so we can't enter a number
    def test_Signup_Form_valid_data(self):
        form = SignUpForm(data = {
            'email': 'bob@gmail.com'
        })
        self.assertFalse(form.is_valid())

     # Check form has correct data as email is Char field 
     # so we can't enter a number. So we show a fail test
    def test_Signup_Form_valid_data_fail(self):
         form = SignUpForm(data = {
             'email': 1000,
         })
         self.assertFalse(form.is_valid())

    # Check if the form is invalid, check correct amount of data. 
    def test_Signup_Form_no_data(self):
        form = SignUpForm(data = {
            
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    def test_issue_form_valid(self):
        data = {'valid_to': " ", 'valid_from': " "}
        form = forms.ItemForm(data=data)
        self.assertFalse(form.is_valid())


class AuthTests(TestCase):
    def test_registration(self):
        c = Client()
        response = c.post('/register/', {'username': 'tester', 'email': 'tester@testing.test', 'password': 'testingtesting123', 'password1': 'testingtesting123'})
        self.assertEqual(404, response.status_code)

    def test_registration_then_login(self):
        c = Client()
        response = c.post('/register/', {'username': 'tester', 'email': 'tester@testing.test', 'password': 'testingtesting123','password': 'testingtesting123'})
        response = c.post('/login/', {'username': 'tester', 'password': 'testingtesting123'})
        self.assertEqual(200, response.status_code)
