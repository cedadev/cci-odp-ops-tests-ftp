#!/usr/bin/env python
"""Nagios script to test CCI Open Data Portal THREDDS OPeNDAP service
"""
__author__ = "P J Kershaw"
__date__ = "23/04/18"
__copyright__ = "(C) 2018 Science and Technology Facilities Council"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id$'
from ceda.unittest_nagios_wrapper.script import nagios_script
from ceda.cci_odp_ops_tests.test_ftp import FtpTestCase


def main():
    '''Entry point for script - use standard nagios script'''

    # These options can be overridden by the CLI options
    SLACK_CHANNEL = 'cci-odp-ops-logging'
    SLACK_USER = 'cci-ops-test'

    nagios_script(FtpTestCase, slack_channel=SLACK_CHANNEL,
                  slack_user=SLACK_USER)


if __name__ == '__main__':
    main()
