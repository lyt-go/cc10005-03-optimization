"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ConnectorEntry(BaseModel):
    """数据连接器明细结构。"""

    field_0: str | None = None  # 连接器编号
    field_1: str | None = None  # 协议类型
    field_2: str | None = None  # 目标端点
    field_3: str | None = None  # 认证参数
    field_4: str | None = None  # 重连次数
    field_5: str | None = None  # 心跳间隔
    field_6: str | None = None  # 数据编码
    field_7: str | None = None  # 超时阈值

class ProxypoolEntry(BaseModel):
    """代理实例明细结构。"""

    field_0: str | None = None  # 实例编号
    field_1: str | None = None  # 代理地址
    field_2: str | None = None  # 代理端口
    field_3: str | None = None  # 匿名等级
    field_4: str | None = None  # 出站地域
    field_5: str | None = None  # 响应毫秒
    field_6: str | None = None  # 存活检测时间
    field_7: str | None = None  # 分配权重

class DeepcrawlEntry(BaseModel):
    """爬虫配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 种子URL
    field_2: str | None = None  # 最大深度
    field_3: str | None = None  # 同域约束
    field_4: str | None = None  # 路径包含规则
    field_5: str | None = None  # 路径排除规则
    field_6: str | None = None  # 并发线程数
    field_7: str | None = None  # 断点续爬

class JsrenderEntry(BaseModel):
    """渲染配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 目标URL
    field_2: str | None = None  # 浏览器类型
    field_3: str | None = None  # 渲染等待秒
    field_4: str | None = None  # 滚动次数
    field_5: str | None = None  # 点击选择器
    field_6: str | None = None  # 页面等待条件
    field_7: str | None = None  # 截屏开关

class ParserEntry(BaseModel):
    """解析模板明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 目标字段数
    field_2: str | None = None  # XPath表达式
    field_3: str | None = None  # 正则匹配式
    field_4: str | None = None  # 类型转换规则
    field_5: str | None = None  # 默认填充值
    field_6: str | None = None  # 多值分隔符
    field_7: str | None = None  # 嵌套结构深度

class DatacleanEntry(BaseModel):
    """去噪规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # HTML标签清理
    field_3: str | None = None  # 特殊字符过滤
    field_4: str | None = None  # 空白规整模式
    field_5: str | None = None  # 长度截断阈值
    field_6: str | None = None  # 编码纠错
    field_7: str | None = None  # 敏感词脱敏

class FormatterEntry(BaseModel):
    """转换器明细结构。"""

    field_0: str | None = None  # 转换器编号
    field_1: str | None = None  # 输入格式
    field_2: str | None = None  # 输出格式
    field_3: str | None = None  # 字段映射表
    field_4: str | None = None  # 日期格式模板
    field_5: str | None = None  # 数值精度
    field_6: str | None = None  # 嵌套展平层数
    field_7: str | None = None  # 空值输出策略

class DedupengineEntry(BaseModel):
    """去重引擎明细结构。"""

    field_0: str | None = None  # 引擎编号
    field_1: str | None = None  # 去重字段组
    field_2: str | None = None  # 哈希算法
    field_3: str | None = None  # 布隆过滤器大小
    field_4: str | None = None  # 误判容忍率
    field_5: str | None = None  # 滑动窗口天
    field_6: str | None = None  # 跨批次去重
    field_7: str | None = None  # 相似度阈值

class ThrottleEntry(BaseModel):
    """限速规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标域组
    field_2: str | None = None  # 初始速率
    field_3: str | None = None  # 最大速率
    field_4: str | None = None  # 加速因子
    field_5: str | None = None  # 减速因子
    field_6: str | None = None  # 错误率阈值
    field_7: str | None = None  # 降速恢复间隔

class CaptchaEntry(BaseModel):
    """验证码策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 验证码类型
    field_2: str | None = None  # 识别服务商
    field_3: str | None = None  # 识别超时秒
    field_4: str | None = None  # 重试次数上限
    field_5: str | None = None  # 降级策略
    field_6: str | None = None  # 手动打码开关
    field_7: str | None = None  # 打码等待队列

class MonitorEntry(BaseModel):
    """监控面板明细结构。"""

    field_0: str | None = None  # 面板编号
    field_1: str | None = None  # 监控指标集
    field_2: str | None = None  # 采样间隔秒
    field_3: str | None = None  # 趋势窗口分
    field_4: str | None = None  # 异常检测方法
    field_5: str | None = None  # 告警触发条件
    field_6: str | None = None  # 通知接收组
    field_7: str | None = None  # 自动降级开关

class ExporttaskEntry(BaseModel):
    """分发任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 数据源标识
    field_2: str | None = None  # 目标系统
    field_3: str | None = None  # 传输协议
    field_4: str | None = None  # 压缩格式
    field_5: str | None = None  # 分片大小MB
    field_6: str | None = None  # 加密开关
    field_7: str | None = None  # 校验方式

class SeedmgrEntry(BaseModel):
    """URL种子明细结构。"""

    field_0: str | None = None  # 种子编号
    field_1: str | None = None  # 种子URL
    field_2: str | None = None  # 发现来源
    field_3: str | None = None  # 发现时间
    field_4: str | None = None  # 预计数据量
    field_5: str | None = None  # 分类标签
    field_6: str | None = None  # 优先级
    field_7: str | None = None  # 抓取截止日期

class SitemapEntry(BaseModel):
    """站点描述明细结构。"""

    field_0: str | None = None  # 站点编号
    field_1: str | None = None  # 站点域名
    field_2: str | None = None  # robots规则
    field_3: str | None = None  # sitemap地址
    field_4: str | None = None  # 页面模板路径
    field_5: str | None = None  # 翻页参数名
    field_6: str | None = None  # 站点字符编码
    field_7: str | None = None  # 最近探测时间

class CookiejarEntry(BaseModel):
    """会话凭证明细结构。"""

    field_0: str | None = None  # 凭证编号
    field_1: str | None = None  # 所属站点
    field_2: str | None = None  # 登录方式
    field_3: str | None = None  # Cookie内容哈希
    field_4: str | None = None  # 创建时间
    field_5: str | None = None  # 过期时间
    field_6: str | None = None  # 刷新策略
    field_7: str | None = None  # 绑定代理节点

class HealthcheckEntry(BaseModel):
    """健康报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 采集器名称
    field_2: str | None = None  # CPU占用率
    field_3: str | None = None  # 内存占用MB
    field_4: str | None = None  # 网络IO速率
    field_5: str | None = None  # 活跃连接数
    field_6: str | None = None  # 错误队列长度
    field_7: str | None = None  # 检查时间戳

class SnapshotEntry(BaseModel):
    """数据快照明细结构。"""

    field_0: str | None = None  # 快照编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 快照时间
    field_3: str | None = None  # 采集行数
    field_4: str | None = None  # 去重后行数
    field_5: str | None = None  # 新增行数
    field_6: str | None = None  # 变更行数
    field_7: str | None = None  # 快照文件路径

class AudittrailEntry(BaseModel):
    """审计记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 操作类型
    field_2: str | None = None  # 操作对象
    field_3: str | None = None  # 操作人
    field_4: str | None = None  # 操作时间
    field_5: str | None = None  # 操作IP
    field_6: str | None = None  # 变更详情
    field_7: str | None = None  # 操作结果
