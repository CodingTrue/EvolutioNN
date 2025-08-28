from evolutionn import logger
import pyopencl as cl

def get_device_info(device_info: cl.Device) -> str:
    amd_gpu = "AMD Accelerated Parallel Processing" in device_info.platform.name

    display_name = device_info.board_name_amd if amd_gpu else device_info.name
    mem_size = device_info.global_mem_size

    return f"{display_name.strip()} ({mem_size / 1024**3:0.2f} GB)"

def get_cl_devices() -> list[cl.Device]:
    devices = []

    for platform in cl.get_platforms():
        for device in platform.get_devices():
            devices.append(device)
    return devices

def debug_devices():
    logger.debug(*[
        "======== DEVICE LIST ========",
        *(f"{i}: {get_device_info(device_info)}" for i, device_info in enumerate(get_cl_devices())),
        "======== =========== ========"
    ])

class ENN:
    CL_CONTEXT = None
    CL_DEVICE = None
    CL_COMMAND_QUEUE = None

    def __init__(self, index: int):
        if ENN.CL_CONTEXT:
            logger.warning("OpenCL context was already initialized. Operation will be ignored.")
            return

        devices = get_cl_devices()
        if index >= len(devices):
            logger.error(f"Device index '{index}' is unvalid.")
            exit(-1)

        ENN.CL_DEVICE = devices[index]
        ENN.CL_CONTEXT = cl.Context([ENN.CL_DEVICE])
        ENN.CL_COMMAND_QUEUE = cl.CommandQueue(context=ENN.CL_CONTEXT, device=ENN.CL_DEVICE)