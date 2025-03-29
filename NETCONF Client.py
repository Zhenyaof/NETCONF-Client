from ncclient import manager
import xml.dom.minidom

def connect_netconf(host, port, username, password):
    """Establish a NETCONF session with the device."""
    print(f"Connecting to {host} on port {port}...")
    return manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'default'},
        allow_agent=False,
        look_for_keys=False
    )

def get_running_config(host, port, username, password, filter_xml=None):
    """Retrieve the current running configuration, optionally filtered."""
    with connect_netconf(host, port, username, password) as m:
        print("Fetching running configuration...")
        if filter_xml:
            config = m.get_config(source='running', filter=('subtree', filter_xml)).data_xml
        else:
            config = m.get_config(source='running').data_xml
        return xml.dom.minidom.parseString(config).toprettyxml()

def edit_config(host, port, username, password, config_data):
    """Apply configuration changes to the device."""
    with connect_netconf(host, port, username, password) as m:
        print("Applying configuration changes...")
        m.edit_config(target='running', config=config_data)
        print("Configuration updated successfully.")

def get_capabilities(host, port, username, password):
    """Retrieve and display the device's NETCONF capabilities."""
    with connect_netconf(host, port, username, password) as m:
        print("Fetching device capabilities...")
        return list(m.server_capabilities)

def validate_config(host, port, username, password):
    """Validate the device configuration before committing changes."""
    with connect_netconf(host, port, username, password) as m:
        print("Validating current configuration...")
        result = m.validate(source='running')
        print("Configuration validation result:")
        print(result)

def save_config(host, port, username, password):
    """Commit the configuration changes to save them permanently."""
    with connect_netconf(host, port, username, password) as m:
        print("Saving configuration...")
        m.commit()
        print("Configuration saved successfully.")

if __name__ == "__main__":
    host = "192.168.1.1"
    port = 830
    username = "admin"
    password = "password"
    
    print("Starting NETCONF client...")
    
    # Get running config with optional filter
    filter_xml = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    config = get_running_config(host, port, username, password, filter_xml)
    print("Running Configuration:")
    print(config)
    
    # Get NETCONF server capabilities
    capabilities = get_capabilities(host, port, username, password)
    print("\nServer Capabilities:")
    for cap in capabilities:
        print(cap)
    
    # Validate current configuration
    validate_config(host, port, username, password)
    
    # Edit configuration example (ensure valid XML for your device)
    config_data = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet0/1</name>
                <description>Configured via NETCONF</description>
            </interface>
        </interfaces>
    </config>
    """
    edit_config(host, port, username, password, config_data)
    
    # Save configuration
    save_config(host, port, username, password)
    
    print("NETCONF operations completed successfully.")
