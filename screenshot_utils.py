#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""跨平台截图工具"""

import sys
from PIL import Image, ImageGrab
from logger import log_debug

def capture_screen_region(x1, y1, width, height):
    """
    跨平台截图函数
    
    Args:
        x1, y1: 左上角坐标
        width, height: 宽度和高度
    
    Returns:
        PIL.Image 或 None
    """
    try:
        if sys.platform == "darwin":  # macOS
            # macOS 上使用 PIL.ImageGrab，更可靠
            x2 = x1 + width
            y2 = y1 + height
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            return screenshot
        else:
            # Windows/Linux 使用 pyautogui
            import pyautogui
            screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
            return screenshot
    except Exception as e:
        log_debug(f"Screenshot error: {e}")
        # 如果失败，尝试全屏截图然后裁剪
        try:
            full_screenshot = ImageGrab.grab()
            x2 = x1 + width
            y2 = y1 + height
            cropped = full_screenshot.crop((x1, y1, x2, y2))
            return cropped
        except Exception as e2:
            log_debug(f"Fallback screenshot also failed: {e2}")
            return None
