"""Import XLA custom call of the pipeline marker"""
import sys
from alpa.global_env import global_config

if global_config.has_cuda:
    try:
        from .build.xla_custom_call_marker import pipeline_marker, identity
    except ImportError as e:
        import os
        print(f"Cannot import XLA custom markers: {e}")
        path = os.path.dirname(__file__)
        print(f"Please run 'bash build.sh' under {path}")
        sys.exit(-1)
