<div align="center">

# 🔍 IPInfo CLI

**A Modern Command-Line Tool for IP Address Information Lookup**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)](https://github.com/gitstq/ipinfo-cli)

**🌍 Languages / 语言 / 語言**

[English](#-english) | [简体中文](#-简体中文) | [繁體中文](#-繁體中文)

---

</div>

---

## 🇬🇧 English

### 🎉 Introduction

**IPInfo CLI** is a lightweight, modern command-line tool for retrieving detailed information about IP addresses. Whether you're a developer, system administrator, or security professional, this tool provides quick and accurate IP geolocation, ISP details, and network information right from your terminal.

**Key Highlights:**
- 🚀 **Fast & Lightweight** - Get results in milliseconds
- 🎨 **Beautiful Output** - Rich, colorful terminal display
- 📊 **Multiple Formats** - Table, JSON, or compact output
- 🔒 **Privacy Focused** - No data collection, uses public APIs
- 🌐 **IPv4 & IPv6** - Full support for both protocols

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔍 **IP Lookup** | Query any public IP address for detailed information |
| 📍 **Geolocation** | Get city, region, country, and coordinates |
| 🏢 **Organization** | View ISP and organization details |
| ⏰ **Timezone** | Display timezone information |
| 📋 **JSON Export** | Export data in JSON format for scripting |
| 🎯 **Self IP** | Quickly check your own public IP |

### 🚀 Quick Start

#### Requirements
- Python 3.8 or higher
- pip (Python package manager)

#### Installation

```bash
# Install from PyPI (recommended)
pip install ipinfo-cli

# Or install from source
git clone https://github.com/gitstq/ipinfo-cli.git
cd ipinfo-cli
pip install -e .
```

#### Usage

```bash
# Check your public IP
ipinfo

# Look up a specific IP address
ipinfo 8.8.8.8

# Output as JSON
ipinfo 8.8.8.8 --json

# Compact output
ipinfo 8.8.8.8 --compact

# Show version
ipinfo --version
```

### 📖 Detailed Usage Guide

#### Basic Commands

```bash
# Get your public IP information
$ ipinfo

🔍 IP Information: 203.0.113.45
┌─────────────────┬──────────────────────────────┐
│ Field           │ Value                        │
├─────────────────┼──────────────────────────────┤
│ 🌐 IP Address   │ 203.0.113.45                 │
│ 🏙️ City         │ San Francisco                │
│ 📍 Region       │ California                   │
│ 🌍 Country      │ United States                │
│ 🏢 Organization │ Example ISP Inc.             │
│ ⏰ Timezone     │ America/Los_Angeles          │
└─────────────────┴──────────────────────────────┘
```

#### JSON Output (Perfect for Scripts)

```bash
$ ipinfo 1.1.1.1 -j

{
  "ip": "1.1.1.1",
  "hostname": "one.one.one.one",
  "city": "Sydney",
  "region": "New South Wales",
  "country": "Australia",
  "location": "-33.8688,151.2093",
  "organization": "Cloudflare, Inc.",
  "timezone": "Australia/Sydney"
}
```

#### Use Cases

1. **Network Debugging** - Quickly identify IP-related issues
2. **Security Analysis** - Investigate suspicious IP addresses
3. **Automation Scripts** - Parse JSON output in your scripts
4. **Geolocation Services** - Get location data for applications
5. **DevOps** - Monitor and log IP information in pipelines

### 💡 Design Philosophy

IPInfo CLI was designed with simplicity and efficiency in mind:
- **Minimal Dependencies** - Only essential packages required
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **API Fallback** - Multiple API sources for reliability
- **Clean Code** - Well-documented, type-hinted Python code

### 📦 Packaging & Deployment

```bash
# Build the package
pip install build
python -m build

# The distribution files will be in dist/
```

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🇨🇳 简体中文

### 🎉 项目介绍

**IPInfo CLI** 是一款轻量级、现代化的命令行工具，用于查询IP地址的详细信息。无论您是开发者、系统管理员还是安全专业人员，这款工具都能在终端中快速准确地提供IP地理位置、ISP详情和网络信息。

**核心亮点：**
- 🚀 **快速轻量** - 毫秒级响应
- 🎨 **美观输出** - 丰富多彩的终端显示
- 📊 **多种格式** - 支持表格、JSON或紧凑输出
- 🔒 **隐私优先** - 不收集数据，使用公共API
- 🌐 **IPv4 & IPv6** - 完整支持两种协议

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🔍 **IP查询** | 查询任意公网IP地址的详细信息 |
| 📍 **地理位置** | 获取城市、地区、国家和坐标 |
| 🏢 **组织信息** | 查看ISP和组织详情 |
| ⏰ **时区信息** | 显示时区数据 |
| 📋 **JSON导出** | 导出JSON格式数据用于脚本 |
| 🎯 **本机IP** | 快速查看自己的公网IP |

### 🚀 快速开始

#### 环境要求
- Python 3.8 或更高版本
- pip（Python包管理器）

#### 安装方式

```bash
# 从PyPI安装（推荐）
pip install ipinfo-cli

# 或从源码安装
git clone https://github.com/gitstq/ipinfo-cli.git
cd ipinfo-cli
pip install -e .
```

#### 使用方法

```bash
# 查看您的公网IP
ipinfo

# 查询特定IP地址
ipinfo 8.8.8.8

# JSON格式输出
ipinfo 8.8.8.8 --json

# 紧凑格式输出
ipinfo 8.8.8.8 --compact

# 显示版本
ipinfo --version
```

### 📖 详细使用指南

#### 基本命令

```bash
# 获取您的公网IP信息
$ ipinfo

🔍 IP Information: 203.0.113.45
┌─────────────────┬──────────────────────────────┐
│ 字段            │ 值                           │
├─────────────────┼──────────────────────────────┤
│ 🌐 IP地址       │ 203.0.113.45                 │
│ 🏙️ 城市         │ 旧金山                       │
│ 📍 地区         │ 加利福尼亚                   │
│ 🌍 国家         │ 美国                         │
│ 🏢 组织         │ Example ISP Inc.             │
│ ⏰ 时区         │ America/Los_Angeles          │
└─────────────────┴──────────────────────────────┘
```

#### JSON输出（适合脚本使用）

```bash
$ ipinfo 1.1.1.1 -j

{
  "ip": "1.1.1.1",
  "hostname": "one.one.one.one",
  "city": "Sydney",
  "region": "New South Wales",
  "country": "Australia",
  "location": "-33.8688,151.2093",
  "organization": "Cloudflare, Inc.",
  "timezone": "Australia/Sydney"
}
```

#### 应用场景

1. **网络调试** - 快速识别IP相关问题
2. **安全分析** - 调查可疑IP地址
3. **自动化脚本** - 在脚本中解析JSON输出
4. **地理位置服务** - 为应用获取位置数据
5. **DevOps** - 在流水线中监控和记录IP信息

### 💡 设计理念

IPInfo CLI 以简洁高效为设计理念：
- **最小依赖** - 仅需必要的包
- **跨平台** - 支持 Windows、macOS 和 Linux
- **API容错** - 多API源确保可靠性
- **整洁代码** - 文档完善、类型提示完整的Python代码

### 📦 打包与部署

```bash
# 构建包
pip install build
python -m build

# 分发文件将生成在 dist/ 目录
```

### 🤝 贡献指南

欢迎贡献代码！请随时提交Pull Request。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: 添加某个很棒的特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 📄 开源协议

本项目采用 MIT 协议开源 - 详情请查看 [LICENSE](LICENSE) 文件。

---

## 🇹🇼 繁體中文

### 🎉 專案介紹

**IPInfo CLI** 是一款輕量級、現代化的命令列工具，用於查詢IP地址的詳細資訊。無論您是開發者、系統管理員還是安全專業人員，這款工具都能在終端機中快速準確地提供IP地理位置、ISP詳情和網路資訊。

**核心亮點：**
- 🚀 **快速輕量** - 毫秒級響應
- 🎨 **美觀輸出** - 豐富多彩的終端顯示
- 📊 **多種格式** - 支援表格、JSON或緊湊輸出
- 🔒 **隱私優先** - 不收集資料，使用公共API
- 🌐 **IPv4 & IPv6** - 完整支援兩種協定

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🔍 **IP查詢** | 查詢任意公網IP地址的詳細資訊 |
| 📍 **地理位置** | 取得城市、地區、國家和座標 |
| 🏢 **組織資訊** | 查看ISP和組織詳情 |
| ⏰ **時區資訊** | 顯示時區資料 |
| 📋 **JSON匯出** | 匯出JSON格式資料用於腳本 |
| 🎯 **本機IP** | 快速查看自己的公網IP |

### 🚀 快速開始

#### 環境要求
- Python 3.8 或更高版本
- pip（Python套件管理器）

#### 安裝方式

```bash
# 從PyPI安裝（推薦）
pip install ipinfo-cli

# 或從原始碼安裝
git clone https://github.com/gitstq/ipinfo-cli.git
cd ipinfo-cli
pip install -e .
```

#### 使用方法

```bash
# 查看您的公網IP
ipinfo

# 查詢特定IP地址
ipinfo 8.8.8.8

# JSON格式輸出
ipinfo 8.8.8.8 --json

# 緊湊格式輸出
ipinfo 8.8.8.8 --compact

# 顯示版本
ipinfo --version
```

### 📖 詳細使用指南

#### 基本命令

```bash
# 取得您的公網IP資訊
$ ipinfo

🔍 IP Information: 203.0.113.45
┌─────────────────┬──────────────────────────────┐
│ 欄位            │ 值                           │
├─────────────────┼──────────────────────────────┤
│ 🌐 IP地址       │ 203.0.113.45                 │
│ 🏙️ 城市         │ 舊金山                       │
│ 📍 地區         │ 加利福尼亞                   │
│ 🌍 國家         │ 美國                         │
│ 🏢 組織         │ Example ISP Inc.             │
│ ⏰ 時區         │ America/Los_Angeles          │
└─────────────────┴──────────────────────────────┘
```

#### JSON輸出（適合腳本使用）

```bash
$ ipinfo 1.1.1.1 -j

{
  "ip": "1.1.1.1",
  "hostname": "one.one.one.one",
  "city": "Sydney",
  "region": "New South Wales",
  "country": "Australia",
  "location": "-33.8688,151.2093",
  "organization": "Cloudflare, Inc.",
  "timezone": "Australia/Sydney"
}
```

#### 應用場景

1. **網路除錯** - 快速識別IP相關問題
2. **安全分析** - 調查可疑IP地址
3. **自動化腳本** - 在腳本中解析JSON輸出
4. **地理位置服務** - 為應用取得位置資料
5. **DevOps** - 在管線中監控和記錄IP資訊

### 💡 設計理念

IPInfo CLI 以簡潔高效為設計理念：
- **最小依賴** - 僅需必要的套件
- **跨平台** - 支援 Windows、macOS 和 Linux
- **API容錯** - 多API來源確保可靠性
- **整潔程式碼** - 文件完善、型別提示完整的Python程式碼

### 📦 打包與部署

```bash
# 建構套件
pip install build
python -m build

# 分發檔案將生成在 dist/ 目錄
```

### 🤝 貢獻指南

歡迎貢獻程式碼！請隨時提交Pull Request。

1. Fork 本儲存庫
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'feat: 新增某個很棒的功能'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 📄 開源授權

本專案採用 MIT 授權條款開源 - 詳情請查看 [LICENSE](LICENSE) 檔案。

---

<div align="center">

**Made with ❤️ by [gitstq](https://github.com/gitstq)**

**⭐ If this project helps you, please give it a star! ⭐**

</div>
