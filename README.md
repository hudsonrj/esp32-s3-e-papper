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
- SHA-256: `CDEF4DC5377C284B0B51D78FA78D43168ED5B90687D2B59E40B69C527E258995`

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

The Gregorian calendar works offline and opens immediately. Lunar data remains
optional and can be refreshed with a long press. Weather uses IP-based location
and Open-Meteo worldwide, without an API key.

The firmware creates the SD-card folders used by the built-in applications:

- `/music` for MP3/WAV audio and WAV recordings
- `/fiction` for UTF-8 TXT documents
- `/bookmarks` for reader progress and bookmarks

The reader does not support PDF directly; convert PDFs to UTF-8 TXT first.

## Repository layout

- `source/` — translated ESP-IDF project based on Waveshare's official source
- `firmware/` — merged 16 MB image ready to flash at offset `0x0`
- `tools/` — translation helper and its translation cache

## Upstream

Based on the Waveshare project:
https://github.com/waveshareteam/ESP32-AIChats
