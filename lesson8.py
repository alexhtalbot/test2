class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name='app in dev'):
        print(f"Installing {app_name}...")
        self.app_list.append(app_name)
        return self.app_list

device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()
print(device_a.app_list)
device_a.install_app('Cool new app')
print(device_a.app_list)
device_a.install_app()
print(device_a.app_list)
device_a.install_app()
print(device_a.app_list)

device_a.app_list=list(set(device_a.app_list))
print(device_a.app_list)

device_a.app_list.pop()
print(device_a.app_list)

device_b = SmartDevice(1010101, 'Samsung', 6.3, ['app number 1', 'app number 2'])
device_b.report()
print(device_b.app_list)