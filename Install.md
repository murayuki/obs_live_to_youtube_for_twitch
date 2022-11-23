## 重要

所有自動執行都須將前置作業設置完成

`場景`, `來源`, `Twitch 帳號`, `Youtube 帳號` 都務必先登入或設置完成

`Twitch 帳號`,` Youtube 帳號` 務必登入在 腳本使用的 瀏覽器上

---

## 

## 瀏覽器 插件安裝

請下載 [Twitch-Theater](https://github.com/murayuki/obs_live_to_youtube_for_twitch/tree/main/Twitch-Theater "Twitch-Theater") 放在不易刪除的目錄

針對不同瀏覽器 僅限 chromium 核心 或 chrome 能夠安裝

大多都是 `擴充功能` > `載入未封裝項目` > 選擇下載後的 Twitch-Theater 目錄即可

---

## OBS 安裝

`Python` 設定 請到 [Download Python | Python.org](https://www.python.org/downloads/) 下載 並安裝

`工具` > `腳本` > `Python 設置` 上方安裝後的 `Python`路徑

`OBS 安裝路徑`

`\obs-studio\data\obs-plugins\frontend-tools\scripts`

將下載後的 [obs_py_script](https://github.com/murayuki/obs_live_to_youtube_for_twitch/tree/main/obs_py_script "obs_py_script") 資料夾內的腳本放到此路徑中
接下來到 `工具` > `腳本` > `+` > 選擇 `autoLive.py` 並將各設定填寫完成

重啟 OBS 即可, 想知道是否有執行可以至
`工具` > `腳本` > `指令稿紀錄` 查看執行結果
