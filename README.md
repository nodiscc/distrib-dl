# distrib-dl

Download and keep up-to-date Linux/BSD distribution ISO images (installers/live images). Can be used to maintain a local ISO image repository.

Downloads will be verified against checksums and GPG keys when available. Checksums/signatures are downloaded as part of the process, they are recorded in the repository for archival/reference purposes.

[![pipeline status](https://gitlab.com/nodiscc/distrib-dl/badges/master/pipeline.svg)](https://gitlab.com/nodiscc/distrib-dl/commits/master)

## Installation

`git clone https://github.com/nodiscc/distrib-dl`

## Requirements

 * bash
 * wget
 * gnupg

## Usage

```
./distrib-dl DISTRIBUTION1 [DISTRIBUTION2 DISTRIBUTION3 ...]
Available distributions: debian centos tails kali proxmox pfsense freebsd
```

* [Debian GNU/Linux](https://www.debian.org/)
* [CentOS](https://www.centos.org/)
* [Tails](https://tails.boum.org/)
* [Kali](https://www.kali.org/)
* [Proxmox VE](https://pve.proxmox.com/wiki/Main_Page)
* [pfSense](https://www.pfsense.org/download/)
* [FreeBSD](https://www.freebsd.org/)
* [Android x86](https://www.android-x86.org/)


## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

 * Patches and pull requests welcome.
 * File bugs or possible improvements at https://github.com/nodiscc/distrib-dl/issues
 * Run `shellcheck` against the script to check for errors/styling issues.

## TODO

* add support for bittorrent downloads (transmission-cli?)
* add a --check mode: just ensure that wget commands return HTTP code 200
* automatically check for new versions of distributions (RSS feeds?)
* support other distros (arch/ubuntu/mint/zorin/alpine/fedora/dban/...)
* support downloading via bittorrent/transmission-cli
* centos: do not hardcode mirror, let centos.org take us to the closest download
* add support for Debian Live
* add support for [Arch Linux](https://www.archlinux.org/)
* add support for [GuixSD](https://www.gnu.org/software/guix/)
* add support for [NixOS Linux](https://nixos.org/)
* add support for [Fedora](https://getfedora.org/)
* add support for [Ubuntu](https://www.ubuntu.com/)
* add support for [OpenBSD](https://www.openbsd.org/)
* add support for [Lakka](https://www.lakka.tv/)
* add support for [Sparky Linux](https://sparkylinux.org/)
* add support for [Bedrock Linux](https://bedrocklinux.org/)
* add GPG/checksum verifications for proxmox
* add support for windows 10
* Integrate with https://github.com/thias/glim
* add support for debian netinstall to glim
* add support for tails and centos in main glim grub configuration
* add support for debian live including non-free firmware https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/

## License

[MIT](https://opensource.org/licenses/MIT)