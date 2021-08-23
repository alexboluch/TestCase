from django.test import TestCase
from .models import GitUser, Repository
from .views import *
from .logics import *


class TestFullCycleTest(TestCase):

    count_rep_user = 10


    def setUpTestData(self):
        user1 = GitUser(username="georg", name="King Georg")
        user1.save()
        user2 = GitUser(username="karl", name="King Karl")
        user2.save()

        
        for current in range(self.count_rep_user):
            Repository.objects.create(owner=user1, name="Georg%s" % current, 
            description = "N%s Georg repositories" % current, url="https://github.com/")
            Repository.objects.create(owner=user2, name="Karl%s" % current, 
            description = "N%s Karl repositories" % current, url="https://github.com/")


    def test_check_in_base(self):
        gituser = GitUser.objects.get(username="georg")
        set_rep = Repository.objects.all().filter(owner=gituser.username)
        self.assertTrue(gituser)
        self.assertTrue(len(set_rep) == self.count_rep_user)


    def test_check_graphql_and_handler_logic(self):
        gituser = GitUser.objects.get(username="karl")
        set_rep = Repository.objects.all().filter(owner=gituser.username)
        resp_graph = get_from_graph(gituser.username)
        self.assertTrue(resp_graph)
        resp_handler = handler_logic(gituser.username)
        self.assertEqual(resp_graph, resp_handler)


    def test_check_view(self):
        resp = self.client.get('/get-info/')
        self.assertEqual(resp.status_code, 200)








