"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import connector as router_connector
from app.routers import proxypool as router_proxypool
from app.routers import deepcrawl as router_deepcrawl
from app.routers import jsrender as router_jsrender
from app.routers import parser as router_parser
from app.routers import dataclean as router_dataclean
from app.routers import formatter as router_formatter
from app.routers import dedupengine as router_dedupengine
from app.routers import throttle as router_throttle
from app.routers import captcha as router_captcha
from app.routers import monitor as router_monitor
from app.routers import exporttask as router_exporttask
from app.routers import seedmgr as router_seedmgr
from app.routers import sitemap as router_sitemap
from app.routers import cookiejar as router_cookiejar
from app.routers import healthcheck as router_healthcheck
from app.routers import snapshot as router_snapshot
from app.routers import audittrail as router_audittrail

ROUTERS = [router_connector, router_proxypool, router_deepcrawl, router_jsrender, router_parser, router_dataclean, router_formatter, router_dedupengine, router_throttle, router_captcha, router_monitor, router_exporttask, router_seedmgr, router_sitemap, router_cookiejar, router_healthcheck, router_snapshot, router_audittrail]
