from model.group import Group


class GroupHelper:

    group_cache = None

    def __init__(self,app):
        self.app = app

    def get_group_list(self):
        if self.group_cache is None:
            self.open_group_editor()
            tree = self.group_edit.window(auto_id='uxAddressTreeView')
            root = tree.tree_root()
            group_list = [Group(name = node.text()) for node in root.children()]
            self.close_group_editor()
        return group_list

    def add_new_group(self,group):
        self.open_group_editor()
        self.click_new_group()
        self.set_group_name(group.name)
        self.close_group_editor()
        self.group_cache = None

    def delete_group_by_index(self,index):
        self.open_group_editor()
        self.click_group_delete_by_index(index)
        self.click_delete()
        self.click_delete_select_group()
        self.delete_group_confirm()

    def click_new_group(self):
        self.group_edit.window(auto_id='uxNewAddressButton').click()

    def click_group_delete_by_index(self,index):
        tree = self.group_edit.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        group=root.children()
        group[index].click()


    def click_delete(self):
        self.group_edit.window(auto_id='uxDeleteAddressButton').click()
        self.group_delete = self.app.application.window(title='Delete group')
        self.group_delete.wait('visible')

    def click_delete_select_group(self):
        self.group_delete.window(auto_id = "uxDeleteAllRadioButton").click()

    def delete_group_confirm(self):
        self.group_delete.window(auto_id = "uxOKAddressButton").click()

    def set_group_name(self,name):
        input = self.group_edit.window(class_name='Edit')
        input.set_text(name)
        input.type_keys('\n')

    def open_group_editor(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.group_edit = self.app.application.window(title='Group editor')
        self.group_edit.wait('visible')

    def close_group_editor(self):
        self.group_edit.close()