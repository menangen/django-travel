from django.test import TestCase
from .models import AddonsStack


class EntryModelTest(TestCase):

    def test_string_representation(self):
        addons_stack = AddonsStack.objects.all()

        data = [{'pk': stack.pk, '__str__': str(stack)} for stack in addons_stack]

        return True