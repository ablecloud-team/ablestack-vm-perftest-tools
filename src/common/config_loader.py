# config_loader.py
# ---------------------------
# 현재는 사용하지 않지만, 추후 여러 모듈에서 공통으로
# config.yaml 로딩 기능을 제공하기 위해 사용할 예정입니다.
#
# 향후 예시:
# def load_config(path):
#     import yaml
#     from pathlib import Path
#     if not Path(path).exists():
#         raise FileNotFoundError(f"Config file not found: {path}")
#     with open(path, "r") as f:
#         return yaml.safe_load(f)
