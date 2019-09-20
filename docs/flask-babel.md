生成模板
pybabel extract -F babel.cfg -o messages.pot .


创建翻译
pybabel init -i messages.pot -d translations -l zh_Hans_CN

编译出messages.mo

pybabel compile -d translations

更新翻译
pybabel update -i messages.pot -d translations