import graphene
from graphene_django import DjangoObjectType
from .models import GitUser, Repository

class RepositoryType(DjangoObjectType):
    class Meta:
        model = Repository
        fields = ("id", "name", "description", "url", "owner")

class GitUserType(DjangoObjectType):
    class Meta:
        model = GitUser
        fields = ("username", "name", "repositories")


class Query(graphene.ObjectType):
    all_repositories = graphene.List(RepositoryType)
    gituser_by_name = graphene.Field(GitUserType, username=graphene.String(required=True))


    def resolve_all_repositories(root, info):
        return Repository.objects.select_related("owner").all()


    def resolve_gituser_by_name(root, info, username):
        try:
            return GitUser.objects.get(username=username)
        except GitUser.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
