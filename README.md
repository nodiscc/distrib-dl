# distrib-dl

Download and keep up-to-date Linux/BSD distribution ISO images (installers/live images). Can be used to maintain a local ISO image repository.

[![pipeline status](https://gitlab.com/nodiscc/distrib-dl/badges/master/pipeline.svg)](https://gitlab.com/nodiscc/distrib-dl/commits/master)

## Installation

`git clone https://gitlab.com/nodiscc/distrib-dl`

## Requirements

`python3 wget gnupg`

## Usage

```bash
$ ./distrib-dl --help
usage: distrib-dl [-h] [-c] [-d DIR] [distributions ...]

Download and verify Linux distribution installers

positional arguments:
  distributions  Distributions to download (archlinux debian debian-live debian-live-config fedora freebsd kali proxmox tails ubuntu, or all)

options:
  -h, --help     show this help message and exit
  -c             Only check URL, don't download
  -d DIR         Specify base download directory
```

Downloads will be verified against checksums and GPG keys when available. Checksums/signatures are downloaded as part of the process. The script will return warnings unless you manually `trust` GPG keys:

```
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
```

Consider a periodic cleanup of old/obsolete images from your download directory, else disk usage will keep increasing over time (unless you intend to keep old distribution releases?).


## Configuration

Architectures and distribution versions are configurable in the script itself.

## Contributing/testing/support

* Patches and pull requests welcome
* File bugs or possible improvements at https://gitlab.com/nodiscc/distrib-dl/issues
* Run `make tests` to test your changes

## License

[MIT](https://opensource.org/licenses/MIT)

## Mirrors

* https://gitlab.com/nodiscc/distrib-dl
* https://github.com/nodiscc/distrib-dl
