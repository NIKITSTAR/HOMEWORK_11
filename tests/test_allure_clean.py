import allure
from allure_commons.types import Severity
from selene import browser, be, have
from selene.api import s



def test_allure_github_clean():
    browser.open('https://github.com/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('/NIKITSTAR/HOMEWORK_10').press_enter()
    browser.element('a[href="/NIKITSTAR/HOMEWORK_10').should(have.text('NIKITSTAR/HOMEWORK_10')).click()
    browser.element('#issues-tab').click()
    browser.element('.env-production').should(have.text('#1'))

def test_allure_github_steps():
    with allure.step("Открываем главную страницу GitHub"):
        browser.open('https://github.com/')

    with allure.step("Ищем репозиторий 'eroshenkoam/allure-example'"):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим в репозиторий"):
        s('.search-title').should(have.exact_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем вкладку Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с текстом 'Тестируем тест'"):
        s('.ListItem-module__listItem--kHali').should(have.text('Тестируем тест'))
        s('.ListItem-module__listItem--kHali').should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com/')

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
        s('.search-title').should(have.exact_text('eroshenkoam/allure-example')).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
        s('#issues-tab').click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
        s('.ListItem-module__listItem--kHali').should(have.text('Тестируем тест'))
        s('.ListItem-module__listItem--kHali').should(be.visible)

def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass