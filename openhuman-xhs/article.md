纯 WebGL 数字人引擎

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
字符模型走标准管线，开发者关注渲染就行。

刚上线，GitHub 可关注。
数字人不再是大厂特权——一行标签就够了。

#OpenHuman #WebGL #数字人 #AI渲染 #开源