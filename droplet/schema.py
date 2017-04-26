from django.contrib.auth.models import User as UserModel

from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
	class Meta:
		model = UserModel

class Query(graphene.ObjectType):
	users = graphene.List(User)

	@graphene.resolve_only_args
	def resolve_users(self):
		return UserModel.objects.all()

schema = graphene.Schema(query=Query)
