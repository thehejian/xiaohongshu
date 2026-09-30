# -*- coding: utf-8 -*-
"""三个系列的流程参数（一张图 + 三套 profile）。

参数来源：ai_doc/macmin_*小红书创作与发布指南.md 的「总体流程架构」与「环境速查」。
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SeriesProfile:
    name: str
    folder_token: str      # 飞书 --parent-token
    title_prefix: str      # 飞书文档标题前缀，如 场景{N}：
    words_min: int         # 写后验证字数下限（含标题行）
    words_max: int
    image_count: int       # 0 = 不生图（游记用照片）
    image_style: str       # inkwash | flat-tech | none
    needs_image_gen: bool
    serial_image_verify: bool   # 科技类：逐张生成→逐张验字
    dir_template: str      # 目录名模板，{n}=序号 {slug}=英文 slug


PROFILES: dict[str, SeriesProfile] = {
    "history": SeriesProfile(
        name="history",
        folder_token="JUBNfa8TyldTHsd9pzNcOTbynWf",  # 两汉风云
        title_prefix="场景{n}：",
        words_min=700,
        words_max=900,
        image_count=3,
        image_style="inkwash",
        needs_image_gen=True,
        serial_image_verify=False,
        dir_template="topic-{n}",
    ),
    "tech": SeriesProfile(
        name="tech",
        folder_token="LFpJf4lSRlMUKpdPi9fcWIjhnNZ",  # 科技
        title_prefix="",
        words_min=750,
        words_max=900,
        image_count=3,
        image_style="flat-tech",
        needs_image_gen=True,
        serial_image_verify=True,
        dir_template="{slug}",
    ),
    "travel": SeriesProfile(
        name="travel",
        folder_token="L8MKfqrG6lNMJkdf79ZcrB8inJg",  # 游记
        title_prefix="",
        words_min=650,
        words_max=800,
        image_count=0,
        image_style="none",
        needs_image_gen=False,
        serial_image_verify=False,
        dir_template="{slug}",
    ),
}
