请求获取语言 q表示权重
Accept-Language: da, en-gb;q=0.8, en;q=0.7

生成模板
pybabel extract -F babel.cfg -o messages.pot .


创建翻译
pybabel init -i messages.pot -d translations -l zh_Hans_CN

    模板
    msgid "It's %(day)s today"
    填写翻译
    msgstr "今天是%(day)s"


编译出messages.mo

pybabel compile -d translations

更新翻译
pybabel update -i messages.pot -d translations


