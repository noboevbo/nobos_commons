class CudnnConfig(object):
    __slots__ = ['benchmark', 'deterministic', 'enabled']

    def __init__(self):
        self.enabled = True
        self.deterministic = False
        self.benchmark = True


class GpuModelConfig(object):
    __slots__ = ['use_gpu', 'gpu_number', 'cudnn_config']

    def __init__(self):
        self.use_gpu = True
        self.gpu_number = 0
        self.cudnn_config = CudnnConfig()