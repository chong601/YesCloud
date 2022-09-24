class NetworkConfig(object):
    """
    Base representation for the Cloud-Init object to be exported to YAML
    """
    _attr = {}

    def __init__(self):
        # Initialize base Cloud-Init configuration
        ethernets_config = {
        }
        self._attr.update({'version': 2})
        self._attr.update({'ethernets': ethernets_config})

    def addInterface(self, network_config: dict):
        count = len(self._attr.get('ethernets').keys())
        self._attr.get('ethernets').update({f'enp{str(count+1)}s0': network_config})

    def getConfig(self):
        return self._attr

    def __repr__(self):
        return str(self._attr)
