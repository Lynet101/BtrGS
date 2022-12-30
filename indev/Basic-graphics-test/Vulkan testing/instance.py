from config import *

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
        print(f'extensions to be requested:')

        for ext in extensions:
            print(f'  {ext}')
    

    createInfo = VkInstanceCreateInfo(
        pApplicationInfo = appInfo,
        enabledLayerCount = 0, ppEnabledLayerNames = None,
        enabledExtensionCount = len(extensions), ppEnabledExtensionNames = extensions
    )


    try:
        return vkCreateInstance(createInfo, None)
    except:
        if (debug):
            print("Failed to create instance")
        return None

    