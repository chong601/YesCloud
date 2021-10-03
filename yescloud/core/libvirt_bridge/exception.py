from libvirt import libvirtError
from flask_restx import abort

class YesCloudTranslateLibvirtErrorToUsableException(object):
    """Handle libvirt error on our own because libvirt error are just all smashed into libvirt.libvirtError"""

    def __init__(self, libvirt_error_obj: libvirtError) -> None:
        # Get all available error messgaes from libvirt for further processing

        # "See note above":
        # * The conn, dom and net fields should be used with extreme care.
        # * Reference counts are not incremented so the underlying objects
        # * may be deleted without notice after the error has been delivered.
        # IOW: don't use these
        # YesCloud skips these by defaults

        # Other deprecated functions are not exposed through libvirt-python

        # int  code                 # The error code, a virErrorNumber
        self.error_code = libvirt_error_obj.get_error_code()
        # Generate error code messages
        self.error_code_msg = self.getVirErrorNumber()
        # int  domain               # What part of the library raised this error
        self.error_domain = libvirt_error_obj.get_error_domain()
        # Generate error domain messages
        self.error_domain_msg = self.getvirErrorDomain()
        # virErrorLevel  level      # how consequent is the error
        self.error_level = libvirt_error_obj.get_error_level()
        # Generate error level message
        self.error_level_msg = self.getVirErrorLevel()
        # char *  message           # human-readable informative error message
        self.error_message = libvirt_error_obj.get_error_message()
        # char *  str1              # extra string information
        self.str1 = libvirt_error_obj.get_str1()
        # char *  str1              # extra string information
        self.str2 = libvirt_error_obj.get_str2()
        # char *  str1              # extra string information
        self.str3 = libvirt_error_obj.get_str3()
        # int  int1                 # extra number information
        self.int1 = libvirt_error_obj.get_int1()
        # int  int1                 # extra number information
        self.int2 = libvirt_error_obj.get_int2()

    def getvirErrorDomain(self):
        return {
        # Start of virErrorDomain struct
        # enum virErrorDomain {
            # VIR_FROM_NONE  =  0 (0x0)
            0: {'type': None, 'description': None},
            # VIR_FROM_XEN  =  1 (0x1)                  # Error at Xen hypervisor layer
            1: {'type': 'xen', 'description': 'Error at Xen hypervisor layer'},
            # VIR_FROM_XEND  =  2 (0x2)                 # Error at connection with xend daemon
            2: {'type': 'xend', 'description': 'Error at connection with xend daemon'},
            # VIR_FROM_XENSTORE  =  3 (0x3)             # Error at connection with xen store
            3: {'type': 'xenstore', 'description': 'Error at connection with xen store'},
            # VIR_FROM_SEXPR  =  4 (0x4)                # Error in the S-Expression code
            4: {'type': 'sexpr', 'description': 'Error in the S-Expression code'},
            # VIR_FROM_XML  =  5 (0x5)                  # Error in the XML code
            5: {'type': 'xml', 'description': 'Error in the XML code'},
            # VIR_FROM_DOM  =  6 (0x6)                  # Error when operating on a domain
            6: {'type': 'domain', 'description': 'Error when operating on a domain'},
            # VIR_FROM_RPC  =  7 (0x7)                  # Error in the XML-RPC code
            7: {'type': 'rpc', 'description': 'Error in the XML-RPC code'},
            # VIR_FROM_PROXY  =  8 (0x8)                # Error in the proxy code; unused since 0.8.6
            8: {'type': 'proxy', 'description': 'Error in the proxy code', 'notice': 'This error is unused since 0.8.6'},
            # VIR_FROM_CONF  =  9 (0x9)                 # Error in the configuration file handling
            9: {'type': 'config', 'description': 'Error in the configuration file handling'},
            # VIR_FROM_QEMU  =  10 (0xa)                # Error at the QEMU daemon
            10: {'type': 'qemu', 'description': 'Error at the QEMU daemon'},
            # VIR_FROM_NET  =  11 (0xb)                 # Error when operating on a network
            11: {'type': 'net', 'description': 'Error when operating on a network'},
            # VIR_FROM_TEST  =  12 (0xc)                # Error from test driver
            12: {'type': 'test', 'description': 'Error from test driver'},
            # VIR_FROM_REMOTE  =  13 (0xd)              # Error from remote driver
            13: {'type': 'remote', 'description': 'Error from remote driver'},
            # VIR_FROM_OPENVZ  =  14 (0xe)              # Error from OpenVZ driver
            14: {'type': 'openvz', 'description': 'Error from OpenVZ driver'},
            # VIR_FROM_XENXM  =  15 (0xf)               # Error at Xen XM layer
            15: {'type': 'xenxm', 'description': 'Error at Xen XM layer'},
            # VIR_FROM_STATS_LINUX  =  16 (0x10)        # Error in the Linux Stats code
            16: {'type': 'stats-linux', 'description': 'Error in the Linux Stats code'},
            # VIR_FROM_LXC  =  17 (0x11)                # Error from Linux Container driver
            17: {'type': 'lxc', 'description': 'Error from Linux Container driver'},
            # VIR_FROM_STORAGE  =  18 (0x12)            # Error from storage driver
            18: {'type': 'storage', 'description': 'Error from storage driver'},
            # VIR_FROM_NETWORK  =  19 (0x13)            # Error from network config
            19: {'type': 'network', 'description': 'Error from network config'},
            # VIR_FROM_DOMAIN  =  20 (0x14)             # Error from domain config
            20: {'type': 'domain', 'description': 'Error from domain config'},
            # VIR_FROM_UML  =  21 (0x15)                # Error at the UML driver; unused since 5.0.0
            21: {'type': 'uml', 'description': 'Error at the UML driver', 'notice': 'This error is unused since 5.0.0'},
            # VIR_FROM_NODEDEV  =  22 (0x16)            # Error from node device monitor
            22: {'type': 'nodedev', 'description': 'Error from node device monitor'},
            # VIR_FROM_XEN_INOTIFY  =  23 (0x17)        # Error from xen inotify layer
            23: {'type': 'xen-inotify', 'description': 'Error from xen inotify layer'},
            # VIR_FROM_SECURITY  =  24 (0x18)           # Error from security framework
            24: {'type': 'security', 'description': 'Error from security framework'},
            # VIR_FROM_VBOX  =  25 (0x19)               # Error from VirtualBox driver
            25: {'type': 'virtualbox', 'description': 'Error from VirtualBox driver'},
            # VIR_FROM_INTERFACE  =  26 (0x1a)          # Error when operating on an interface
            26: {'type': 'interface', 'description': 'Error when operating on an interface'},
            # VIR_FROM_ONE  =  27 (0x1b)                # The OpenNebula driver no longer exists. Retained for ABI/API compat only
            27: {'type': 'opennebula-one', 'description': 'Error from OpenNebula driver', 'notice': 'OpenNebula driver no longer exists and is retained for ABI/API compatibility only'},
            # VIR_FROM_ESX  =  28 (0x1c)                # Error from ESX driver
            28: {'type': 'esx', 'description': 'Error from ESX driver'},
            # VIR_FROM_PHYP  =  29 (0x1d)               # Error from the phyp driver, unused since 6.0.0
            29: {'type': 'phyp', 'description': 'Error from the phyp driver', 'notice': 'This error is unused since 6.0.0'},
            # VIR_FROM_SECRET  =  30 (0x1e)             # Error from secret storage
            30: {'type': 'secret', 'description': 'Error from secret storage'},
            # VIR_FROM_CPU  =  31 (0x1f)                # Error from CPU driver
            31: {'type': 'cpu', 'description': 'Error from CPU driver'},
            # VIR_FROM_XENAPI  =  32 (0x20)             # Error from XenAPI
            32: {'type': 'xenapi', 'description': 'Error from XenAPI'},
            # VIR_FROM_NWFILTER  =  33 (0x21)           # Error from network filter driver
            33: {'type': 'nwfilter', 'description': 'Error from network filter driver'},
            # VIR_FROM_HOOK  =  34 (0x22)               # Error from Synchronous hooks
            34: {'type': 'hook', 'description': 'Error from Synchronous hooks'},
            # VIR_FROM_DOMAIN_SNAPSHOT  =  35 (0x23)    # Error from domain snapshot
            35: {'type': 'domain-snapshot', 'description': 'Error from domain snapshot'},
            # VIR_FROM_AUDIT  =  36 (0x24)              # Error from auditing subsystem
            36: {'type': 'audit', 'description': 'Error from auditing subsystem'},
            # VIR_FROM_SYSINFO  =  37 (0x25)            # Error from sysinfo/SMBIOS
            37: {'type': 'sysinfo', 'description': 'Error from sysinfo/SMBIOS'},
            # VIR_FROM_STREAMS  =  38 (0x26)            # Error from I/O streams
            38: {'type': 'streams', 'description': 'Error from I/O streams'},
            # VIR_FROM_VMWARE  =  39 (0x27)             # Error from VMware driver
            39: {'type': 'vmware', 'description': 'Error from VMware driver'},
            # VIR_FROM_EVENT  =  40 (0x28)              # Error from event loop impl
            40: {'type': 'event', 'description': 'Error from event loop impl'},
            # VIR_FROM_LIBXL  =  41 (0x29)              # Error from libxenlight driver
            41: {'type': 'libxl', 'description': 'Error from libxenlight driver'},
            # VIR_FROM_LOCKING  =  42 (0x2a)            # Error from lock manager
            42: {'type': 'locking', 'description': 'Error from lock manager'},
            # VIR_FROM_HYPERV  =  43 (0x2b)             # Error from Hyper-V driver
            43: {'type': 'hyper-v', 'description': 'Error from Hyper-V driver'},
            # VIR_FROM_CAPABILITIES  =  44 (0x2c)       # Error from capabilities
            44: {'type': 'capabilities', 'description': 'Error from capabilities'},
            # VIR_FROM_URI  =  45 (0x2d)                # Error from URI handling
            45: {'type': 'uri', 'description': 'Error from URI handling'},
            # VIR_FROM_AUTH  =  46 (0x2e)               # Error from auth handling
            46: {'type': 'auth', 'description': 'Error from auth handling'},
            # VIR_FROM_DBUS  =  47 (0x2f)               # Error from DBus
            47: {'type': 'd-bus', 'description': 'Error from DBus'},
            # VIR_FROM_PARALLELS  =  48 (0x30)          # Error from Parallels
            48: {'type': 'parallels', 'description': 'Error from Parallels'},
            # VIR_FROM_DEVICE  =  49 (0x31)             # Error from Device
            49: {'type': 'device', 'description': 'Error from Device'},
            # VIR_FROM_SSH  =  50 (0x32)                # Error from libssh2 connection transport
            50: {'type': 'ssh', 'description': 'Error from libssh2 connection transport'},
            # VIR_FROM_LOCKSPACE  =  51 (0x33)          # Error from lockspace
            51: {'type': 'lockspace', 'description': 'Error from lockspace'},
            # VIR_FROM_INITCTL  =  52 (0x34)            # Error from initctl device communication
            52: {'type': 'initctl', 'description': 'Error from initctl device communication'},
            # VIR_FROM_IDENTITY  =  53 (0x35)           # Error from identity code
            53: {'type': 'identify', 'description': 'Error from identity code'},
            # VIR_FROM_CGROUP  =  54 (0x36)             # Error from cgroups
            54: {'type': 'cgroup', 'description': 'Error from cgroups'},
            # VIR_FROM_ACCESS  =  55 (0x37)             # Error from access control manager
            55: {'type': 'access', 'description': 'Error from access control manager'},
            # VIR_FROM_SYSTEMD  =  56 (0x38)            # Error from systemd code
            56: {'type': 'systemd', 'description': 'Error from systemd code'},
            # VIR_FROM_BHYVE  =  57 (0x39)              # Error from bhyve driver
            57: {'type': 'bhyve', 'description': 'Error from bhyve driver'},
            # VIR_FROM_CRYPTO  =  58 (0x3a)             # Error from crypto code
            58: {'type': 'crypto', 'description': 'Error from crypto code'},
            # VIR_FROM_FIREWALL  =  59 (0x3b)           # Error from firewall
            59: {'type': 'firewall', 'description': 'Error from firewall'},
            # VIR_FROM_POLKIT  =  60 (0x3c)             # Error from polkit code
            60: {'type': 'polkit', 'description': 'Error from polkit code'},
            # VIR_FROM_THREAD  =  61 (0x3d)             # Error from thread utils
            61: {'type': 'thread', 'description': 'Error from thread utils'},
            # VIR_FROM_ADMIN  =  62 (0x3e)              # Error from admin backend
            62: {'type': 'admin', 'description': 'Error from admin backend'},
            # VIR_FROM_LOGGING  =  63 (0x3f)            # Error from log manager
            63: {'type': 'logging', 'description': 'Error from log manager'},
            # VIR_FROM_XENXL  =  64 (0x40)              # Error from Xen xl config code
            64: {'type': 'xen-xl', 'description': 'Error from Xen xl config code'},
            # VIR_FROM_PERF  =  65 (0x41)               # Error from perf
            65: {'type': 'perf', 'description': 'Error from perf'},
            # VIR_FROM_LIBSSH  =  66 (0x42)             # Error from libssh connection transport
            66: {'type': 'libssh', 'description': 'Error from libssh connection transport'},
            # VIR_FROM_RESCTRL  =  67 (0x43)            # Error from resource control
            67: {'type': 'res-ctrl', 'description': 'Error from resource control'},
            # VIR_FROM_FIREWALLD  =  68 (0x44)          # Error from firewalld
            68: {'type': 'firewalld', 'description': 'Error from firewalld'},
            # VIR_FROM_DOMAIN_CHECKPOINT  =  69 (0x45)  # Error from domain checkpoint
            69: {'type': 'domain-checkpoint', 'description': 'Error from domain checkpoint'},
            # VIR_FROM_TPM  =  70 (0x46)                # Error from TPM
            70: {'type': 'tpm', 'description': 'Error from TPM'},
            # VIR_FROM_BPF  =  71 (0x47)                # Error from BPF code
            71: {'type': 'bpf', 'description': 'Error from BPF code'},
            # VIR_FROM_CH  =  72 (0x48)                 # Error from Cloud-Hypervisor driver
            72: {'type': 'cloud-hypervisor', 'description': 'Error from Cloud-Hypervisor driver'},
            # VIR_ERR_DOMAIN_LAST  =  73 (0x49)
            73: {'type': 'last', 'description': None}
        # }
        }.get(self.error_domain, {'error': f'{self.error_domain} is not found in virErrorDomain. Please file a bug report'})
    


    def getVirErrorLevel(self):
        # enum virErrorLevel {
        return {
            # VIR_ERR_NONE  =  0 (0x0)
            0: {'level': '', 'type': '', 'description': ''},
            # VIR_ERR_WARNING  =  1 (0x1)   # A simple warning
            1: {'type': 'warning', 'description': 'A warning has been encountered.'},
            # VIR_ERR_ERROR  =  2 (0x2)     # An error
            2: {'type': 'error', 'description': 'An error has been encountered.'},
        }.get(self.error_level, {'error': f'{self.error_level} is not found in virErrorLevel. Please file a bug report'})
        # }


    def getVirErrorNumber(self):
        # enum virErrorNumber {
        return {
            # VIR_ERR_OK  =  0 (0x0)
            0: {'level': '', 'type': '', 'description': ''},
            # VIR_ERR_INTERNAL_ERROR  =  1 (0x1)  # internal error
            1: {'level': 'error', 'type': 'internal-error', 'description': 'Internal error'},
            # VIR_ERR_NO_MEMORY  =  2 (0x2)  # memory allocation failure
            2: {'level': 'error', 'type': 'no-memory', 'description': 'Memory allocation failure'},
            # VIR_ERR_NO_SUPPORT  =  3 (0x3)  # no support for this function
            3: {'level': 'error', 'type': 'no-support', 'description': 'No support for this function'},
            # VIR_ERR_UNKNOWN_HOST  =  4 (0x4)  # could not resolve hostname
            4: {'level': 'error', 'type': 'unknown-host', 'description': 'Could not resolve hostname'},
            # VIR_ERR_NO_CONNECT  =  5 (0x5)  # can't connect to hypervisor
            5: {'level': 'error', 'type': 'no-connection', 'description': 'Cannot connect to hypervisor'},
            # VIR_ERR_INVALID_CONN  =  6 (0x6)  # invalid connection object
            6: {'level': 'error', 'type': 'invalid-connection', 'description': 'Invalid connection object'},
            # VIR_ERR_INVALID_DOMAIN  =  7 (0x7)  # invalid domain object
            7: {'level': 'error', 'type': 'invalid-domain', 'description': 'Invalid domain object'},
            # VIR_ERR_INVALID_ARG  =  8 (0x8)  # invalid function argument
            8: {'level': 'error', 'type': 'invalid-arg', 'description': 'Invalid function argument'},
            # VIR_ERR_OPERATION_FAILED  =  9 (0x9)  # a command to hypervisor failed
            9: {'level': 'error', 'type': 'operation-failed', 'description': 'Command issued to hypervisor failed'},
            # VIR_ERR_GET_FAILED  =  10 (0xa)  # a HTTP GET command to failed
            10: {'level': 'error', 'type': 'http-get-failed', 'description': 'HTTP GET command tfailed'},
            # VIR_ERR_POST_FAILED  =  11 (0xb)  # a HTTP POST command to failed
            11: {'level': 'error', 'type': 'http-post-failed', 'description': 'HTTP POST command failed'},
            # VIR_ERR_HTTP_ERROR  =  12 (0xc)  # unexpected HTTP error codE
            12: {'level': 'error', 'type': 'http-error', 'description': 'Unexpected HTTP error code'},
            # VIR_ERR_SEXPR_SERIAL  =  13 (0xd)  # failure to serialize an S-Expr
            13: {'level': 'error', 'type': 's-expr-serialization', 'description': 'Failed to serialize a S-Expr'},
            # VIR_ERR_NO_XEN  =  14 (0xe)  # could not open Xen hypervisor control
            14: {'level': 'error', 'type': 'no-xen', 'description': 'Cannot open Xen hypervisor control'},
            # VIR_ERR_XEN_CALL  =  15 (0xf)  # failure doing an hypervisor call
            15: {'level': 'error', 'type': 'xen-call', 'description': 'Failure doing a Xen hypervisor call'},
            # VIR_ERR_OS_TYPE  =  16 (0x10)  # unknown OS type
            16: {'level': 'error', 'type': 'os-type', 'description': 'Unknown OS type'},
            # VIR_ERR_NO_KERNEL  =  17 (0x11)  # missing kernel information
            17: {'level': 'error', 'type': 'no-kernel', 'description': 'Missing kernel information'},
            # VIR_ERR_NO_ROOT  =  18 (0x12)  # missing root device information
            18: {'level': 'error', 'type': 'no-root', 'description': 'Missing root device information'},
            # VIR_ERR_NO_SOURCE  =  19 (0x13)  # missing source device information
            19: {'level': 'error', 'type': 'no-source', 'description': 'Missing source device information'},
            # VIR_ERR_NO_TARGET  =  20 (0x14)  # missing target device information
            20: {'level': 'error', 'type': 'no-target', 'description': 'Missing target device information'},
            # VIR_ERR_NO_NAME  =  21 (0x15)  # missing domain name information
            21: {'level': 'error', 'type': 'no-name', 'description': 'Missing domain name information'},
            # VIR_ERR_NO_OS  =  22 (0x16)  # missing domain OS information
            22: {'level': 'error', 'type': 'no-os', 'description': 'Missing domain OS information'},
            # VIR_ERR_NO_DEVICE  =  23 (0x17)  # missing domain devices information
            23: {'level': 'error', 'type': 'no-device', 'description': 'Missing domain device information'},
            # VIR_ERR_NO_XENSTORE  =  24 (0x18)  # could not open Xen Store control
            24: {'level': 'error', 'type': 'no-xenstore', 'description': 'Cannot open Xen Store control'},
            # VIR_ERR_DRIVER_FULL  =  25 (0x19)  # too many drivers registered
            25: {'level': 'error', 'type': 'driver-full', 'description': 'Too many drivers'},
            # VIR_ERR_CALL_FAILED  =  26 (0x1a)  # not supported by the drivers (DEPRECATED)
            26: {'level': 'error', 'type': 'call-failed', 'description': 'Not supported by the driver'},
            # VIR_ERR_XML_ERROR  =  27 (0x1b)  # an XML description is not well formed or broken
            27: {'level': 'error', 'type': 'xml-error', 'description': 'Not well-formed or broken XML description'},
            # VIR_ERR_DOM_EXIST  =  28 (0x1c)  # the domain already exist
            28: {'level': 'error', 'type': 'domain-exist', 'description': 'Domain already exists'},
            # VIR_ERR_OPERATION_DENIED  =  29 (0x1d)  # operation forbidden on read-only connections
            29: {'level': 'error', 'type': 'operation-denied', 'description': 'Operation not allowed on read-only connections'},
            # VIR_ERR_OPEN_FAILED  =  30 (0x1e)  # failed to open a conf file
            30: {'level': 'error', 'type': 'conf-file-open-failed', 'description': 'Failed to open configuration file'},
            # VIR_ERR_READ_FAILED  =  31 (0x1f)  # failed to read a conf file
            31: {'level': 'error', 'type': 'conf-file-read-failed', 'description': 'Failed to read configuration file'},
            # VIR_ERR_PARSE_FAILED  =  32 (0x20)  # failed to parse a conf file
            32: {'level': 'error', 'type': 'conf-file-parse-failed', 'description': 'Failed to parse configuration file'},
            # VIR_ERR_CONF_SYNTAX  =  33 (0x21)  # failed to parse the syntax of a conf file
            33: {'level': 'error', 'type': 'conf-file-syntax-error', 'description': 'Syntax error found in configuration file'},
            # VIR_ERR_WRITE_FAILED  =  34 (0x22)  # failed to write a conf file
            34: {'level': 'error', 'type': 'conf-file-write-failed', 'description': 'Failed to write configuration file'},
            # VIR_ERR_XML_DETAIL  =  35 (0x23)  # detail of an XML error
            35: {'level': 'error', 'type': 'xml-detail-error', 'description': 'XML detail error'},
            # VIR_ERR_INVALID_NETWORK  =  36 (0x24)  # invalid network object
            36: {'level': 'error', 'type': 'invalid-network', 'description': 'Invalid network object'},
            # VIR_ERR_NETWORK_EXIST  =  37 (0x25)  # the network already exist
            37: {'level': 'error', 'type': 'network-already-exist', 'description': 'Network already exist'},
            # VIR_ERR_SYSTEM_ERROR  =  38 (0x26)  # general system call failure
            38: {'level': 'error', 'type': 'system-error', 'description': 'General system call failure'},
            # VIR_ERR_RPC  =  39 (0x27)  # some sort of RPC error
            39: {'level': 'error', 'type': 'rpc', 'description': 'RPC call error'},
            # VIR_ERR_GNUTLS_ERROR  =  40 (0x28)  # error from a GNUTLS call
            40: {'level': 'error', 'type': 'gnutls', 'description': 'GNU TLS error'},
            # VIR_WAR_NO_NETWORK  =  41 (0x29)  # failed to start network
            41: {'level': 'warning', 'type': 'network', 'description': 'Failed to start network'},
            # VIR_ERR_NO_DOMAIN  =  42 (0x2a)  # domain not found or unexpectedly disappeared
            42: {'level': 'error', 'type': 'no-domain', 'description': 'Domain not found or unexpectedly dissappeared'},
            # VIR_ERR_NO_NETWORK  =  43 (0x2b)  # network not found
            43: {'level': 'error', 'type': 'no-network', 'description': 'Network not found'},
            # VIR_ERR_INVALID_MAC  =  44 (0x2c)  # invalid MAC address
            44: {'level': 'error', 'type': 'mac', 'description': 'Invalid MAC address'},
            # VIR_ERR_AUTH_FAILED  =  45 (0x2d)  # authentication failed
            45: {'level': 'error', 'type': 'authentication', 'description': 'Authentication failed'},
            # VIR_ERR_INVALID_STORAGE_POOL  =  46 (0x2e)  # invalid storage pool object
            46: {'level': 'error', 'type': 'storage-pool', 'description': 'Invalid storage pool object'},
            # VIR_ERR_INVALID_STORAGE_VOL  =  47 (0x2f)  # invalid storage vol object
            47: {'level': 'error', 'type': 'storage-volume', 'description': 'Invalid storage volume object'},
            # VIR_WAR_NO_STORAGE  =  48 (0x30)  # failed to start storage
            48: {'level': 'warning', 'type': 'storage', 'description': 'Failed to start storage'},
            # VIR_ERR_NO_STORAGE_POOL  =  49 (0x31)  # storage pool not found
            49: {'level': 'error', 'type': 'storage-pool', 'description': 'Storage pool not found'},
            # VIR_ERR_NO_STORAGE_VOL  =  50 (0x32)  # storage volume not found
            50: {'level': 'error', 'type': 'storage-volume', 'description': 'Storage volume note found'},
            # VIR_WAR_NO_NODE  =  51 (0x33)  # failed to start node driver
            51: {'level': 'warning', 'type': 'node', 'description': 'Failed to start node driver'},
            # VIR_ERR_INVALID_NODE_DEVICE  =  52 (0x34)  # invalid node device object
            52: {'level': 'error', 'type': 'node-device', 'description': 'Invalid node device object'},
            # VIR_ERR_NO_NODE_DEVICE  =  53 (0x35)  # node device not found
            53: {'level': 'error', 'type': 'node-device', 'description': 'Node device not found'},
            # VIR_ERR_NO_SECURITY_MODEL  =  54 (0x36)  # security model not found
            54: {'level': 'error', 'type': 'security-model', 'description': 'Security model not found'},
            # VIR_ERR_OPERATION_INVALID  =  55 (0x37)  # operation is not applicable at this time
            55: {'level': 'error', 'type': 'invalid-operation', 'description': 'Operation is not applicable at this time'},
            # VIR_WAR_NO_INTERFACE  =  56 (0x38)  # failed to start interface driver
            56: {'level': 'warning', 'type': 'interface-driver', 'description': 'Failed to start interface driver'},
            # VIR_ERR_NO_INTERFACE  =  57 (0x39)  # interface driver not running
            57: {'level': 'error', 'type': 'interface-driver', 'description': 'Interface driver is not running'},
            # VIR_ERR_INVALID_INTERFACE  =  58 (0x3a)  # invalid interface object
            58: {'level': 'error', 'type': 'interface', 'description': 'Invalid interface object'},
            # VIR_ERR_MULTIPLE_INTERFACES  =  59 (0x3b)  # more than one matching interface found
            59: {'level': 'error', 'type': 'interface', 'description': 'Multiple interfaces found'},
            # VIR_WAR_NO_NWFILTER  =  60 (0x3c)  # failed to start nwfilter driver
            60: {'level': 'warning', 'type': 'nwfilter', 'description': 'Failed to start nwfilter'},
            # VIR_ERR_INVALID_NWFILTER  =  61 (0x3d)  # invalid nwfilter object
            61: {'level': 'error', 'type': 'nwfilter', 'description': 'Invalid nwfilter object'},
            # VIR_ERR_NO_NWFILTER  =  62 (0x3e)  # nw filter pool not found
            62: {'level': 'error', 'type': 'nwfilter', 'description': 'nwfilter pool not found'},
            # VIR_ERR_BUILD_FIREWALL  =  63 (0x3f)  # nw filter pool not found
            63: {'level': 'error', 'type': 'build-firewall', 'description': 'nwfilter pool not found'},
            # VIR_WAR_NO_SECRET  =  64 (0x40)  # failed to start secret storage
            64: {'level': 'warning', 'type': 'secret', 'description': 'Failed to start secret storage'},
            # VIR_ERR_INVALID_SECRET  =  65 (0x41)  # invalid secret
            65: {'level': 'error', 'type': 'secret', 'description': 'Invalid secret'},
            # VIR_ERR_NO_SECRET  =  66 (0x42)  # secret not found
            66: {'level': 'error', 'type': 'secret', 'description': 'Secret not found'},
            # VIR_ERR_CONFIG_UNSUPPORTED  =  67 (0x43)  # unsupported configuration construct
            67: {'level': 'error', 'type': 'unsupported-conf', 'description': 'Unsupported configuration construct'},
            # VIR_ERR_OPERATION_TIMEOUT  =  68 (0x44)  # timeout occurred during operation
            68: {'level': 'error', 'type': 'operation-timeout', 'description': 'Timeout occurred during operation'},
            # VIR_ERR_MIGRATE_PERSIST_FAILED  =  69 (0x45)  # a migration worked, but making the VM persist on the dest host failed
            69: {'level': 'error', 'type': 'migration', 'description': 'Migration succeeded, '},
            # VIR_ERR_HOOK_SCRIPT_FAILED  =  70 (0x46)  # a synchronous hook script failed
            70: {'level': 'error', 'type': 'hook-script', 'description': 'Hook script execution failed'},
            # VIR_ERR_INVALID_DOMAIN_SNAPSHOT  =  71 (0x47)  # invalid domain snapshot
            71: {'level': 'error', 'type': 'domain-snapshot', 'description': 'Invalid domain snapshot'},
            # VIR_ERR_NO_DOMAIN_SNAPSHOT  =  72 (0x48)  # domain snapshot not found
            72: {'level': 'error', 'type': 'domain-snapshot', 'description': 'Domain snapshot not found'},
            # VIR_ERR_INVALID_STREAM  =  73 (0x49)  # stream pointer not valid
            73: {'level': 'error', 'type': 'stream', 'description': 'Stream pointer is not valid'},
            # VIR_ERR_ARGUMENT_UNSUPPORTED  =  74 (0x4a)  # valid API use but unsupported by the given driver
            74: {'level': 'error', 'type': 'unsupported-argument', 'description': 'Argument unsupported for this driver'},
            # VIR_ERR_STORAGE_PROBE_FAILED  =  75 (0x4b)  # storage pool probe failed
            75: {'level': 'error', 'type': 'storage-probe', 'description': 'Stoage pool probing failure'},
            # VIR_ERR_STORAGE_POOL_BUILT  =  76 (0x4c)  # storage pool already built
            76: {'level': 'error', 'type': 'storage-pool', 'description': 'Storage pool already exists'},
            # VIR_ERR_SNAPSHOT_REVERT_RISKY  =  77 (0x4d)  # force was not requested for a risky domain snapshot revert
            77: {'level': 'error', 'type': 'snapshot-revert', 'description': 'Force argument was not requested for risky domain snapshot revert'},
            # VIR_ERR_OPERATION_ABORTED  =  78 (0x4e)  # operation on a domain was canceled/aborted by user
            78: {'level': 'error', 'type': 'operation-abort', 'description': 'Operation on a domain was cancelled/aborted by user'},
            # VIR_ERR_AUTH_CANCELLED  =  79 (0x4f)  # authentication cancelled
            79: {'level': 'error', 'type': 'auth', 'description': 'Authentication cancelled'},
            # VIR_ERR_NO_DOMAIN_METADATA  =  80 (0x50)  # The metadata is not present
            80: {'level': 'error', 'type': 'domain-metadata', 'description': 'Domain metadata is not present'},
            # VIR_ERR_MIGRATE_UNSAFE  =  81 (0x51)  # Migration is not safe
            81: {'level': 'error', 'type': 'migration', 'description': 'Migration is not safe'},
            # VIR_ERR_OVERFLOW  =  82 (0x52)  # integer overflow
            82: {'level': 'error', 'type': 'integer-overflow', 'description': 'Integer overflow was detected'},
            # VIR_ERR_BLOCK_COPY_ACTIVE  =  83 (0x53)  # action prevented by block copy job
            83: {'level': 'error', 'type': 'block-copy', 'description': 'The action requested was blocked by a block copy job'},
            # VIR_ERR_OPERATION_UNSUPPORTED  =  84 (0x54)  # The requested operation is not supported
            84: {'level': 'error', 'type': 'operation-unsupported', 'description': 'The requested operation is not supported'},
            # VIR_ERR_SSH  =  85 (0x55)  # error in ssh transport driver
            85: {'level': 'error', 'type': 'ssh', 'description': 'Error in ssh transport driver'},
            # VIR_ERR_AGENT_UNRESPONSIVE  =  86 (0x56)  # guest agent is unresponsive, not running or not usable
            86: {'level': 'error', 'type': 'guest-agent', 'description': 'Guest agent is unresponsive, not running or not usable'},
            # VIR_ERR_RESOURCE_BUSY  =  87 (0x57)  # resource is already in use
            87: {'level': 'error', 'type': 'resource', 'description': 'Resource is already in use'},
            # VIR_ERR_ACCESS_DENIED  =  88 (0x58)  # operation on the object/resource was denied
            88: {'level': 'error', 'type': 'access-denied', 'description': 'Operation on the object or resource was denied'},
            # VIR_ERR_DBUS_SERVICE  =  89 (0x59)  # error from a dbus service
            89: {'level': 'error', 'type': 'dbus', 'description': 'Error from D-Bus service'},
            # VIR_ERR_STORAGE_VOL_EXIST  =  90 (0x5a)  # the storage vol already exists
            90: {'level': 'error', 'type': 'storage-volume', 'description': 'The storage volume already exists'},
            # VIR_ERR_CPU_INCOMPATIBLE  =  91 (0x5b)  # given CPU is incompatible with host CPU
            91: {'level': 'error', 'type': 'cpu', 'description': 'Provided CPU is incompatible with host CPU'},
            # VIR_ERR_XML_INVALID_SCHEMA  =  92 (0x5c)  # XML document doesn't validate against schema
            92: {'level': 'error', 'type': 'xml-schema', 'description': 'XML document does not validate against schema'},
            # VIR_ERR_MIGRATE_FINISH_OK  =  93 (0x5d)  # Finish API succeeded but it is expected to return NULL
            93: {'level': 'error', 'type': 'migration', 'description': 'Migration API succeeeded, but did not get the expected NULL return data'},
            # VIR_ERR_AUTH_UNAVAILABLE  =  94 (0x5e)  # authentication unavailable
            94: {'level': 'error', 'type': 'authentication', 'description': 'Authentication unavailable'},
            # VIR_ERR_NO_SERVER  =  95 (0x5f)  # Server was not found
            95: {'level': 'error', 'type': 'server', 'description': 'Server was not found'},
            # VIR_ERR_NO_CLIENT  =  96 (0x60)  # Client was not found
            96: {'level': 'error', 'type': 'client', 'description': 'Client was not found'},
            # VIR_ERR_AGENT_UNSYNCED  =  97 (0x61)  # guest agent replies with wrong id to guest-sync command (DEPRECATED)
            97: {'level': 'error', 'type': 'agent-unsynced', 'description': 'Guest agent replied with wrong ID to guest-sync command'},
            # VIR_ERR_LIBSSH  =  98 (0x62)  # error in libssh transport driver
            98: {'level': 'error', 'type': 'libssh', 'description': 'Error in libssh transport driver'},
            # VIR_ERR_DEVICE_MISSING  =  99 (0x63)  # fail to find the desired device
            99: {'level': 'error', 'type': 'device-missing', 'description': 'Unabled to find the desired device'},
            # VIR_ERR_INVALID_NWFILTER_BINDING  =  100 (0x64)  # invalid nwfilter binding
            100: {'level': 'error', 'type': 'nwfilter-binding', 'description': 'Invalid nwfilter binding'},
            # VIR_ERR_NO_NWFILTER_BINDING  =  101 (0x65)  # no nwfilter binding
            101: {'level': 'error', 'type': 'nwfilter-binding', 'description': 'No nwfilter binding'},
            # VIR_ERR_INVALID_DOMAIN_CHECKPOINT  =  102 (0x66)  # invalid domain checkpoint
            102: {'level': 'error', 'type': 'domain-checkpoint', 'description': 'Invalid domain checkpoint'},
            # VIR_ERR_NO_DOMAIN_CHECKPOINT  =  103 (0x67)  # domain checkpoint not found
            103: {'level': 'error', 'type': 'domain-checkpoint', 'description': 'Domain checkpoint not found'},
            # VIR_ERR_NO_DOMAIN_BACKUP  =  104 (0x68)  # domain backup job id not found
            104: {'level': 'error', 'type': 'domain-backup', 'description': 'Domain backup job ID not found'},
            # VIR_ERR_INVALID_NETWORK_PORT  =  105 (0x69)  # invalid network port object
            105: {'level': 'error', 'type': 'network-port', 'description': 'Invalid network port object'},
            # VIR_ERR_NETWORK_PORT_EXIST  =  106 (0x6a)  # the network port already exist
            106: {'level': 'error', 'type': 'network-port', 'description': 'Network port already exist'},
            # VIR_ERR_NO_NETWORK_PORT  =  107 (0x6b)  # network port not found
            107: {'level': 'error', 'type': 'network-port', 'description': 'Network port not found'},
            # VIR_ERR_NO_HOSTNAME  =  108 (0x6c)  # no domain's hostname found
            108: {'level': 'error', 'type': 'domain-hostname', 'description': 'Domain hostname not found'},
            # VIR_ERR_CHECKPOINT_INCONSISTENT  =  109 (0x6d)  # checkpoint can't be used
            109: {'level': 'error', 'type': 'checkpoint-inconsistent', 'description': 'Checkpoint cannot be used'},
            # VIR_ERR_MULTIPLE_DOMAINS  =  110 (0x6e)  # more than one matching domain found
            110: {'level': 'error', 'type': 'domain', 'description': 'More than pne matching domain found'},
            # VIR_ERR_NUMBER_LAST  =  111 (0x6f)
            111: {'level': '', 'type': '', 'description': ''},
        }.get(self.error_code, {'error': f'{self.error_code} is not found in virErrorLevel. Please file a bug report'})
        # }


def handle_libvirt_exception(func):
    def wrapper(*args, **kwargs):
        try: 
            return func(*args, *kwargs)
        except libvirtError as e:
            real_exception = YesCloudTranslateLibvirtErrorToUsableException(e)
            abort(400, **{'error': vars(real_exception)})
    return wrapper

