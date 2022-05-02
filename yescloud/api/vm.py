from flask_restx import Namespace, Resource, abort
from ..core.libvirt_bridge import domain
from ..core.libvirt_bridge import struct_n_stuff

api = Namespace('vm', 'Virtual-machine related operations')

@api.route('/')
class CreateOrDeleteVirtualMachines(Resource):
    def post(self):
        """Create virtual machine"""
        pass

    def delete(self):
        """Delete virtual machine"""
        pass


@api.route('/list')
class ListVirtualMachineByStatus(Resource):

    def get(self):
        # **facedesks**
        # WHY LIBVIRT. WHY.
        status_flag = struct_n_stuff.LIST_ALL_DOMAIN_FLAG.get('active', None)
        
        return domain.list_domains(status_flag)


@api.route('/list/<status>')
class ListVirtualMachineByStatus(Resource):

    def get(self, status: str='active'):
        # **facedesks**
        # WHY LIBVIRT. WHY.
        status = status.lower()
        status_flag = struct_n_stuff.LIST_ALL_DOMAIN_FLAG.get(status, None)

        if not status_flag: 
            abort(400, error=f'Bad status request {status}')
        
        return domain.list_domains(status_flag)


@api.route('/<int:vm_uuid>/detail')
class ViewVirtualMachineDetail(Resource):

    def get(self, vm_uuid):
        """Show VM details based on VM ID"""
        return domain.get_domain_detail(vm_uuid)


@api.route('/<int:vm_uuid>/start')
class StartVirtualMachine(Resource):

    def get(self, vm_uuid):
        """Start VM based on the VM ID"""
        return domain.create_domain(vm_uuid)


@api.route('/<int:vm_uuid>/shutdown')
class ShutDownVirtualMachine(Resource):

    def get(self, vm_uuid):
        """Gracefully shut down a VM based on VM ID"""
        return domain.shutdown_domain(vm_uuid)


@api.route('/<int:vm_uuid>/destroy')
class DestroyVirtualMachine(Resource):

    def get(self, vm_uuid):
        """Hard power-down a VM based on VM ID"""
        return domain.destroy_domain(vm_uuid)

@api.route('/<int:vm_uuid>/delete')
class DestroyVirtualMachine(Resource):

    def get(self, vm_uuid):
        """Hard power-down a VM based on VM ID"""
        return domain.destroy_domain(vm_uuid)


@api.route('/<int:vm_uuid>/clone')
class CloneVirtualMachine(Resource):

    def post(self, vm_uuid):
        pass
