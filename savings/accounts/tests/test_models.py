from django.core.exceptions import ValidationError

from django.test.testcases import SimpleTestCase, TestCase

from savings.accounts.models import Profile


class ProfileTests(SimpleTestCase):
    def test_profile_full_name_with_valid_data__expect_correct_full_name(self):
        profile = Profile(
            first_name='Test',
            last_name='Testov',
            budget=1,
            email='test@testov.com',
        )

        self.assertEqual('Test Testov', profile.__str__())


