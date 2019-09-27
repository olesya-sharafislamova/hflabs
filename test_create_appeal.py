# -*- coding: utf-8 -*-
from model.appeal import Appeal
from fixture.application import Application



def test_create_appeal(app):
    app.open_appeal_page()
    app.appeal.fill_username()
    app.appeal.fill_phone()
    app.appeal.fill_email()
    app.appeal.fill_message()
    app.appeal.fill_address()
    app.appeal.send_message()




