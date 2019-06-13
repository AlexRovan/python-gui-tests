import pytest
import openpyxl
from fixture.aplication import Application
from model.group import Group
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\Alex\\Downloads\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

