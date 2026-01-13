#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import hashlib
import requests

# Configuration
config = {
    "debian_architecture": "amd64",
    "debian_version": "13.3.0",
    "debian_live_architecture": "amd64",
    "debian_live_desktop_environment": "xfce",
    "tails_architecture": "amd64",
    "tails_version": "7.1",
    "kali_architecture": "amd64",
    "kali_version": "2025.4",
    "kali_flavour": "installer",
    "proxmox_version": "8.4-1",
    "pfsense_version": "2.7.2",
    "pfsense_installer_type": "vga",
    "freebsd_version": "13.2",
    "debian_live_config_version": "4.2.0",
    "fedora_version_major": "41",
    "fedora_version_minor": "1.4",
    "ubuntu_architecture": "amd64",
    "ubuntu_version": "22.04.5",
    "archlinux_version": "2026.01.01"
}

# Global options
verify = True
download_dir = os.getcwd()
wget_opts = "--no-verbose"

def run_cmd(cmd):
    """Run shell command and handle errors."""
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
        )
    for line in iter(process.stdout.readline, ''):
        print(line.rstrip())
    process.stdout.close()
    return_code = process.wait()
    if return_code != 0:
        raise subprocess.CalledProcessError(return_code, cmd)

def download_file(url, dest_dir, filename):
    """Download a file using wget."""
    cmd = f"wget {wget_opts} --timestamping --show-progress --directory-prefix='{dest_dir}/' '{url}'"
    run_cmd(cmd)

def download_and_verify(dir, base_url, iso, sums, sig, key, verify_flag):
    """Generic download and verification function."""
    os.makedirs(dir, exist_ok=True)
    download_file(f"{base_url}/{sums}", dir, sums)
    if sig:
        download_file(f"{base_url}/{sig}", dir, sig)
    if key:
        download_file(key, dir, os.path.basename(key))

    if verify_flag and sig:
        verify_signature(dir, sig, sums, key)

    download_file(f"{base_url}/{iso}", dir, iso)

    if verify_flag:
        print(f"[distrib-dl] Verifying ISO integrity...")
        algo = "sha" + sums.split("SUMS")[0].replace("SHA", "")
        cmd = f"(cd '{dir}' && {algo}sum --check --ignore-missing <(cat '{sums}'))"
        run_cmd(cmd)

def verify_signature(dir, sig_file, sums_file, key_file):
    """Verify GPG signature."""
    cmd = f"gpg --import '{dir}/{key_file}'" if key_file else ""
    run_cmd(cmd)
    cmd = f"gpg --keyid-format 0xlong --verify '{dir}/{sig_file}' '{dir}/{sums_file}'"
    run_cmd(cmd)

def download_debian():
    dir = os.path.join(download_dir, "debian")
    base_url = f"https://cdimage.debian.org/debian-cd/current/{config['debian_architecture']}/iso-cd/"
    iso = f"debian-{config['debian_version']}-{config['debian_architecture']}-netinst.iso"
    sums = "SHA512SUMS"
    sig = "SHA512SUMS.sign"
    download_and_verify(dir, base_url, iso, sums, sig, "", verify)

def download_debian_live():
    dir = os.path.join(download_dir, "debian-live")
    base_url = f"https://cdimage.debian.org/cdimage/release/current-live/{config['debian_live_architecture']}/iso-hybrid/"
    iso = f"debian-live-{config['debian_version']}-{config['debian_live_architecture']}-{config['debian_live_desktop_environment']}.iso"
    sums = "SHA512SUMS"
    sig = "SHA512SUMS.sign"
    download_and_verify(dir, base_url, iso, sums, sig, "", verify)

def download_tails():
    dir = os.path.join(download_dir, "tails")
    os.makedirs(dir, exist_ok=True)
    iso_url = f"https://mirrors.wikimedia.org/tails/stable/tails-{config['tails_architecture']}-{config['tails_version']}/tails-{config['tails_architecture']}-{config['tails_version']}.iso"
    key_url = "https://tails.boum.org/tails-signing.key"
    sig_url = f"https://tails.boum.org/torrents/files/tails-{config['tails_architecture']}-{config['tails_version']}.iso.sig"
    
    download_file(key_url, dir, "tails-signing.key")
    download_file(sig_url, dir, "tails-signing.sig")
    
    if verify:
        run_cmd(f"gpg --import '{dir}/tails-signing.key'")
    
    download_file(iso_url, dir, "tails.iso")
    
    if verify:
        run_cmd(f"gpg --keyid-format 0xlong --verify '{dir}/tails-signing.sig' '{dir}/tails.iso'")

