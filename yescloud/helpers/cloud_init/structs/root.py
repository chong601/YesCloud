from .users import User


class Root(object):
    """
    Base representation for the Cloud-Init object to be exported to YAML
    """
    _attr = {}
    _mapper_attr = {
        'users': User()
    }

    def __init__(self):
        # Initialize base Cloud-Init configuration
        self._attr.update({'system_info': {'default_user': {'name': 'ubuntu'}}})
        self._attr.update({'package_update': True})
        self._attr.update({'package_upgrade': True})
        self._attr.update({'chpasswd': {'expire': False}})
        self._attr.update({'ssh_pwauth': False})
        self._attr.update({'hostname': 'ubuntu'})
        self._attr.update({'timezone': 'Etc/UTC'})
        self._attr.update({'packages': ['qemu-guest-agent', 'haveged']})

    # def __setattr__(self, name: str, value: Any) -> None:
    #     self._attr.update({name: value})
    #
    # def __getattribute__(self, name: str) -> Any:
    #     self._attr.get(name)
    #
    # def __delattr__(self, name: str) -> None:
    #     self._attr.pop(name)
    def setHostname(self, hostname):
        self._attr.update({'hostname': hostname})

    def setDefaultUserPassword(self, password):
        self._attr.update({'ssh_pwauth': password})

    def setUsers(self, users):
        self._attr.update({'users': users})

    def enablePackageUpdate(self):
        self._attr.update({'package_update': True})

    def disablePackageUpdate(self):
        self._attr.update({'package_update': False})

    def addPackages(self, packages):
        if isinstance(packages, str):
            self._attr.get('packages').append(packages)
        elif isinstance(packages, list):
            self._attr.get('packages').extend(packages)

    def addSSHKeyToDefaultUser(self, ssh_key):
        ssh_key_array: list = self._attr.get('system_info').get('default_user').get('ssh_authorized_keys')
        if ssh_key_array is None:
            ssh_key_array = []
        if isinstance(ssh_key, list):
            ssh_key_array.extend(ssh_key)
        elif isinstance(ssh_key, str):
            ssh_key_array.append(ssh_key)
        self._attr.get('system_info').get('default_user').update({'ssh_authorized_keys': ssh_key_array})

    def getConfig(self):
        return self._attr

    def __repr__(self):
        return str(self._attr)
