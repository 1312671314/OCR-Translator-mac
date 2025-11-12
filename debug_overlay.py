#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""调试 overlay 创建问题"""

import tkinter as tk
from logger import log_debug

def check_overlay_status(app):
    """检查 overlay 状态"""
    print("\n" + "="*60)
    print("Overlay 状态检查")
    print("="*60)
    
    # 检查 source_overlay
    print("\n1. Source Overlay:")
    if app.source_overlay:
        print(f"   ✓ source_overlay 对象存在: {type(app.source_overlay)}")
        try:
            exists = app.source_overlay.winfo_exists()
            print(f"   winfo_exists(): {exists}")
        except Exception as e:
            print(f"   ✗ winfo_exists() 失败: {e}")
        
        try:
            viewable = app.source_overlay.winfo_viewable()
            print(f"   winfo_viewable(): {viewable}")
        except Exception as e:
            print(f"   ✗ winfo_viewable() 失败: {e}")
        
        try:
            geometry = app.source_overlay.get_geometry()
            print(f"   geometry: {geometry}")
        except Exception as e:
            print(f"   ✗ get_geometry() 失败: {e}")
    else:
        print("   ✗ source_overlay 为 None")
    
    # 检查 target_overlay
    print("\n2. Target Overlay:")
    if app.target_overlay:
        print(f"   ✓ target_overlay 对象存在: {type(app.target_overlay)}")
        try:
            exists = app.target_overlay.winfo_exists()
            print(f"   winfo_exists(): {exists}")
        except Exception as e:
            print(f"   ✗ winfo_exists() 失败: {e}")
        
        try:
            viewable = app.target_overlay.winfo_viewable()
            print(f"   winfo_viewable(): {viewable}")
        except Exception as e:
            print(f"   ✗ winfo_viewable() 失败: {e}")
    else:
        print("   ✗ target_overlay 为 None")
    
    # 检查 source_area
    print("\n3. Source Area:")
    if hasattr(app, 'source_area') and app.source_area:
        print(f"   ✓ source_area: {app.source_area}")
    else:
        print("   ✗ source_area 未设置")
    
    # 检查 target_area
    print("\n4. Target Area:")
    if hasattr(app, 'target_area') and app.target_area:
        print(f"   ✓ target_area: {app.target_area}")
    else:
        print("   ✗ target_area 未设置")
    
    print("\n" + "="*60)
    print("检查完成")
    print("="*60 + "\n")

if __name__ == "__main__":
    print("这个脚本需要在应用运行时调用")
    print("在 app_logic.py 的 start_translation 方法开始处添加：")
    print("from debug_overlay import check_overlay_status")
    print("check_overlay_status(self)")
