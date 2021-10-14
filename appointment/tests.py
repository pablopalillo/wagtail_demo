from django.test import TestCase


class AppointmentFormTest(TestCase):

    fixtures = ["fixtures/mydata.json"]

    def test_verify_accessible(self):

        url = "/agenda-tu-cita"

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 301)

    def test_page_appointment(self):
        # verify the form in the Edit Page Appointment
        data = {
            'nombre': 'pablo',
            'telefono': '3123132',
            'fecha': '2021-10-28T03:09:14.841Z',
            'barbero': 'Jackie'
        }
        resp = self.client.post("/agenda-tu-cita", data)
        self.assertTrue(resp.status_code, 301)
