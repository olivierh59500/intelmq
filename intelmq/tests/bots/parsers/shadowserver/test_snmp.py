# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils
from intelmq.bots.parsers.shadowserver.parser import ShadowserverParserBot

with open(os.path.join(os.path.dirname(__file__), 'snmp.csv')) as handle:
    EXAMPLE_FILE = handle.read()
EXAMPLE_LINES = EXAMPLE_FILE.splitlines()

with open(os.path.join(os.path.dirname(__file__),
                       'snmp_RECONSTRUCTED.csv')) as handle:
    RECONSTRUCTED_FILE = handle.read()
RECONSTRUCTED_LINES = RECONSTRUCTED_FILE.splitlines()

EXAMPLE_REPORT = {"feed.name": "ShadowServer SNMP",
                  "raw": utils.base64_encode(EXAMPLE_FILE),
                  "__type": "Report",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EVENTS = [{'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "Hardware: x86 Family 6 Model 8 Stepping 6 AT/AT COMPATIBLE - Software: Windows 2000 Version 5.0 (Build 2195 Uniprocessor Free)", "sysname": "ORSONKA", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[1], ''])),
           'source.asn': 22864,
           'source.geolocation.cc': 'US',
           'source.geolocation.city': 'EDINBURG',
           'source.geolocation.region': 'TEXAS',
           'source.ip': '129.113.21.93',
           'source.port': 161,
           'source.reverse_dns': 'doesnotexist.utpa.edu',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:50+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "ADSL Modem", "sysname": "tc", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[2], ''])),
           'source.asn': 3269,
           'source.geolocation.cc': 'IT',
           'source.geolocation.city': 'RAVENNA',
           'source.geolocation.region': 'EMILIA-ROMAGNA',
           'source.ip': '79.2.242.16',
           'source.port': 17080,
           'source.reverse_dns': 'host16-242-dynamic.2-79-r.retail.telecomitalia.it',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[3], ''])),
           'source.asn': 34610,
           'source.geolocation.cc': 'SE',
           'source.geolocation.city': 'UMEA',
           'source.geolocation.region': 'VASTERBOTTENS LAN',
           'source.ip': '95.109.21.127',
           'source.port': 161,
           'source.reverse_dns': 'ip6-127.skekraft.riksnet.se',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "Linux ADSL2PlusRouter 2.6.19 #7 Tue Apr 9 17:06:16 CST 2013 mips", "sysname": "TD5130", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[4], ''])),
           'source.asn': 7738,
           'source.geolocation.cc': 'BR',
           'source.geolocation.city': 'RIO DE JANEIRO',
           'source.geolocation.region': 'RIO DE JANEIRO',
           'source.ip': '201.8.4.57',
           'source.port': 161,
           'source.reverse_dns': '201-8-4-57.user.veloxzone.com.br',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "Linux R6100 2.6.31 #1 Tue Jun 4 06:50:58 EDT 2013 mips MIB=01a01", "sysname": "Unknow", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[5], ''])),
           'source.asn': 11427,
           'source.geolocation.cc': 'US',
           'source.geolocation.city': 'DALLAS',
           'source.geolocation.region': 'TEXAS',
           'source.ip': '76.186.106.223',
           'source.port': 161,
           'source.reverse_dns': 'cpe-76-186-106-223.tx.res.rr.com',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "110TC1", "sysname": "Beetel", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[6], ''])),
           'source.asn': 24560,
           'source.geolocation.cc': 'IN',
           'source.geolocation.city': 'GURGAON',
           'source.geolocation.region': 'HARYANA',
           'source.ip': '182.68.111.119',
           'source.port': 10214,
           'source.reverse_dns': 'abts-north-dynamic-119.111.68.182.airtelbroadband.in',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "BCW710J <<HW_REV: 1.01; VENDOR: Bnmux; BOOTR: 2.4.0alpha14; SW_REV: 5.30.5; MODEL: BCW710J>>", "sysname": "CableHome", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[7], ''])),
           'source.asn': 24249,
           'source.geolocation.cc': 'JP',
           'source.geolocation.city': 'TOKYO',
           'source.geolocation.region': 'TOKYO',
           'source.ip': '125.214.158.32',
           'source.port': 161,
           'source.reverse_dns': 'jway-125-214-158-032.jway.ne.jp',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "Linux WNR1000v2 2.6.15 #199 Thu Jan 28 09:49:57 CST 2010 mips MIB=01a01", "sysname": "Unknow", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[8], ''])),
           'source.asn': 10796,
           'source.geolocation.cc': 'US',
           'source.geolocation.city': 'LOUISVILLE',
           'source.geolocation.region': 'KENTUCKY',
           'source.ip': '74.138.148.8',
           'source.port': 161,
           'source.reverse_dns': '74-138-148-8.dhcp.insightbb.com',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[9], ''])),
           'source.asn': 9318,
           'source.geolocation.cc': 'KR',
           'source.geolocation.city': 'SEOUL',
           'source.geolocation.region': "SEOUL-T'UKPYOLSI",
           'source.ip': '222.233.225.196',
           'source.port': 161,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'},
          {'__type': 'Event',
           'classification.identifier': 'snmp',
           'classification.taxonomy': 'Vulnerable',
           'classification.type': 'vulnerable service',
           'extra': '{"sysdesc": "D-Link Wireless Voice Gateway <<HW_REV: B4; VENDOR: D-Link; BOOTR: 2.4.0beta1; SW_REV: 1.1.0.4; MODEL: DCM-704>>", "sysname": "CableHome", "version": 2}',
           'protocol.application': 'snmp',
           'protocol.transport': 'udp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[10], ''])),
           'source.asn': 5483,
           'source.geolocation.cc': 'HU',
           'source.geolocation.city': 'BUDAPEST',
           'source.geolocation.region': 'BUDAPEST',
           'source.ip': '84.3.91.88',
           'source.port': 161,
           'source.reverse_dns': '54035b58.catv.pool.telekom.hu',
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-03-16T03:45:51+00:00'}]


class TestShadowserverParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for a ShadowserverParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = ShadowserverParserBot
        cls.default_input_message = EXAMPLE_REPORT
        cls.sysconfig = {'feedname': 'Open-SNMP'}

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        for i, EVENT in enumerate(EVENTS):
            self.assertMessageEqual(i, EVENT)


if __name__ == '__main__':
    unittest.main()
