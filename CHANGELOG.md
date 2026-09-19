<!-- THIS FILE IS UPDATED AUTOMATICALLY, ANY CHANGES WILL BE OVERRIDDEN -->
# Changelog
All notable changes to Proxmox Pi OS will be documented in this file.

## [unreleased]
### Documentation

- Add credits section to README.md with references to CustoPiZer and installation guide

## [0.0.3](https://github.com/meteyou/proxmox-pi-os/releases/tag/0.0.3) - 2026-09-19
### Features

- **rpi-imager**: Add icon for the Imager OS list

### Bug Fixes and Improvements

- **ci**: Grant contents write permission to reusable build workflow

### Documentation

- Add README.md with rpi imager guide

## [0.0.2](https://github.com/meteyou/proxmox-pi-os/releases/tag/0.0.2) - 2026-09-19
### Features

- **ci**: Add release workflow with combined rpi-imager.json
- **rpi-imager**: Add manifest json to build workflow for artifacts and build script
- Init upload

### Bug Fixes and Improvements

- **ci**: Use redirect target filename for image download
- **network**: Fix network start
- **rpi**: Use https image download instead of torrent

### Refactor

- **ci**: Extract image build into reusable workflow

### Other

- **changelog**: Add git-cliff configs for release notes and CHANGELOG.md


