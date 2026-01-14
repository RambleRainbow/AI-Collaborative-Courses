# 知识本体与应用 - 教学动画项目

本项目使用 [Manim](https://www.manim.community/) 生成《知识本体与应用》的教学动画。

## ⚠️ 重要配置

**所有生成的代码注释、文档、HTML页面以及动画中的文本内容必须使用中文 (Chinese)。**

这是系统级配置，请勿更改。

## 项目结构

- `src/`: 源代码目录，按幕 (Act) 和场景 (Scene) 组织。
- `manim.cfg`: Manim 渲染配置文件。
- `index.html`: 用于浏览已生成动画的本地页面。
- `script.md`: 原始脚本文件。

## 如何运行

本项目使用 `uv` 管理依赖。

1.  初始化环境: `uv sync`
2.  渲染场景 (示例): `uv run manim -pql src/act1/scene1.py Scene1`
