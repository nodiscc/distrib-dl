# distrib-dl

Download and keep up-to-date Linux/BSD distribution ISO images (installers/live images). Can be used to maintain a local ISO image repository.

[![pipeline status](https://gitlab.com/nodiscc/distrib-dl/badges/master/pipeline.svg)](https://gitlab.com/nodiscc/distrib-dl/commits/master)

## Installation

`git clone https://gitlab.com/nodiscc/distrib-dl`

## Requirements

 * bash
 * wget
 * gnupg

## Usage

```
Usage: ./distrib-dl [OPTIONS] DISTRIBUTION1 [DISTRIBUTION2 DISTRIBUTION3 ...] [all]
Available distributions: debian centos tails kali proxmox pfsense freebsd androidx86 debian-live-config fedora
Options:
-c        only check that the url returns 200, don't download anything
-h        show help
```

* [Debian GNU/Linux](https://www.debian.org/) (_[netinstall](https://www.debian.org/distrib/netinst)_ and _[live](https://www.debian.org/CD/live/)_)
* [CentOS](https://www.centos.org/)
* [Tails](https://tails.boum.org/)
* [Kali](https://www.kali.org/)
* [Proxmox VE](https://pve.proxmox.com/wiki/Main_Page)
* [pfSense](https://www.pfsense.org/download/)
* [FreeBSD](https://www.freebsd.org/)
* [Android x86](https://www.android-x86.org/)
* [debian-live-config](https://debian-live-config.readthedocs.io/)
* [Fedora Workstation](https://getfedora.org/en/workstation/)

Downloads will be verified against checksums and GPG keys when available. Checksums/signatures are downloaded as part of the process, they are recorded in the repository for archival/reference purposes. The script will return warnings unless you manually import and trust gpg keys:

```
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
```

## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

 * Patches and pull requests welcome.
 * File bugs or possible improvements at https://gitlab.com/nodiscc/distrib-dl/issues
 * Run `shellcheck` against the script to check for errors/styling issues.

## TODO

* add support for bittorrent downloads (transmission-cli?)
* automatically check for new versions of distributions (RSS feeds?)
* support downloading via bittorrent/transmission-cli
* centos: do not hardcode mirror, let centos.org take us to the closest download
* add support for [Arch Linux](https://www.archlinux.org/)
* add support for [GuixSD](https://www.gnu.org/software/guix/)
* add support for [NixOS Linux](https://nixos.org/)
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

## Mirrors

- https://stdout.root.sx/gitea/nodiscc/distrib-dl
- https://gitlab.com/nodiscc/distrib-dl
