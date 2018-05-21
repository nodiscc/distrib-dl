# distrib-dl

Download and verify Linux distribution ISO images/installers.  
Downloads will be verified against checksums and GPG keys.
Useful to maintain a local ISO image repository.  

## Installation

`git clone https://github.com/nodiscc/distrib-dl`

## Requirements

 * bash
 * wget
 * gnupg

## Usage

`./distrib-dl DISTRIBUTION1 [DISTRIBUTION2 DISTRIBUTION3 ...]`

Currently supports `debian`, `centos`, `tails`, `kali`.

## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

 * Patches and pull requests welcome.
 * File bugs or possible improvements at https://github.com/nodiscc/distrib-dl/issues
 * Run `shellcheck` against the script to check for errors/styling issues.

## TODO

* add support for bittorrent downloads (transmission-cli?)
* automatically check for new versions of distributions (RSS feeds?)
* support other distros (arch/ubuntu/mint/zorin/alpine/android-x86/fedora/dban/gentoo...)
* support downloading via bittorrent/transmission-cli
* centos: do not hardcode mirror, let centos.org take us to the closest download
* add support for android-x86
* add support for Debian Live
* add support for archlinux
* add support for fedora
* add support for ubuntu
* add support for freebsd
* add support for openbsd
* add support for proxmox VE
* add support for pfsense
* add support for windows 10
* Integrate with https://github.com/thias/glim
* add support for debian netinstall to glim
* add support for tails and centos in main glim grub configuration


## License

[MIT](https://opensource.org/licenses/MIT)