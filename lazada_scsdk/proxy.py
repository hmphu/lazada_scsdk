# -*- coding: utf-8 -*-
# @Author: Phu Hoang
# @Date:   2017-05-23 09:40:32
# @Last Modified by:   Phu Hoang
# @Last Modified time: 2017-06-16 10:53:12

import logging
from requests.exceptions import ReadTimeout
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from http_request_randomizer.requests.parsers.FreeProxyParser import FreeProxyParser
from http_request_randomizer.requests.parsers.ProxyForEuParser import ProxyForEuParser
from http_request_randomizer.requests.parsers.RebroWeeblyParser import RebroWeeblyParser
from http_request_randomizer.requests.parsers.SamairProxyParser import SamairProxyParser
from http_request_randomizer.requests.parsers.HideMyAssProxyParser import HideMyAssProxyParser
from http_request_randomizer.requests.useragent.userAgent import UserAgentManager

# Push back requests library to at least warnings
logging.getLogger("requests").setLevel(logging.WARNING)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-6s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)


class Proxy(RequestProxy):
    def __init__(self, web_proxy_list=[], sustain=False, timeout=20):
        self.userAgent = UserAgentManager()
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(0)

        #####
        # Each of the classes below implements a specific URL Parser
        #####
        parsers = list([])
        parsers.append(FreeProxyParser('http://free-proxy-list.net', timeout=timeout))
        parsers.append(ProxyForEuParser('http://proxyfor.eu/geo.php', 1.0, timeout=timeout))
        parsers.append(RebroWeeblyParser('http://rebro.weebly.com', timeout=timeout))
        # parsers.append(SamairProxyParser('http://samair.ru/proxy/time-01.htm', timeout=timeout))
        parsers.append(HideMyAssProxyParser('http://proxylist.hidemyass.com/', timeout=timeout))

        self.sustain = sustain
        self.parsers = parsers
        self.proxy_list = web_proxy_list

        if len(self.proxy_list) == 0:
            self.logger.debug("=== Initialized Proxy Parsers ===")
            for i in range(len(parsers)):
                self.logger.debug("\t {0}".format(parsers[i].__str__()))
            self.logger.debug("=================================")

            for i in range(len(parsers)):
                try:
                    self.proxy_list += parsers[i].parse_proxyList()
                except ReadTimeout:
                    self.logger.warn("Proxy Parser: '{}' TimedOut!".format(parsers[i].url))
        else:
            print("Loaded proxies from file")

        self.current_proxy = self.randomize_proxy()
