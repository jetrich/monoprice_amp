# monoprice_amplifier
Simple python API to connect to Monoprice/Dayton multizone amplifiers through the RS232 interface. For the RS232 interface use the MonopriceAmplifier class.

Note that the RS232 interface is only tested with the Monoprice 10761. 

For more information see the official documentation at https://downloads.monoprice.com/files/manuals/10761_Manual_141028.pdf 

Usage:
```
receiver = MonopriceAmplifier(serial_port)  # e.g. /dev/ttyUSB0

receiver.main_volume('+')  #  will increase volume with 1 and return new value
receiver.main_volume('-')  #  will decrease volume with 1 and return new value
receiver.main_volume('=', '-40')  # specify dB, will return new value
print(receiver.main_volume('?'))  # will return current value

Monoprice = Monoprice(host_ip)  # The IP address of your amplifier in the network.

Monoprice.power_on()
Monoprice.available_sources()  # Returns a list of available sources in human readable format.
Monoprice.status()  # Returns a dictionary with keys 'volume', 'power', 'muted' and 'source'.
Monoprice.set_volume(150)  # Set volume level. min = 0 = 0dB, max = 50 = +50dB.
sources = Monoprice.available_sources()
Monoprice.select_source('1')
Monoprice.mute()
Monoprice.unmute()
Monoprice.power_off()
```

supported commands with supported operators for the RS232 interface

* main_volume [ +, -, =, ? ]
* main_mute [ +, -, =, ? ]
* main_power [ +, -, =, ? ]
* main_listeningmode [ +, - ]
* main_version [ ? ]
* main_dimmer [ +, -, =, ? ]
* main_source [ +, -, =, ? ]
