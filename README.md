# ESP32-S3 e-Paper 3.97 — English firmware

English-language build of the official Waveshare firmware for the
**ESP32-S3-e-Paper-3.97** board.

This is the complete Waveshare application, not a XiaoZhi-only firmware. It
keeps the original clock, alarm, weather, network, audio, settings, reader and
other board functions. User-facing strings were translated to English. Chinese
tokens required by the weather provider and lunar-calendar parser remain
internally unchanged so those integrations continue to work.

## Ready-to-flash image

`firmware/ESP32-S3-ePaper-3.97-English.bin`

- Flash offset: `0x0`
- Flash size: 16 MB
- SHA-256: `014762DBEC768D9AE442D7028337D852F36AC0C78A5659B499F4CF1735CD6A3A`

Example with esptool:

```shell
esptool --chip esp32s3 --port COM6 --baud 460800 write-flash 0x0 firmware/ESP32-S3-ePaper-3.97-English.bin
```

Replace `COM6` with the serial port used by your board.

## Building from source

Requirements:

- ESP-IDF 5.4.1
- Target: ESP32-S3

```shell
cd source
idf.py set-target esp32s3
idf.py build
```

The managed-component versions are pinned in `source/dependencies.lock`.

## Repository layout

- `source/` — translated ESP-IDF project based on Waveshare's official source
- `firmware/` — merged 16 MB image ready to flash at offset `0x0`
- `tools/` — translation helper and its translation cache

## Upstream

Based on the Waveshare project:
https://github.com/waveshareteam/ESP32-AIChats