def download_kali():
    dir = os.path.join(download_dir, "kali")
    base_url = f"https://cdimage.kali.org/kali-{config['kali_version']}/"
    iso = f"kali-linux-{config['kali_version']}-{config['kali_flavour']}-{config['kali_architecture']}.iso"
    sums = "SHA256SUMS"
    sig = "SHA256SUMS.gpg"
    key = "https://archive.kali.org/archive-key.asc"
    download_and_verify(dir, base_url, iso, sums, sig, key, verify)

def download_proxmox():
    dir = os.path.join(download_dir, "proxmox")
    base_url = "https://enterprise.proxmox.com/iso"
    iso = f"proxmox-ve_{config['proxmox_version']}.iso"
    download_and_verify(dir, base_url, iso, "", "", "", False)

def download_pfsense():
    dir = os.path.join(download_dir, "pfsense")
    os.makedirs(dir, exist_ok=True)
    
    if config["pfsense_installer_type"] == "serial":
        pfsense_is_serial = "serial-"
    elif config["pfsense_installer_type"] == "vga":
        pfsense_is_serial = ""
    else:
        print(f"[distrib-dl] ERROR: invalid installer type for pfsense: {config['pfsense_installer_type']}")
        sys.exit(1)
    
    pfsense_iso_filename = f"pfSense-CE-memstick-{pfsense_is_serial}{config['pfsense_version']}-RELEASE-amd64.img.gz"
    pfsense_hashes_url = f"https://www.pfsense.org/hashes/{pfsense_iso_filename}.sha256"
    pfsense_base_url = "https://frafiles.pfsense.org/mirror/downloads"
    
    download_file(pfsense_hashes_url, dir, f"{pfsense_iso_filename}.sha256")
    download_file(f"{pfsense_base_url}/{pfsense_iso_filename}", dir, pfsense_iso_filename)
    
    if verify:
        cmd = f"(cd '{dir}' && sha256sum --check '{pfsense_iso_filename}.sha256')"
        run_cmd(cmd)

def download_freebsd():
    dir = os.path.join(download_dir, "freebsd")
    os.makedirs(dir, exist_ok=True)
    
    base_url = f"https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/{config['freebsd_version']}"
    iso_filename = f"FreeBSD-{config['freebsd_version']}-RELEASE-amd64-memstick.img"
    sums_filename = f"CHECKSUM.SHA512-FreeBSD-{config['freebsd_version']}-RELEASE-amd64"
    keyring_url = "https://docs.freebsd.org/pgpkeys/pgpkeys.txt"
    
    download_file(keyring_url, dir, "pgpkeys.txt")
    download_file(f"{base_url}/{sums_filename}", dir, sums_filename)
    download_file(f"{base_url}/{iso_filename}", dir, iso_filename)
    
    if verify:
        cmd = f"(cd '{dir}' && sha512sum --ignore-missing -c <(cat '{sums_filename}'))"
        run_cmd(cmd)

def download_debian_live_config():
    dir = os.path.join(download_dir, "debian-live-config")
    base_url = f"https://github.com/nodiscc/debian-live-config/releases/download/{config['debian_live_config_version']}/"
    iso = f"debian-live-config-{config['debian_live_config_version']}-debian-bookworm-amd64.iso"
    sums = "SHA512SUMS"
    sig = "SHA512SUMS.sign"
    key = f"{base_url}debian-live-config-release.key"
    download_and_verify(dir, base_url, iso, sums, sig, key, verify)

