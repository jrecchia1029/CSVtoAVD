

def generateGroupVarsTenants(inventory_file):
    yaml = '''# DC1 Tenants Networks
# Documentation of Tenant specific information - Vlans/VRFs

tenants: 
    # Tenant A Specific Information - VRFs / VLANs
      Tenant_A:
        mac_vrf_vni_base: 10000
        vrfs:
          Tenant_A_OP_Zone:
            vrf_vni: 10
            vtep_diagnostic:
              loopback: 100
              loopback_ip_range: 10.255.1.0/24
            svis:
              110:
                name: Tenant_A_OP_Zone_1
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.1.10.0/24
              111:
                vni_override: 50111
                name: Tenant_A_OP_Zone_2
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.1.11.0/24
          Tenant_A_WEB_Zone:
            vrf_vni: 11
            svis:
              120:
                name: Tenant_A_WEB_Zone_1
                tags: [ web, erp1 ]
                enabled: true
                ip_subnet: 10.1.20.0/24
              121:
                name: Tenant_A_WEBZone_2
                tags: [ web ]
                enabled: true
                ip_subnet: 10.1.21.0/24
          Tenant_A_APP_Zone:
            vrf_vni: 12
            svis:
              130:
                name: Tenant_A_APP_Zone_1
                tags: [ app, erp1 ]
                enabled: true
                ip_subnet: 10.1.30.0/24
              131:
                name: Tenant_A_APP_Zone_2
                tags: [ app ]
                enabled: true
                ip_subnet: 10.1.31.0/24
          Tenant_A_DB_Zone:
            vrf_vni: 13
            svis:
              140:
                name: Tenant_A_DB_BZone_1
                tags: [ db, erp1 ]
                enabled: true
                ip_subnet: 10.1.40.0/24
              141:
                name: Tenant_A_DB_Zone_2
                tags: [ db ]
                enabled: true
                ip_subnet: 10.1.41.0/24
          Tenant_A_WAN_Zone:
            vrf_vni: 14
            svis:
              150:
                name: Tenant_A_WAN_Zone_1
                tags: [ wan ]
                enabled: true
                ip_subnet: 10.1.40.0/24
        l2vlans:
          160:
            vni_override: 50160
            name: Tenant_A_VMOTION
            tags: [ vmotion ]
          161:
            name: Tenant_A_NFS
            tags: [ nfs ]
    
    
    # Tenant B Specific Information - VRFs / VLANs
      Tenant_B:
        mac_vrf_vni_base: 20000
        vrfs:
          Tenant_B_OP_Zone:
            vrf_vni: 20
            svis:
              210:
                name: Tenant_B_OP_Zone_1
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.2.10.0/24
              211:
                name: Tenant_B_OP_Zone_2
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.2.11.0/24
          Tenant_B_WAN_Zone:
            vrf_vni: 21
            svis:
              250:
                name: Tenant_B_WAN_Zone_1
                tags: [ wan ]
                enabled: true
                ip_subnet: 10.2.50.0/24
    
    
    # Tenant C Specific Information - VRFs / VLANs
      Tenant_C:
        mac_vrf_vni_base: 30000
        vrfs:
          Tenant_C_OP_Zone:
            vrf_vni: 30
            svis:
              310:
                name: Tenant_C_OP_Zone_1
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.3.10.0/24
              311:
                name: Tenant_C_OP_Zone_2
                tags: [ opzone ]
                enabled: true
                ip_subnet: 10.3.11.0/24
          Tenant_C_WAN_Zone:
            vrf_vni: 31
            svis:
              350:
                name: Tenant_C_WAN_Zone_1
                tags: [ wan ]
                enabled: true
                ip_subnet: 10.3.50.0/24
      # ansible_demo:
      #   mac_vrf_vni_base: 40000
      #   vrfs:
      #     ansible_web_zone:
      #       vrf_vni: 30
      #       svis:
      #         410:
      #           name: ansible_demo_app_1
      #           tags: [ app ]
      #           enabled: true
      #           ip_subnet: 10.4.10.0/24
      #         411:
      #           name: ansible_demo_app_2
      #           tags: [ app ]
      #           enabled: true
      #           ip_subnet: 10.4.11.0/24
      #     ansible_db_zone:
      #       vrf_vni: 31
      #       svis:
      #         420:
      #           name: ansible_demo_db_1
      #           tags: [ db ]
      #           enabled: true
      #           ip_subnet: 10.4.20.0/24
      #         421:
      #           name: ansible_demo_db_2
      #           tags: [ db ]
      #           enabled: true
      #           ip_subnet: 10.4.21.0/24'''
    return yaml