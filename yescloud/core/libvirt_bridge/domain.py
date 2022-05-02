import libvirt
from .exception import handle_libvirt_exception

URI = 'qemu:///system'
conn_ro = libvirt.openReadOnly(URI)
conn_rw = libvirt.open(URI)

def list_domains(flag: int):
    """Grab a list of domains with the provided flag"""
    result = conn_ro.listAllDomains(flag)
    return result

@handle_libvirt_exception
def get_domain_detail(vm_uuid):
    """
    Get a domain information
    
    Might consider getting a full summary of the 
    """
    domain = conn_ro.lookupByID(vm_uuid)
    return domain.info()

@handle_libvirt_exception
def create_domain(vm_uuid):
    """
    Start a domain
    """
    domain = conn_rw.lookupByID(vm_uuid)
    return True if not domain.create() else False

@handle_libvirt_exception
def destroy_domain(vm_uuid):
    """
    Hard power-off a domain
    This is similar to yanking the power cord or long-press the power button
    """
    domain = conn_rw.lookupByID(vm_uuid)
    return True if not domain.destroy() else False

@handle_libvirt_exception
def shutdown_domain(vm_uuid):
    """
    Shut down a domain using graceful shutdown ala power-button press or hrough the OS
    """
    domain = conn_rw.lookupByID(vm_uuid)
    return True if not domain.shutdown() else False

@handle_libvirt_exception
def undefine_domain(vm_uuid):
    """
    Delete a domain
    undefine is the libvirt-speak for deleting the entry.
    
    Note that undefining a domain does not remove all data owned by the domain;
    it's up to the developer to decide how to remove them
    """
    domain = conn_rw.lookupByID(vm_uuid)
    return True if not domain.undefine() else False

@handle_libvirt_exception
def define_domain(domain_detail):
    """
    Create a new domain from the provided data
    """
    pass

