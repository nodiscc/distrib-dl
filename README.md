# distrib-dl

Download and verify Linux distribution installers.  
Downloads will be verified against checksums and GPG keys.
Useful to maintain a local ISO image repository.  
Supports `debian`, `centos`, `tails`, `kali`.

## Installation

`git clone https://github.com/nodiscc/distrib-dl`

## Requirements

 * bash
 * wget
 * gnupg

## Usage

`./distrib-dl DISTRIBUTION1 [DISTRIBUTION2 DISTRIBUTION3 ...]`

## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

 * Patches and pull requests welcome.
 * File bugs or possible improvements at https://github.com/nodiscc/distrib-dl/issues
 * Run `shellcheck` against the script to check for errors/styling issues.

## TODO

* add support for bittorrent downloads (transmission-cli?)
* automatically check for new versions of distributions (RSS feeds?)
* add support for Proxmox VE
* support other distros (arch/ubuntu/mint/zorin/alpine/android-x86/fedora/dban/gentoo...)
* support downloading via bittorrent/transmission-cli
* centos: do not hardcode mirror, let centos.org take us to the closest download
* add support for windows 10
* add support for androidx86
* Integrate with https://github.com/thias/glim
* add support for debian netinstall to glim
* support Debian Live (multiple variants from main glim grub config)
* add support for tails and centos in main glim grub configuration

## License

[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)

_Template README built from https://github.com/lalo/readme-fads results_