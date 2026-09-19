# Proxmox Pi OS

A port of Raspberry Pi OS Lite (64-bit) with preinstalled Proxmox VE. Images are
built with [CustoPiZer](https://github.com/OctoPrint/CustoPiZer) via GitHub
Actions.

## Flashing with Raspberry Pi Imager

Raspberry Pi Imager offers an *OS customization* step (hostname, user, password,
SSH keys, locale) when it knows which customization format an image expects. For
images selected via **Use custom** this metadata is missing, so the
customization tab stays disabled.

### Recommended: via release repository

Every release publishes a `rpi-imager.json` manifest. Add it once to Raspberry
Pi Imager, and it will show the latest release including the customization step:

```
https://github.com/meteyou/proxmox-pi-os/releases/latest/download/rpi-imager.json
```

**App Options → Content Repository → EDIT → Use custom URL**, paste the URL and
click **Apply & Restart**. The image is downloaded from the release by Imager
itself.

## IMPORTANT INFO: Network

**Wi-Fi is not supported.** Proxmox needs a Linux bridge for VMs and containers,
which cannot sit on top of a Wi-Fi interface. The image therefore uses a static
ifupdown2 setup, NetworkManager (which Raspberry Pi OS uses for Wi-Fi) is
removed and cloud-init's network configuration is disabled on this image. Wi-Fi
settings entered in the Raspberry Pi Imager are silently ignored, all other
settings (hostname, user, password, SSH keys, locale) are applied. Connect the
Pi via Ethernet, ideally before the first boot. The bridge `vmbr0` on `eth0`
gets its address via DHCP, set a reservation in your router so the node keeps a
stable IP.

Proxmox refuses to start when the hostname resolves to `127.0.1.1`, therefore
`/etc/hosts` is kept in sync with the bridge IP (at boot and on every DHCP
lease). If the cable is plugged in after boot, the Proxmox services are started
automatically once the lease arrives.

## Credits

- Images are built with [CustoPiZer](https://github.com/OctoPrint/CustoPiZer)
  by OctoPrint.
- The build workflow follows the guide
  [Proxmox VE auf dem Raspberry Pi 5 installieren](https://schroederdennis.de/raspberry-pi/proxmox-ve-raspberry-pi-5-arm64-anleitung-installieren-tutorial/)
  by Dennis Schröder.
