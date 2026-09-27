# Troubleshooting Guide — Enterprise Security Lab

---

## VM Cannot Reach Other Lab VMs

**Symptom:** `ping 192.168.56.20` from Kali times out.

**Checks:**
1. Confirm the VM uses **Host-Only** adapter, not NAT-only or Bridged
2. Verify the adapter is `vboxnet0` and not another Host-Only network
3. Check the static IP is correctly set:
   ```bash
   ip a show eth1      # Should show 192.168.56.10/24
   ip route            # Should show 192.168.56.0/24 via eth1
   ```
4. Ensure target VM is powered on and not suspended

---

## Kali Cannot Reach Internet for Updates

**Symptom:** `apt update` fails or `curl https://google.com` times out.

**Checks:**
1. Kali must have a **NAT adapter** as the second adapter
2. In VirtualBox: Machine → Settings → Network → Adapter 2 → NAT
3. Run: `ip route | grep default` — should show a default via NAT interface (eth0)
4. Test: `ping 8.8.8.8` — should succeed from Kali

---

## Target VM Reaches Internet (Isolation Failure)

**Critical:** A target VM should **never** reach the internet.

**Fix immediately if this happens:**
1. Power off the VM
2. Go to VM Settings → Network
3. Remove any NAT or Bridged adapter
4. Restore to Host-Only adapter only
5. Boot VM and verify: `ping 8.8.8.8` → must fail

---

## Wazuh Agent Not Connecting

**Symptom:** VM doesn't appear in Wazuh Dashboard.

**Checks:**
1. Wazuh Manager is running: `sudo systemctl status wazuh-manager` on SIEM VM
2. Agent is running on target: `sudo systemctl status wazuh-agent`
3. Agent configured with correct SIEM IP:
   ```bash
   cat /var/ossec/etc/ossec.conf | grep -A5 "<server>"
   # Should show 192.168.56.50
   ```
4. Firewall ports open on SIEM: `ufw allow 1514/udp && ufw allow 1515/tcp`
5. Re-enroll agent if keys mismatch:
   ```bash
   sudo /var/ossec/bin/agent-auth -m 192.168.56.50
   sudo systemctl restart wazuh-agent
   ```

---

## DVWA / Juice Shop Not Loading

**Symptom:** Browser on Kali can't reach `http://192.168.56.40:8080`

**Checks:**
1. Web Lab VM is powered on
2. Docker services are running:
   ```bash
   sudo docker ps    # Should list dvwa, juice-shop, webgoat containers
   ```
3. Start containers if stopped:
   ```bash
   cd /opt/web-lab && sudo docker compose up -d
   ```
4. Check Web Lab IP:
   ```bash
   ip a show eth0    # Should show 192.168.56.40/24
   ```

---

## Nmap Scan Shows All Ports Filtered

**Symptom:** Nmap returns only filtered ports on a target.

**Likely cause:** Windows Firewall or UFW blocking scans.

**For lab exercises:** You may temporarily disable the firewall on the target to confirm services are running, then re-enable.

```bash
# Linux Server: Check UFW
sudo ufw status

# Windows Endpoint: Check Firewall (from RDP session)
netsh advfirewall show allprofiles
```

**Recommended:** Keep firewalls on and use them as a detection exercise instead.

---

## Wazuh Dashboard Not Loading (port 5601)

**Checks:**
1. SIEM VM powered on
2. Dashboard service running:
   ```bash
   sudo systemctl status wazuh-dashboard
   ```
3. OpenSearch running:
   ```bash
   sudo systemctl status wazuh-indexer
   ```
4. Access from host browser: `https://192.168.56.50:443` (HTTPS) or `http://192.168.56.50:5601`
5. Self-signed cert warning: Accept the browser warning for lab use

---

## VM Running Slowly / Out of RAM

**Recommendations:**
- Run a maximum of 3 VMs simultaneously with 16GB host RAM
- Suspend unused VMs instead of keeping them running
- Reduce VM RAM allocations temporarily: Kali 2GB minimum, targets 1.5GB minimum

---

[← Back to README](../README.md)
