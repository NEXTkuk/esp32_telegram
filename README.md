# EspTool

pip install esptool

# Стирание Flash памяти

python -m esptool --chip esp32 erase_flash

# Прошивка MicroPython на ESP32

python -m esptool --chip esp32 --port COM5 write_flash -z 0x1000 <esp32.bin путь>
