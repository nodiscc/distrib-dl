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
Available distributions: debian debian-live tails kali proxmox pfsense freebsd debian-live-config fedora ubuntu
Options:
-c        only check that the url returns 200, don't download anything
-d DIR    specify base download directory (by default the current working directory is used)
-h        show help
```

* [Debian GNU/Linux](https://www.debian.org/) (_[netinstall](https://www.debian.org/distrib/netinst)_ and _[live](https://www.debian.org/CD/live/)_)
* [Tails](https://tails.boum.org/)
* [Kali](https://www.kali.org/)
* [Proxmox VE](https://pve.proxmox.com/wiki/Main_Page)
* [pfSense](https://www.pfsense.org/download/)
* [FreeBSD](https://www.freebsd.org/)
* [debian-live-config](https://debian-live-config.readthedocs.io/)
* [Fedora Workstation](https://getfedora.org/en/workstation/)
* [Ubuntu](https://ubuntu.com/)
* [Arch Linux](https://archlinux.org/)

Downloads will be verified against checksums and GPG keys when available. Checksums/signatures are downloaded as part of the process. The script will return warnings unless you manually import and trust gpg keys:

```
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
```

**Debian:** You need to [import Debian signing keys to your GPG keyring](https://keyring.debian.org/):

```bash
gpg --keyserver keyring.debian.org --recv-keys DF9B9C49EAA9298432589D76DA87E80D6294BE9B
```

Consider a periodic cleanup of old/obsolete images from your download directory, else disk usage will keep increasing over time (unless you intend to keep old distribution releases?).


## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

 * Patches and pull requests welcome.
 * File bugs or possible improvements at https://gitlab.com/nodiscc/distrib-dl/issues
 * Run `shellcheck` against the script to check for errors/styling issues.

## TODO

* add GPG/checksum verifications for proxmox
* add support for [Bedrock Linux](https://bedrocklinux.org/)
* add support for [Clonezilla](https://en.wikipedia.org/wiki/Clonezilla)
* add support for [GNU Guix System](https://en.wikipedia.org/wiki/GNU_Guix_System)
* add support for [Lakka](https://www.lakka.tv/)
* add support for [NixOS](https://en.wikipedia.org/wiki/NixOS)
* add support for [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD)
* add support for [Rocky Linux](https://en.wikipedia.org/wiki/Rocky_Linux)
* add support for [AlmaLinux](https://en.wikipedia.org/wiki/AlmaLinux)
* add support for [Sparky Linux](https://en.wikipedia.org/wiki/SparkyLinux)
* add support for slackware
* add support for opensuse
* add support for void linux
* add support for nixos
* add support for bittorrent downloads (transmission-cli?)
* add support for windows 10
* automatically check for new versions of distributions (RSS feeds?)
* integrate with https://github.com/ventoy/Ventoy/
* support downloading via bittorrent/transmission-cli

## License

[MIT](https://opensource.org/licenses/MIT)

## Mirrors

- https://stdout.root.sx/gitea/nodiscc/distrib-dl
- https://gitlab.com/nodiscc/distrib-dl
