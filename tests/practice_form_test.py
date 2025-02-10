from demoqa_tests.model.pages.registration_page import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    (
       registration_page
       .fill_first_name('Nikita')
       .fill_last_name('Star')
       .fill_email('email@email.ru')
       .select_gender('Male')
       .fill_number('1234567891')
       .fill_date_of_birth('1999', 'May', '11')
       .choose_subject('Computer Science')
       .choose_hobbies('Reading')
       .upload_picture('foto.jpg')
       .fill_address('Moscowskaya Street 18')
       .fill_state('NCR')
       .choose_city('Delhi')
       .submit()
    )

    registration_page.should_registered_user_with(
        'Nikita Star',
        'email@email.ru',
        'Male',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )