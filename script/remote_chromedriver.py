from selenium import webdriver


class RemoteChromeDriver(webdriver.Remote):
    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {}
        prefs['download.default_directory'] = '/home/seluser/Downloads/test'
        prefs['download.directory_upgrade'] = True
        prefs['download.extensions_to_open'] = ''
        prefs['download.prompt_for_download'] = False
        prefs['safebrowsing.enabled'] = True
        options.add_experimental_option("prefs", prefs)
        desired_capabilities = options.to_capabilities()

        super(RemoteChromeDriver, self).__init__(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=desired_capabilities)
