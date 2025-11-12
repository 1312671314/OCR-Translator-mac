#!/bin/bash
# Mac 兼容性修复脚本

echo "正在修复 Mac 兼容性问题..."
echo ""

# 1. 卸载可能导致 bus error 的 keyboard 库
echo "步骤 1: 卸载 keyboard 库（Mac 上不兼容）..."
pip uninstall keyboard -y

# 2. 检查 pyautogui 版本
echo ""
echo "步骤 2: 检查 pyautogui..."
pip show pyautogui

# 3. 确保 Pillow 和 OpenCV 兼容
echo ""
echo "步骤 3: 重新安装图像处理库..."
pip install --upgrade --force-reinstall Pillow opencv-python

echo ""
echo "修复完成！现在尝试运行："
echo "python main.py"