def download_fedora():
    dir = os.path.join(download_dir, "fedora")
    base_url = f"https://download.fedoraproject.org/pub/fedora/linux/releases/{config['fedora_version_major']}/Workstation/x86_64/iso"
    iso = f"Fedora-Workstation-Live-x86_64-{config['fedora_version_major']}-{config['fedora_version_minor']}.iso"
    sums = f"Fedora-Workstation-{config['fedora_version_major']}-{config['fedora_version_minor']}-x86_64-CHECKSUM"
    key = "https://fedoraproject.org/fedora.gpg"
    download_and_verify(dir, base_url, iso, sums, "", key, verify)

def download_ubuntu():
    dir = os.path.join(download_dir, "ubuntu")
    base_url = f"https://releases.ubuntu.com/{config['ubuntu_version']}"
    iso = f"ubuntu-{config['ubuntu_version']}-desktop-{config['ubuntu_architecture']}.iso"
    sums = "SHA256SUMS"
    sig = "SHA256SUMS.gpg"
    download_and_verify(dir, base_url, iso, sums, sig, "", verify)
    
    if verify:
        print("[distrib-dl] Verifying Ubuntu signature...")
        run_cmd("gpg --keyid-format long --keyserver hkp://keyserver.ubuntu.com --recv-keys 0x843938DF228D22F7B3742BC0D94AA3F0EFE21092")
        run_cmd(f"gpg --keyid-format long --verify '{dir}/SHA256SUMS.gpg' '{dir}/SHA256SUMS'")

def download_archlinux():
    dir = os.path.join(download_dir, "archlinux")
    os.makedirs(dir, exist_ok=True)
    
    base_url = f"https://geo.mirror.pkgbuild.com/iso/{config['archlinux_version']}/"
    iso_filename = "archlinux-x86_64.iso"
    sums_url = f"https://archlinux.org/iso/{config['archlinux_version']}/sha256sums.txt"
    sig_url = f"https://geo.mirror.pkgbuild.com/iso/{config['archlinux_version']}/archlinux-x86_64.iso.sig"
    
    download_file(sums_url, dir, "sha256sums.txt")
    download_file(sig_url, dir, "archlinux-x86_64.iso.sig")
    download_file(f"{base_url}/{iso_filename}", dir, iso_filename)
    
    if verify:
        run_cmd("gpg --auto-key-locate clear,wkd -v --locate-external-key pierre@archlinux.org")
        run_cmd(f"gpg --verify '{dir}/archlinux-x86_64.iso.sig' '{dir}/archlinux-x86_64.iso'")
        cmd = f"(cd '{dir}' && sha256sum --check --ignore-missing <(cat sha256sums.txt))"
        run_cmd(cmd)

def main():
    parser = argparse.ArgumentParser(description="Download and verify Linux distribution installers")
    parser.add_argument("-c", action="store_true", help="Only check URL, don't download")
    parser.add_argument("-d", dest="dir", help="Specify base download directory")
    parser.add_argument("distributions", nargs="*", help="Distributions to download (archlinux debian debian-live debian-live-config fedora freebsd kali pfsense proxmox tails ubuntu, or all")

    args = parser.parse_args()

    global verify, download_dir, wget_opts
    if args.c:
        wget_opts = "--spider"
        verify = False
    if args.dir:
        download_dir = args.dir

    distributions = args.distributions

    if not distributions or "all" in distributions:
        functions = [
            download_debian, download_debian_live, download_tails, download_kali,
            download_proxmox, download_pfsense, download_freebsd, download_debian_live_config,
            download_fedora, download_ubuntu, download_archlinux
        ]
        for func in functions:
            func()
    else:
        for dist in distributions:
            if dist == "debian":
                download_debian()
            elif dist == "debian-live":
                download_debian_live()
            elif dist == "tails":
                download_tails()
            elif dist == "kali":
                download_kali()
            elif dist == "proxmox":
                download_proxmox()
            elif dist == "pfsense":
                download_pfsense()
            elif dist == "freebsd":
                download_freebsd()
            elif dist == "debian-live-config":
                download_debian_live_config()
            elif dist == "fedora":
                download_fedora()
            elif dist == "ubuntu":
                download_ubuntu()
            elif dist == "archlinux":
                download_archlinux()
            elif dist == "all":
                # Already handled above
                pass
            else:
                print(f"[distrib-dl] ERROR: Invalid distribution '{dist}'")
                sys.exit(1)

if __name__ == "__main__":
    main()
