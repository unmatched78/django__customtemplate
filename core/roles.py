# core/roles.py
from rolepermissions.roles import AbstractUserRole

class MainAdmin(AbstractUserRole):
    available_permissions = {'manage_all': True}

class OrganizationAdmin(AbstractUserRole):
    available_permissions = {'manage_organization': True}

#and many level permissions etc