from config import *

def choose_physical_device(instance, debug):
    if debug:
        print("\n")
        print("Choosing physical device")

    availableDevices = vkEnumeratePhysicalDevices(instance)

    if debug:
        print(f'There are {len(availableDevices)}, available devices')
    
    devices = []
    for device in availableDevices:
        if debug:
            log_device_properties(device)
        if is_suitable(device, debug):
            devices.append(device)
    return devices

class QueueFamilyIndices:
    def __init__(self):
        self.graphicsQueueFamily = None
        self.presentQueueFamily = None
        
    def is_complete(self):
        return self.graphicsQueueFamily is not None and self.presentQueueFamily is not None
    
    

def log_device_properties(device):
    properties = vkGetPhysicalDeviceProperties(device)

    print(f'Device name: {properties.deviceName}')
    print(f'Device type: ', end='')

    if properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_CPU:
        print('CPU')
    elif properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU:
        print('Discrete GPU')
    elif properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU:
        print('Integrated GPU')
    else:
        print('other')
    
def is_suitable(device, debug):
    if debug:
        print('Checking if device is suitable')

    requestedExtensions = [
        VK_KHR_SWAPCHAIN_EXTENSION_NAME
    ]

    if debug:
        print('Requesting extensions')
        for extension in requestedExtensions:
            print(f'  {extension}')
    
    if check_device_extension_support(device, requestedExtensions, debug):
        if debug:
            print('Device is suitable')
        return True

    if debug:
        print('Device is not suitable')
    return False

def check_device_extension_support(device, requestedExtensions, debug):
    supportedExtensions = [
        extension.extensionName for extension in vkEnumerateDeviceExtensionProperties(device, None)
    ]

    if debug:
        print(f'Supported extensions:')
        for extension in supportedExtensions:
            print(f'  {extension}')

    for extension in requestedExtensions:
        if extension not in supportedExtensions:
            return False
    
    return True

def find_queue_families(device, debug):

    indices = QueueFamilyIndices()

    queueFamilies = vkGetPhysicalDeviceQueueFamilyProperties(device)

    if debug:
        print(f'There are {len(queueFamilies)} queueFamilies')

    for i, queueFamily in enumerate(queueFamilies):

        if queueFamily.queueFlags & VK_QUEUE_GRAPHICS_BIT:
            indices.graphicsFamily = i
            indices.presentFamily = i
            if debug:
                print(f'Found graphics queue family {i}')

    return indices

def create_logical_device(physicalDevice, debug):


    indices = find_queue_families(physicalDevice, debug)

    queueCreateInfo = VkDeviceQueueCreateInfo(
        queueFamilyIndex = indices.graphicsFamily,
        queueCount = 1,
        pQueuePriorities = [1.0,]
    )

    deviceFeatures = VkPhysicalDeviceFeatures()

    enabledLayers = []

    create_Info = VkDeviceCreateInfo(
        queueCreateInfoCount = 1, pQueueCreateInfos = [queueCreateInfo,],
        enabledExtensionCount = 0,
        pEnabledFeatures = [deviceFeatures,],
        enabledLayerCount = len(enabledLayers), ppEnabledLayerNames = enabledLayers
    )

    return vkCreateDevice(physicalDevice = physicalDevice, pCreateInfo = [create_Info,], pAllocator = None)

def get_queue(physicalDevice, device, debug):
    indices = find_queue_families(physicalDevice, debug)

    return vkGetDeviceQueue(
        device = device,
        queueFamilyIndex = indices.graphicsFamily,
        queueIndex = 0
    )