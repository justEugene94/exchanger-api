import os
import socket
from datetime import datetime
from unittest import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities



SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)



class HomePage(StaticLiveServerTestCase):

    def setUp(self):
        """ install """
        # self.browser = webdriver.Chrome()
        self.browser = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )


    def tearDown(self):
        """ демонтаж """

        if self._test_has_failed():
            if not os.path.exists(SCREEN_DUMP_LOCATION):
                os.makedirs(SCREEN_DUMP_LOCATION)
        for ix, handle in enumerate(self.browser.window_handles):
            self._windowid = ix
            self.browser.switch_to.window(handle)
            self.take_screenshot()
            self.dump_html()

        self.browser.quit()
        super().tearDown()


    def _test_has_failed(self):
        """тест не сработал"""
        # слегка туманно, но не смог найти способа получше!
        return any(error for (method, error) in self._outcome.errors)


    def take_screenshot(self):
        """сделать снимок экрана"""
        filename = self._get_filename() + '.png'
        print('screenshotting to ', filename)
        self.browser.get_screenshot_as_file(filename)


    def dump_html(self):
        """выгрузить html"""
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(self.browser.page_source)


    def _get_filename(self):
        """получить имя файла"""
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}-window{windowid}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )


    def test_home_page(self):

        # User open home page
        self.browser.get('http://nginx:8000/')

        # User see title of home page
        assert 'Exchange office' in self.browser.title

        # User see exchange rates

        # User click on link