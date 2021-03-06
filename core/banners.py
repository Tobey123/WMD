#!/usr/bin/env python3
#
# MIT - (c) 2016 ThomasTJ (TTJ)
#


import configparser
from core.colors import bc as bc
import random
import os


config = configparser.ConfigParser()
config.read('core/config.ini')
fwNAME = (config['FRAMEWORK']['NAME'])
fwVERSION = (config['FRAMEWORK']['VERSION'])
fwDATE = (config['FRAMEWORK']['DATE'])
fwAUTHOR = (config['FRAMEWORK']['AUTHOR'])


banner1 = """


                                     ,»¡>═.
                                   j╬╗Ñ║Ñ░D╥░
                                    ╫░`░╙╨║▀H
                                   ▐▌╬Ñ╠Ü╠╩▓▄
                                   ╚▌▀▀▀║▓▀▀▀
                                   .▓▓▓▓▓▓▓▓╦.
                               .≈..»▓▓╫▓▓╫▓▓▒░,,»«
                          «^,,╦╬╬╬╬▓▓██▓▓██▓▓▓▓▒╬╫H..;;
                        ,Ñ¡:,"¡╙╙▀▀▀▀▓█████▓▀╣▀╫,;;»,,`╨¼
                        ╫░╔]µ╬╬╫Ö`,»╦╫╣███▌╬╦¡,;╟Ñ░░╦╥m░╦N.
                     r░╙╣╣╫▓▓▓▓╫Ñ╦╦µ╦╫▓██▓▓Ñ░╦╫╫╫▓▓▓▓▓╫#╨`,,«
                    ╫ÑÑw,,▐▓█████▓▓▓▓╫▓▓█▓▓╫╫▓▓▓▓▓██▓Ñµ╔╦U,`»]
                  ,Ñ╦░╟╫▓▓▓▓█``▀██████████████████▀ ▀▓▓▓▌Ñd╗▄▄╫
                  ▓╫N`╙╙█▀▀╙    ████████▓████████▓    ╙▀",»░╫╣╗⌐
                  ╫▓▓╫U~,      .▀█████████████▌▀╜▀   .,,╓╗╣▓▓▓Ö
                   ▀██▓▓▄µ╦½µ╦▄╦░╠▓██████████▄╫▄╣╦╦╦Ü▄▄▓▓███▀`
"""

banner2 = """


                              ~.
                            ▄╫jH.]░╗,╥▄▓▌▄,
                            ▓Ü░░╦╫▓█▓Ü─ └╙▀█
                           ╫╫K»]╫▓▓██▄▄▄~▄▄█▌
                           ▓▌╫N╬╫▌╦█░⌂.╔pµ╙▀█
                           ▓▓▓▓▓▓▓▓█╠╫3Φ▀Φ╫▀
                          ╟▓██████Ñ.▓▓▓▄▄▓▌
                          █▓███▓▌H  `▀▓███M
                          ▀▓▓░"╫Ñ╦╦;.`╙▀█▀Ñ».
                           ╦╫░!"░╫Ñ╦░░░╫╣╨░n╝╦╦⌂≈,
                           ▓▌Ñ░~:╫╫Ñ╦╦╦╫╫▓»─"!╦╫╫╬╫╖
                           ▓▓▓Ñ»,:╨╫Ñ╫▀╫╫╫╦,«╥╦╫▓█▓▓L
                           \▀█▌░»]░╨╫Ü╨╬╫▓▀▓▓▓▓██▓▀▓▌
                            '▀█╫╬▒═ÑφÅM░░╫╫╫▓███▌»░║╫,
                             └▓▌╫▄▒╗⌂░]╬▀▓█▓██▀▀▓╫#Å╫▓
                              ╘▀▄▌▒╫»╠▓▓▓▓▓╬▓▌  '▀▓▓▓▀H
                                ╨▀▓▄░¡╠µ╦╣▓▓▓    '▓█▀`╠
                                 ╫▀▀▀╨╩Ñ╦╫╫▓▓⌐    ╚░]⌐]▌
                                ▄███▓▓▓▓▓▓▓╫▒φ    j╬ÑH░▓
                               ▐██████▀▓▓▓▓▓▓╫     ╠╣Ñ░▓

"""

