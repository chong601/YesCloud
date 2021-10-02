LIST_ALL_DOMAIN_FLAG = {
# enum virConnectListAllDomainsFlags {
    # VIR_CONNECT_LIST_DOMAINS_ACTIVE 	= 	1 (0x1; 1 << 0)
    'active': 1 << 0,
    # VIR_CONNECT_LIST_DOMAINS_INACTIVE 	= 	2 (0x2; 1 << 1)
    'inactive': 1 << 1,
    # VIR_CONNECT_LIST_DOMAINS_PERSISTENT 	= 	4 (0x4; 1 << 2)
    'persistent': 1 << 2,
    # VIR_CONNECT_LIST_DOMAINS_TRANSIENT 	= 	8 (0x8; 1 << 3)
    'transient': 1 << 3,
    # VIR_CONNECT_LIST_DOMAINS_RUNNING 	= 	16 (0x10; 1 << 4)
    'running': 1 << 4,
    # VIR_CONNECT_LIST_DOMAINS_PAUSED 	= 	32 (0x20; 1 << 5)
    'paused': 1 << 5,
    # VIR_CONNECT_LIST_DOMAINS_SHUTOFF 	= 	64 (0x40; 1 << 6)
    'shutoff': 1 << 6,
    # VIR_CONNECT_LIST_DOMAINS_OTHER 	= 	128 (0x80; 1 << 7)
    'other': 1 << 7,
    # VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE 	= 	256 (0x100; 1 << 8)
    'with-managed-save': 1 << 8,
    # VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE 	= 	512 (0x200; 1 << 9)
    'without-managed-save': 1 << 9,
    # VIR_CONNECT_LIST_DOMAINS_AUTOSTART 	= 	1024 (0x400; 1 << 10)
    'autostart': 1 << 10,
    # VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART 	= 	2048 (0x800; 1 << 11)
    'no-autostart': 1 << 11,
    # VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT 	= 	4096 (0x1000; 1 << 12)
    'with-snapshot': 1 << 12,
    # VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT 	= 	8192 (0x2000; 1 << 13)
    'without-snapshot': 1 << 13,
    # VIR_CONNECT_LIST_DOMAINS_HAS_CHECKPOINT 	= 	16384 (0x4000; 1 << 14)
    'with-checkpoint': 1 << 14,
    # VIR_CONNECT_LIST_DOMAINS_NO_CHECKPOINT 	= 	32768 (0x8000; 1 << 15)
    'without-checkpoint': 1 << 15
}
# }