import graphene

import courses.programs.schema
from courses.programs.mutations import ProgramSerializerMutation, WeekSerializerMutation, PageSerializerMutation

class Mutation(graphene.ObjectType):
    program_create = ProgramSerializerMutation.CreateField()
    program_delete = ProgramSerializerMutation.DeleteField()
    program_update = ProgramSerializerMutation.UpdateField()

    week_create = WeekSerializerMutation.CreateField()
    week_delete = WeekSerializerMutation.DeleteField()
    week_update = WeekSerializerMutation.UpdateField()

    page_create = PageSerializerMutation.CreateField()
    page_delete = PageSerializerMutation.DeleteField()
    page_update = PageSerializerMutation.UpdateField()

class Query(courses.programs.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)