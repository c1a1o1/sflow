# -*- coding: utf-8 -*-
# CUDA_VISIBLE_DEVICE

from __future__ import absolute_import


def visible_devices(devices):
    """
    see also : http://acceleware.com/blog/cudavisibledevices-masking-gpus

    example::

        visible_devices(0)  # use gpu0 only
        visible_devices([1,3])  # use gpu1,3 only
        visible_devices('1,2,3')  # use gpu1,2,3 only
        visible_devices('cpu')   # don't use gpu

    :param devices: int | str | list(int), cpu, gpu0, ... 1,2,3 or
    :return: None
    """
    import os

    def _format():
        if isinstance(devices, int):
            return str(devices)
        elif isinstance(devices, (tuple, list)):
            return ','.join(str(d) for d in devices)
        else:
            assert isinstance(devices, (str, basestring))
            if devices is 'cpu':
                return '99'  # invalid gpu number makes all gpu invisible
            else:
                return devices

    os.environ['CUDA_VISIBLE_DEVICES'] = _format()
    print('CUDA_VISIBLE_DEVICES={0}'.format(os.environ['CUDA_VISIBLE_DEVICES']))

