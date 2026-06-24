# OpenHuman — 纯 WebGL 数字人引擎

## 小红书版本

标题：纯 WebGL 数字人引擎（13字）

---

OpenHuman——纯 WebGL 2.0 数字人渲染引擎。
零运行时依赖，不套 Three.js，打包不到 200KB。

只做渲染，不做建模。

用它做什么？
🖥️ <open-human> 自定义标签嵌入，一行 HTML 让数字人上线
🎭 52 个 FACS 面部表情精准控制
🎬 idle → talk → gesture 动画状态机
📡 WebSocket 流式驱动，TTS 唇形同步、动捕实时推流
✨ 皮肤 SSS 渲染 + Bloom + ACES 色调映射

性能碾压？
· Chrome 60+ / Safari 15+ / Firefox 55+
· 手机端 30fps+
· Shadow map + 后处理全开不掉帧

怎么用？
npm install @openhuman/sdk
然后 <open-human src="./char.ohb">

.ohb 格式 = glTF + KTX2 纹理 + 骨骼 + 形变目标

刚上线，GitHub 可关注。
数字人不再是大厂特权——一行标签就够了。

#OpenHuman #WebGL #数字人 #AI渲染 #开源

---

卡片设计（4 浅色中文 + 4 深色英文）

浅色中文卡片（奶油色底 #FAF7F2, 深色字 #1E293B）:

1. **oh-cover-zh** — 大标题 OpenHuman + "纯 WebGL 2.0 数字人渲染引擎"
2. **oh-card-1-zh** — "零依赖 · 极轻量" 性能指标展示
3. **oh-card-2-zh** — "一行标签嵌入" Web Component + SDK 代码示例
4. **oh-card-3-zh** — "流式动画驱动" TTS 唇形同步 / MoCap / 动画状态机

深色英文卡片（深蓝底 #0B1027, 浅色字 #F1F5F9）:

5. **oh-cover-en** — Big title "OpenHuman" + "Pure WebGL 2.0 Digital Human Engine"
6. **oh-card-1-en** — "Zero Runtime Deps" specs showcase
7. **oh-card-2-en** — "Web Component Ready" embed + SDK code
8. **oh-card-3-en** — "Real-time Streaming" TTS / MoCap / Animation Graph

---

## Twitter 版本

OpenHuman 纯 WebGL 数字人引擎，≤200KB 零依赖。一行 HTML 标签嵌入数字人，WebSocket 流式唇形同步。开源可玩。

#OpenHuman #WebGL #DigitalHuman

配图：oh-cover-en.png, oh-card-1-en.png, oh-card-2-en.png, oh-card-3-en.png（选 2-4 张深色英文卡）

---

## 完整信息

> Website: [openhuman.ai](https://openhuman.ai)
> SDK: `npm install @openhuman/sdk`
> GitHub: [github.com/openhuman-ai](https://github.com/openhuman-ai)
> Twitter: @openhuman

## Features

- **纯 WebGL 2.0** — zero runtime dependencies, no Three.js/Babylon.js
- **≤200KB gzipped** — full engine in one self-contained package
- **Web Component** — `<open-human src="./char.ohb">` for zero-config embedding
- **52 FACS blendshapes** — full facial expression control
- **Animation Graph** — idle → talk → gesture state machine
- **WebSocket Streaming** — real-time TTS lip sync & mocap (<50ms latency)
- **Production Rendering** — PCF shadows, SSS skin, Bloom, DoF, ACES tonemapping, FXAA

## Browser Support

| Browser | Status |
|---------|--------|
| Chrome 60+ | Full |
| Firefox 55+ | Full |
| Edge 79+ | Full |
| Safari 15+ | Full |
| Chrome Android | 30fps+ |
| Safari iOS 15+ | 30fps+ |

## Quick Start

```bash
npm install @openhuman/sdk
```

```javascript
import { OpenHuman } from "@openhuman/sdk"
const human = new OpenHuman({ canvas, quality: "high" })
await human.loadCharacter("./characters/default.ohb")
human.play("idle")
```

### Web Component

```html
<script type="module" src="https://cdn.openhuman.io/sdk/latest/embed.js"></script>
<open-human src="./char.ohb" animation="idle" quality="high"></open-human>
```

### Streaming

```javascript
import { OpenHuman, StreamingClient } from "@openhuman/sdk"
const stream = new StreamingClient({
  url: "wss://your-server.example.com/animation-stream",
  jitterBuffer: 80,
})
stream.on("frame", (pose) => human.applyPose(pose))
stream.connect()
```

## Character Format

`.ohb` (OpenHuman Bundle) — glTF mesh + KTX2 textures + skeleton + 52 FACS morph targets

## License

MIT Open Source