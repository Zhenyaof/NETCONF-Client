# NETCONF Client
 

## Overview
This project provides a Python-based NETCONF client using the `ncclient` library to manage network devices. The script enables users to retrieve, edit, validate, and commit configurations via NETCONF.

## Features
- Connect to a network device using NETCONF
- Retrieve the running configuration (optionally with a filter)
- Apply configuration changes
- Validate configuration before committing
- Save (commit) configuration changes
- Fetch device capabilities

## Prerequisites
Ensure you have Python 3 installed along with the `ncclient` library. You can install it using:

```sh
pip install ncclient
```

### Network Device Requirements
To use this script, your network device must:
- Support NETCONF
- Have NETCONF enabled on port 830 (default)
- Have an accessible username and password for authentication

You may need to configure NETCONF on your Cisco device using the following commands:

```sh
configure terminal
netconf-yang
end
write memory
```

## Usage

### 1. Clone the repository
```sh
git clone https://github.com/your-repo/netconf-client.git
cd netconf-client
```

### 2. Update the connection details
Open `netconf_client.py` and modify the following variables with your network device’s details:

```python
host = "192.168.1.1"  # Device IP address
port = 830  # NETCONF default port
username = "admin"  # Your username
password = "password"  # Your password
```

### 3. Run the script
```sh
python netconf_client.py
```

## Code Explanation

### 1. Establishing a Connection
```python
def connect_netconf(host, port, username, password):
```
- Establishes a secure NETCONF session with the specified device.
- Uses `manager.connect()` to handle authentication and connection.

### 2. Fetching Running Configuration
```python
def get_running_config(host, port, username, password, filter_xml=None):
```
- Retrieves the device's running configuration.
- Optionally applies a filter to limit the output.
- Uses the `get-config` NETCONF RPC operation.

### 3. Editing Configuration
```python
def edit_config(host, port, username, password, config_data):
```
- Applies new configuration changes using the NETCONF `edit-config` operation.
- Accepts configuration data in XML format.
- Sends the new configuration to the device.

### 4. Fetching Device Capabilities
```python
def get_capabilities(host, port, username, password):
```
- Lists all NETCONF capabilities supported by the device.
- Useful for understanding what features are available.

### 5. Validating Configuration
```python
def validate_config(host, port, username, password):
```
- Validates the device configuration before committing changes.
- Helps detect errors before applying modifications.

### 6. Saving Configuration
```python
def save_config(host, port, username, password):
```
- Commits configuration changes to make them persistent.
- Uses the `commit` RPC operation.

## Example Output
```
Starting NETCONF client...
Connecting to 192.168.1.1 on port 830...
Fetching running configuration...
Running Configuration:
<xml configuration output>
Fetching device capabilities...
Capability: urn:ietf:params:netconf:base:1.0
...
Validating current configuration...
Configuration validation result: OK
Applying configuration changes...
Configuration updated successfully.
Saving configuration...
Configuration saved successfully.
NETCONF operations completed successfully.
```

## Troubleshooting
### Common Issues & Fixes
- **Connection refused**: Ensure NETCONF is enabled on the device.
- **Authentication failed**: Verify username and password.
- **Timeout errors**: Check device accessibility and firewall settings.
- **Incorrect XML data**: Ensure your configuration data follows the correct YANG model.

