from config import *

def supported(extensions, layers, debug):
#Extensions
    supported_extensions = [extension.extensionName for extension in vkEnumerateInstanceExtensionProperties(None)]

    if debug:
        print("Supported extensions:")
        for extension in supported_extensions:
            print(extension)
        
    for extension in extensions:
        if extension in supported_extensions:
            if debug:
                print("Extension %s is supported" % extension)
        else:
            if debug:
                print("Extension %s is not supported" % extension)
            return False

#Layers
    supported_layers = [layer.layerName for layer in vkEnumerateInstanceLayerProperties()]

    if debug:
        print("Supported layers:")
        for layer in supported_layers:
            print(layer)
    
    for layer in layers:
        if layer in supported_layers:
            if debug:
                print("Layer %s is supported" % layer)
        else:
            if debug:
                print("Layer %s is not supported" % layer)
            return False


def make_instance(debug, applicationName):
    if debug:
        print("Creating instance")

    version = vkEnumerateInstanceVersion()

    if debug:
        print(
            f"System can support the following versions of vulkan variant: {version >> 29}\
            , Major: {VK_VERSION_MAJOR(version) & 0x7F}\
            , Minor: {VK_VERSION_MINOR(version)}\
            , Patch: {VK_VERSION_PATCH(version)}"
            )

    version = VK_MAKE_VERSION(1, 0, 0)

    appInfo = VkApplicationInfo(
        pApplicationName = applicationName,
        applicationVersion = version, 
        pEngineName = "No engine for you!",
        engineVersion = 0,
        apiVersion = version
    )
    
    extensions = glfw.get_required_instance_extensions()


    if debug:
        extensions.append(VK_EXT_DEBUG_REPORT_EXTENSION_NAME)


    if debug:
        print(f'extensions to be requested:')

        for ext in extensions:
            print(f'  {ext}')
    
    layers = []

    supported(extensions, layers, debug)

    createInfo = VkInstanceCreateInfo(
        pApplicationInfo = appInfo,
        enabledLayerCount = len(layers), ppEnabledLayerNames = None,
        enabledExtensionCount = len(extensions), ppEnabledExtensionNames = extensions
    )


    try:
        return vkCreateInstance(createInfo, None)
    except:
        if (debug):
            print("Failed to create instance")
        return None

