import pyOCD
import usb


def get_hids():
    devs = usb.core.find(find_all=True)
    hids = []
    for dev in devs:
        conf = dev.get_active_configuration()
        for interf in conf:
            if usb.CLASS_HID == interf.bInterfaceNumber:
                hids.append(dev)
    return hids


def deactivate_driver(dev):
    config = dev.get_active_configuration()
    for interface in config:
        if interface.bInterfaceClass == 0x03:
             if dev.is_kernel_driver_active(interface.bInterfaceNumber):
                 dev.detach_kernel_driver(interface.bInterfaceNumber)
                 break


def get_hid_interface(dev):
    for interface in dev.get_active_configuration():
        if interface.bInterfaceClass == 0x03:
            return interface
    return None


# This is the so called <interface> passsed around in PyOCD
def make_pyusb_backend():
    interf = pyOCD.interface.pyusb_backend.PyUSB()
    ep_in, ep_out = None, None
    deactivate_driver(hid)
    for ep in get_hid_interface(hid):
        print(ep)
        if ep.bEndpointAddress & 0x80:
            ep_in = ep
        else:
            ep_out = ep
    interf.dev = hid
    interf.ep_in = ep_in
    interf.ep_out = ep_out
    interf.start_rx()
    return interf


interface = make_pyusb_backend(get_hids()[0])

# Create PyUSB instance






# Test communication
