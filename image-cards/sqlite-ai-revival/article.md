被骂多年的数据库，凭什么在大模型圈翻红

提到SQLite，很多老开发会想起那些被锁表、无法高并发的黑历史。但最近它在AI圈火得不行——从本地大模型到Agent框架，几乎都在用它。

1️⃣ AI四大场景完美踩中✅

本地化与边缘AI兴起：Ollama、Llama.cpp等端侧模型满天飞，开发者不想把所有东西都塞云端，单文件零配置的SQLite成了存聊天记录和知识库的不二之选。

向量检索轻量化：sqlite-vec等扩展让SQLite直接做RAG向量搜索，个人知识库和桌面AI应用不再需要部署Milvus、Qdrant这套重型架构。

Agent状态管理：LangGraph、CrewAI等框架用SQLite做checkpointing，ACID事务保数据不丢。

云端分布式：Turso/libSQL把SQLite带到边缘和全球分发，打破单机限制。

2️⃣ 过去为啥被骂？🤔

传统Web场景下，几十并发写入同一个SQLite就Database is locked；扩展性差；无主从复制。云原生时代这些痛点被放大，就有了讨伐浪潮。

3️⃣ AI时代场景变了 🔄

单用户/轻并发是主流：桌面客户端、浏览器插件写冲突极低。

开发效率至上：原型阶段import sqlite3一行开干，谁也不想花半天配Postgres+Docker。

本地优先：隐私诉求推动数据不出机器，SQLite天然契合。

4️⃣ 生态已经跟上 🚀

sqlite-vec成为向量检索新主流；Turso拿到融资推分布式；LangGraph默认推荐SqliteSaver；Ollama和Llama.cpp官方就用SQLite存embeddings和聊天历史。

5️⃣ 但它真成万能了吗？❄️

单机仍是单机，写入吞吐天花板在那；复杂查询不如PG，多用户高并发别硬上。它只是找到了自己的生态位，不是要取代Postgres。

总结: SQLite不是变强了，是AI时代本地化、Agent化需求恰好需要它这种"够用就好、零运维、离线友好"的选手。评论区聊聊👇

#SQLite #AI #大模型 #开发者
