import requests
from django.conf import settings
from .models import GitUser, Repository
import json
# from django.contrib.sites.models import Site

# SITE_URL = Site.objects.get_current().domain
# SITE_URL = "git.heroku.com/obscure-fjord-35629.git"
def get_from_graph(username):
    url = "https://obscure-fjord-35629.herokuapp.com/api-graphql"
    query = "query { gituserByName(username: \"" + username + "\") { username name repositories{ id name description url } } } "
    data = {"query":query}
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data=data)
    if res.status_code == 200:
        try:
            j_res = res.json()
        except:
            raise Exception("Not JSON")
        else:
            return j_res
    else:
        raise Exception(("Not response 200 Graph"))


def get_from_git(username):
    url = "https://api.github.com/users/" + username + "/repos"
    res = requests.get(url)
    if res.status_code == 200:
        try:
            j_res = res.json()
        except:
            raise Exception("Not JSON")
        else:
            return res.json()
    else:
        raise Exception(("Not response 200 Git"))
    
def get_name_from_git(username):
    url = "https://api.github.com/users/" + username
    res = requests.get(url)
    if res.status_code == 200:
        try:
            j_res = res.json()
        except:
            raise Exception("Not JSON")
        else:
            if j_res.get("name")!= None:
                return j_res["name"]
            else:
                return j_res["login"].capitalize()
    else:
        raise Exception(("Not response 200 Git"))
    

def get_clean_data(data):
    clean_data = dict()
    clean_data["username"] = data[0]["owner"]["login"]
    clean_data["name"] = get_name_from_git(clean_data["username"])
    clean_data["repositories"] = list()
    for dct in data:
        new_dict = dict()
        new_dict["name"] = (dct["name"])
        if dct["description"] is None:
            new_dict["description"] = "Null"
        else:
            new_dict["description"] = (dct["description"])
        new_dict["url"] = (dct["url"])
        clean_data["repositories"].append(new_dict)
    return clean_data


def check_user_in_bd(username):
    try:
        git_user = GitUser.objects.get(username=username)
    except:
        return False
    else:
        return True


def create_instance(data):
    new_git_user = GitUser(username=data["username"], name=data["name"])
    new_git_user.save()
    for dct in data["repositories"]:
        new_repository = Repository(
            name=dct["name"],
            description=dct["description"],
            url=dct["url"],
            owner=new_git_user
            )
        new_repository.save()


def get_data_and_create_instance(username):
    try:
        create_instance(get_clean_data(get_from_git(username)))
    except:
        return {"error":"Error create instance"}


def handler_logic(username):
    username = username.lower()
    if check_user_in_bd(username) is True:
        try:
            return get_from_graph(username)
        except:
            return {"error":"Error graph handler logic"}
    else:
        try:
            create_instance(get_clean_data(get_from_git(username)))
            return get_from_graph(username)
        except:
            return {"error":"Error create instance handler logic"}






