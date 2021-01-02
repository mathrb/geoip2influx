import re

import pytest

from nginx_parser import IPV4_REGEX, IPV6_REGEX, IPV4_NGINX_LOG_LINE

@pytest.mark.parametrize("sample,expected", [("192.168.0.1", True), ("1.1.1.1", True), ("192.168.0.1", True), (".168.0.1", False), ("192.168.", False)])
def test_ipv4(sample, expected):
    assert (IPV4_REGEX.match(sample) != None) == expected

@pytest.mark.parametrize("sample,expected", [("fe80::215:5dff:fe9a:97e8", True), ("192.168.0.1", False)])
def test_ipv6(sample, expected):
    assert (IPV6_REGEX.match(sample) != None) == expected

def test_nginx_log_line():
    for idx, line in enumerate(open('tests/access.log')):
        assert IPV4_NGINX_LOG_LINE.match(line), "{}:{}".format(idx+1, line)