"""
Authentication backends for default WhereBee Inventory projects.
"""


class ActiveUserBackend(object):
    """
    Give access to all 'wbinventory' permissions to active, logged-in users.
    """

    supports_object_permissions = False
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, username, password):
        pass

    def has_perm(self, user_obj, perm):
        if (perm.startswith('wbinventory.')
            and not user_obj.is_anonymous()
            and user_obj.is_active
        ):
            return True
        else:
            return False

    def has_module_perms(self, user_obj, app_label):
        if (app_label == 'wbinventory'
            and not user_obj.is_anonymous()
            and not user_obj.is_active
        ):
            return True
        else:
            return False
