# Q2: Configure Host-based NAT

## Overview

This project updates the original network topology to implement host-based NAT. A new host (H9) is added as a NAT gateway to provide external connectivity for internal hosts h1 and h2. H9 is configured with a public IP (172.16.10.10) and performs NAT for internal IP addresses 10.1.1.2 (h1) and 10.1.1.3 (h2).

## Topology Changes

- **New Host Addition:**  
  - **H9** is added to switch **S1** with a 5 ms host-to-switch link latency.

- **Link Reassignment:**  
  - The links that previously connected **h1** and **h2** to **S1** are now moved to **H9** (links h1–H9 and h2–H9, each with a 5 ms delay).

- **NAT Implementation on H9:**  
  - H9 is configured with a public IP of **172.16.10.10**.
  - NAT functionality is implemented on H9:
    - **Source NAT (SNAT):** Translates outbound traffic from the internal network (10.1.1.0/24) to the public IP.
    - **Destination NAT (DNAT):** Translates incoming traffic destined for the public IP (172.16.10.10) to the appropriate internal host (10.1.1.2 for h1 and 10.1.1.3 for h2).

## Implementation Details

### Topology Update and NAT Setup

- The updated topology is built using Mininet and a Python script (`q2_net.py`):
  - **H9** is added and linked to **S1** with a 5 ms delay.
  - **h1** and **h2** are reattached to **H9** instead of directly connecting to **S1**.
  
- **NAT Configuration on H9:**  
  - **SNAT Rule:**

  - **DNAT Rules:**
   

### Program Execution

- Run the topology with:
  ```bash
  sudo python3 q2_net.py
