""" Preload module for DeepDanbooru or onnxtagger. """
from pathlib import Path
from argparse import ArgumentParser

from modules.shared import models_path  # pylint: disable=import-error

root_dir = Path(__file__).parent.parent

default_ddp_path = Path(models_path, 'deepdanbooru')
default_onnx_path = Path(models_path, 'TaggerOnnx')


def preload(parser: ArgumentParser):
    """ Preload module for DeepDanbooru or onnxtagger. """
    # default deepdanbooru use different paths:
    # models/deepbooru and models/torch_deepdanbooru
    # https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/c81d440d876dfd2ab3560410f37442ef56fc6632

    parser.add_argument(
        '--deepdanbooru-projects-path',
        type=str,
        help='Path to directory with DeepDanbooru project(s).',
        default=default_ddp_path
    )
    parser.add_argument(
        '--onnxtagger-path',
        type=str,
        help='Path to directory with Onnyx project(s).',
        default=default_onnx_path
    )
