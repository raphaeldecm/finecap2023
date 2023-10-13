from django.contrib.auth.mixins import UserPassesTestMixin


class GerentePermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Gerente"):
            return True
        return False
