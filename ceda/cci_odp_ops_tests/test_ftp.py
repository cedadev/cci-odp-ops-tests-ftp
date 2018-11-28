#!/usr/bin/env python
"""Test CCI Open Data Portal FTP service
"""
__author__ = "P J Kershaw"
__date__ = "23/04/18"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id$'
import unittest
import os
from ftplib import FTP


class FtpTestCase(unittest.TestCase):
    '''Unit test case for testing ESA CCI Open Data Portal FTP Service'''

    FTP_SERVER_ADDR = 'anon-ftp.ceda.ac.uk'
    TOP_DIR = 'neodc'
    CCI_DIR = os.path.join(TOP_DIR, 'esacci')
    SEA_LEVEL_README_FILEPATH = os.path.join(CCI_DIR, 'sea_level', '00README')
    
    def setUp(self):
        super(FtpTestCase, self).setUp()
        self.ftp_client = FTP()
        self.ftp_client.connect(self.__class__.FTP_SERVER_ADDR)
        self.ftp_client.login()
        
    def tearDown(self):
        self.ftp_client.quit()
        super(FtpTestCase, self).tearDown()
        
    def test_01_change_to_top_dir(self):   
        print(self.ftp_client.cwd(self.__class__.TOP_DIR))
        
    def test_02_list_cci_dir(self):   
        self.ftp_client.cwd(self.__class__.CCI_DIR)
        self.assertGreater(len(self.ftp_client.nlst()), 0,
                            'Got empty dir listing for {!r}'.format(
                                self.__class__.CCI_DIR))
        
    def test_03_get_sea_level_readme(self): 
        import io  
        readme_txt = io.BytesIO()
        self.ftp_client.retrbinary(
            'RETR {}'.format(self.__class__.SEA_LEVEL_README_FILEPATH), 
            readme_txt.write)
        
        self.assertGreater(len(readme_txt.getvalue()), 0, 
                           'Got zero length readme file {!r}'.format(
                               self.__class__.SEA_LEVEL_README_FILEPATH))