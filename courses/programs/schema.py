import graphene

from graphene_django.types import DjangoObjectType

from courses.programs.models import Program, Week, Page

class ProgramType(DjangoObjectType):
    class Meta:
        model = Program

    progress = graphene.String()

    def resolve_progress(self, info):
        num_pages_complete = self.weeks.filter(pages__complete=True).count()
        num_pages = self.weeks.filter(pages__isnull=False).count()
        if num_pages_complete == 0:
            return 0
        return (num_pages_complete / num_pages) * 100


class WeekType(DjangoObjectType):
    class Meta:
        model = Week

class PageType(DjangoObjectType):
    class Meta:
        model = Page

class Query(object):
    program = graphene.Field(ProgramType,
                        id=graphene.Int(),
                        name=graphene.String())
    week = graphene.Field(WeekType,
                        id=graphene.Int(),
                        name=graphene.String())
    page = graphene.Field(PageType,
                        id=graphene.Int(),
                        name=graphene.String())
    all_programs = graphene.List(ProgramType)
    all_weeks = graphene.List(WeekType)
    all_pages = graphene.List(PageType)

    def resolve_program(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Program.objects.get(pk=id)

        if name is not None:
            return Program.objects.get(name=name)

        return None


    def resolve_week(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Program.objects.get(pk=id)

        if name is not None:
            return Week.objects.get(name=name)

        return None


    def resolve_page(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Page.objects.get(pk=id)

        if name is not None:
            return Page.objects.get(name=name)

        return None

    def resolve_all_programs(self, info, **kwargs):
        return Program.objects.all()

    def resolve_all_weeks(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            program = Program.objects.get(pk=id)
            return Week.objects.get(program=program)
        # We can easily optimize query count in the resolve method
        return Week.objects.all()

    def resolve_all_pages(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Page.objects.all()