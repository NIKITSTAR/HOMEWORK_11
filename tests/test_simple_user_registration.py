from demoqa_tests.model.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()

    registration_page.open()
    registration_page.fill_full_name('Nikita S')
    registration_page.fill_email('email@email.com')
    registration_page.submit()

    registration_page.should_have_submited('Nikita S', 'email@email.com')