# 芝士，與你分享

 一隻專為 "《原神崩鐵討論群》夏洛特亞洲遊戲討論站｜Genshin Impact／Honkai:Star Rail" 設計的機器人

## 結構
```
cheese
├╴cmds → 指令
│ ├╴admin
│ │ ├╴ban.py → 預計 4.1.0 完成
│ │ ├╴black_list.py → 黑名單系統
│ │ ├╴purge.py → 批量刪除訊息
│ │ └╴send_embed.py → 使用檔案發送 embed
│ ├╴guild
│ │ ├╴deleted_mes → 監測刪除訊息
│ │ ├╴intro.py → 錄入 uid、自我介紹及查尋自我介紹功能
│ │ ├╴quest.py → 發送求助訊息
│ │ ├╴suggest.py → 發送建議與反饋
│ │ └╴tmp_channel → 動態語音頻道
│ ├╴member
│ │ ├╴join.py → 偵測成員加入
│ │ └╴leave.py → 偵測成員離開
│ └╴reaction_roles
│ │ ├╴manage.py → 預計 4.1.0 完成
│ │ └╴update.py → 身份組領取
├╴config → 一些設定檔
│ ├╴bot_info.json
│ ├╴channels.json
│ ├╴errors.json
│ ├╴roles.json
│ └╴token.json
├╴core → 一些函式、畫面
│ ├╴classes.py
│ ├╴views.py
│ └╴models.py
└╴main.py → 主函式
```
