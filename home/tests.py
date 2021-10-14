from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from .models import HomePage


class MyHomePageCase(WagtailPageTests):

    fixtures = ["fixtures/mydata.json"]

    def test_can_create_new_page(self):
        """
        Test new Home page Create
        """
        # Get the HomePage
        new_test_page = HomePage.objects.create(nested_form_data({
                'intro': 'About us',
                'body': streamfield([
                    ('section', 'Lorem ipsum dolor sit amet'),
                    ('cta', 'Lorem ipsum dolor sit amet'),
                ])
            })
        )

        # if have ID then is created
        self.assertIsNotNone(new_test_page.id)
