ssidgen
=======

An SSID list generator for decloaking hidden Wireless networks.

Usage
=====

If you want to decloak a hidden network in a company use the `-c` option. The following command will generate a list of probable SSIDs for the target network into the file `ssid.txt`.

    ./ssidgen.py -c google

If you want to decloak someone's hidden network, the `-f` option is mandatory to specify the ISP hardware and the `-l` can be used to specify the usual suffix length (e.g. Livebox-75C5). Default suffix lenght is 4.

    ./ssidgen.py -f livebox


### Bruteforce with MDK3

To decloack a wireless network, you must use the adequate dictionnary and an appropriate tool like `mdk3`. The following line describes how to generate the dictionnary and launch the attack for a Livebox :

    # ./ssidgen.py -f livebox; mdk3 wlan0 p -f ssid.txt -c <channel>