banner3 = """


                                           ,▄▓▓Ö╠▄╫Ñ╦╗╦,
                       .                  ╬▓▓╨╙╣▓▌▓▓▓████▄
                 j╦╦uuu¡╔µ▄╦╫╦           ╟▓▓N»»╨▓Å»»║▀████▓▄
               .╬╫▓██▄╬▓▓╫▌╦╣»∩          ▓█▒╦µµ;»»µµ░░╫▓██▓█
             .]Ñ▒▓████▓▓▌▓▌▄▓▄H         ,██▓▓█▓▒░╣▓▓▓▓▓╫▓███,
            ╔╦╫╣╫██▌     ▀▀▓            *██╠╠░µ╩╔╦░»░░░╫╫████
         .]╦╩╩╦╣██▀       `              ╟█╬Ñ░╟▄▄▒Ün]╦╬▓▓▓██▌
        ]╦Ü╦╫╫╫███                        ╙▀╫╦▄▄▄╦▄╦╦╫╫╫▓▓▄██⌐
      ,╦╫Ñ░╦╫╫▓███                         ╟╫╬╫╫╬╬Ñ╦╫╫╫▓▓▌▌
     ╔╫╫╫╬╬╫╫▓▓██▌                          ╙▓╫╫╬╬╬╬▓▓█▓▌▓▌
    ╔╫╫╫╫╫╫╫▓▓███▌]╦╦╦u¡╔,                   ▓████████▓▀╫▌░»
    ╣▓▓▓╫╣╣╣▓▌▀▒╦╬Ñ░░░░╨╫╫N  ~::"]]];:.      ║████████╫╫╫╫╫N╦░«.
   ╫╫╫▓▓▓▓╫╫▓Φ▀╨░╣▓▓╫╫╫╫╫╫Ñ╦╟╫╦╦░╦╦╦░░░╩╫««u»╢█████▓▌╬╫╫╫╫╫╫╨╨Uw░╓
   "╣▄╬╠╫╫╬╣╥╠╫╫╬╫▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫ÑÑ╦Ñ╦╦µ╦╦░]╫╫╩▒╦╦╫╩ÑÑ╩╫╫╫╫╫Ñ╦NN╦░░:~.
     ╙▀▓▓▓▓▓▓▓╬╫╨╨╠╣╣▀▀▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╬╫╫╫Ñ╬╫Ñ╨»»░╦╦╦╦╦╫Ñ░╫Ü░░╨░╨╨╦╦╫╬┐
        ╙▀▓▓▒╫╬╬╫╫╫╫╫╫╫╫▓▓▓███▓▓▓╫╫╫╫╫╫╫╫ÑÜ╫╩╨░]╦ÑÑÑ╨╠Ñ╦╫╫Ñ╫╫Ñ╦╦╦░░░╫╫╣▓▒
           ╙▀▓▓▓▓▓▓▓▓▓▓████████▓▓▓╫╫╫╫╫ÑÑ╬╫╫╫╫╫╫╬Ñ╦╦╬╣▓▓▓▓▓╫▓▓╫╫╫╫╫╫╫▓▓▓▓H
               `╙▀▀▓▓▓███████████▓╫╫╫╫╫N╬╫╫▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓╫╫N
                               ╙█▓▓╫╫╫╫╠▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▀╫╫Ñ╨╩╣╣╬Ü░╨╩╫╫φ
                                 █▓▓╫╫╬╫▓▓▓▓▓▓▓▓▓▓▓▓███▀▓██╫╫Ñ░]╦╥╦ÑÑÑ░░╫╫╫▄
                                 '██▓▓╣╣▀▓▓▓██████▓▀▒Ü░╨╠╫▓Å╫╫╦░Ñ╫╫Ü░╫╬╦╠╫╫╫▄
                                   ▓▌╫╫╫╫╫╫╫Ñ╩╫NÜ░╦░░╠╬╫▓▓▓▓▒╫╫╦╫╫▓╫╫▓▀╫Ñ╫╫╫▓⌐
                                   "▓▓▓▓╫╫╫Ü░░░░░░░░░╠╬╬╠╣╫███▓▓▓╫▓▀Ñ╬╣Ñ░╩╫╣▓▌
                                    ▓▓▓▓▓▓▓╫Ñ╦╦░╦╦╦╫╫╬╫╫╫▓▓███▓╫╫╫Ñ╨░░░╫╫╬╫╫▓▌

"""


def loadBanner():
    """Load a random banner."""
    os.system('clear')

    randomBanner = random.randint(1, 3)
    if randomBanner == 1:
        print(banner1)
    if randomBanner == 2:
        print(banner2)
    if randomBanner == 3:
        print(banner3)

    print('%-*s%s%-*s%s%s' % (30, '', bc.FAIL, 10, 'NAME:', bc.ENDC, fwNAME))
    print('%-*s%s%-*s%s%s' % (30, '', bc.FAIL, 10, 'VERSION:', bc.ENDC, fwVERSION))
    print('%-*s%s%-*s%s%s' % (30, '', bc.FAIL, 10, 'AUTHOR:', bc.ENDC, fwAUTHOR))
    print('\n\n')
