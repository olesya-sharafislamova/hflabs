

class AppealHelper:

    def __init__(self, app):
        self.app = app


    def fill_username(self, fullname=u"Баширова", name=u"Анастасия", secondname=u"Сергеевна"):
        wd = self.app.wd
        wd.find_element_by_id("fullname-surname").click()
        wd.find_element_by_id("fullname-surname").clear()
        wd.find_element_by_id("fullname-surname").send_keys(fullname)
        wd.find_element_by_id("fullname-name").clear()
        wd.find_element_by_id("fullname-name").send_keys(name)
        wd.find_element_by_id("fullname-patronymic").clear()
        wd.find_element_by_id("fullname-patronymic").send_keys(secondname)

    def fill_phone(self, phone="+7916 235-98-74"):
        wd = self.app.wd
        wd.find_element_by_id("phone").click()
        wd.find_element_by_id("phone").clear()
        wd.find_element_by_id("phone").send_keys(phone)

    def fill_email(self, email="1@1.ru"):
        wd = self.app.wd
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(email)

    def fill_message(self, message=u"текст обращения"):
        wd = self.app.wd
        wd.find_element_by_id("message").click()
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(message)

    def fill_address(self, postal_code="420000", address_city=u"Казань", street=u"Батыршина", house="1", flat="1"):
        wd = self.app.wd
        wd.find_element_by_id("address-postal_code").click()
        wd.find_element_by_id("address-postal_code").clear()
        wd.find_element_by_id("address-postal_code").send_keys(postal_code)
        wd.find_element_by_id("address-city").clear()
        wd.find_element_by_id("address-city").send_keys(address_city)
        wd.find_element_by_id("address-street").clear()
        wd.find_element_by_id("address-street").send_keys(street)
        wd.find_element_by_id("address-house").clear()
        wd.find_element_by_id("address-house").send_keys(house)
        wd.find_element_by_id("address-flat").clear()
        wd.find_element_by_id("address-flat").send_keys(flat)

    def send_message(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@type='submit']").click()