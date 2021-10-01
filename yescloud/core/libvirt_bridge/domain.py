import libvirt

URI = 'qemu:///system'
conn_ro = libvirt.openReadOnly(URI)
conn_rw = libvirt.open(URI)

def list_domains(flag: int):
    """Grab a list of domains with the provided flag"""
    result = conn_ro.listAllDomains(flag)
    return result

def get_domain_detail(vm_id):
    """
    Get a domain information
    
    Might consider getting a full summary of the 
    """
    domain = conn_ro.lookupByID(vm_id)
    return domain.info()

def create_domain(vm_id):
    """
    Start a domain
    """
    domain = conn_rw.lookupByID(vm_id)
    return True if not domain.create() else False

def destroy_domain(vm_id):
    """
    Hard power-off a domain
    This is similar to yanking the power cord or long-press the power button
    """
    domain = conn_rw.lookupByID(vm_id)
    return True if not domain.destroy() else False

def shutdown_domain(vm_id):
    """
    Shut down a domain using graceful shutdown ala power-button press or hrough the OS
    """
    domain = conn_rw.lookupByID(vm_id)
    return True if not domain.shutdown() else False

def undefine_domain(vm_id):
    """
    Delete a domain
    undefine is the libvirt-speak for deleting the entry.
    
    Note that undefining a domain does not remove all data owned by the domain;
    it's up to the developer to decide how to remove them
    """
    domain = conn_rw.lookupByID(vm_id)
    domain.unde
    return True if not domain.undefine() else False

def define_domain(domain_detail):
    """
    Create a new domain from the provided data
    """
    pass

