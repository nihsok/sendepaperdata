from bluepy import btle

mac_address = ''
characteristic_uuid='6E400001-B5A3-F393-E0A9-E50E24DCCA9E'

peripheral = btle.Peripheral(mac_address)
service = peripheral.getServiceUUID(characteristic_uuid)
characteristic = service.getCharacteristics(characteristic_uuid)[0]

with open('tmp.buf','rb') as f:
  data=f.read()

characteristic.write(data)
peripheral.disconnect()
