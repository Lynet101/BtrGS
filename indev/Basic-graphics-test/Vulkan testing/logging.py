from config import *

def debugCallback(*args):
    print(f'debug messenger has {len(args)} components')
    for arg in args:
        print(arg)
    

def make_debug_messenger(instance):
    createInfo = VkDebugReportCallbackCreateInfoEXT(
        flags=VK_DEBUG_REPORT_ERROR_BIT_EXT | VK_DEBUG_REPORT_WARNING_BIT_EXT,
        pfnCallback=debugCallback
    )

    creationFunction = vkGetInstanceProcAddr(instance, 'vkCreateDebugReportCallbackEXT')

    return creationFunction(instance, createInfo, None)