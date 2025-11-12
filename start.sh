#!/bin/bash
# 启动脚本 - 隐藏 macOS 输入法警告

# 激活 conda 环境
source /opt/miniconda3/bin/activate zimuOCR

# 运行应用，过滤掉 IMK 错误
python main.py 2>&1 | grep -v "IMKCFRunLoopWakeUpReliable"
