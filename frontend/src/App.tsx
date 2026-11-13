import { useState } from 'react'
import { Link, Route, Routes } from 'react-router-dom'

import Overview from './views/Overview'
import ConnectorView from './views/connector'
import ProxypoolView from './views/proxypool'
import DeepcrawlView from './views/deepcrawl'
import JsrenderView from './views/jsrender'
import ParserView from './views/parser'
import DatacleanView from './views/dataclean'
import FormatterView from './views/formatter'
import DedupengineView from './views/dedupengine'
import ThrottleView from './views/throttle'
import CaptchaView from './views/captcha'
import MonitorView from './views/monitor'
import ExporttaskView from './views/exporttask'
import SeedmgrView from './views/seedmgr'
import SitemapView from './views/sitemap'
import CookiejarView from './views/cookiejar'
import HealthcheckView from './views/healthcheck'
import SnapshotView from './views/snapshot'
import AudittrailView from './views/audittrail'

const navItems = [{ label: "运营概览", path: "/" }, { label: "连接器管理", path: "/connector" }, { label: "代理池管理", path: "/proxypool" }, { label: "深度爬取", path: "/deepcrawl" }, { label: "JS渲染采集", path: "/jsrender" }, { label: "字段解析器", path: "/parser" }, { label: "数据去噪", path: "/dataclean" }, { label: "格式转换", path: "/formatter" }, { label: "采集去重", path: "/dedupengine" }, { label: "动态限速", path: "/throttle" }, { label: "验证码处理", path: "/captcha" }, { label: "采集监控", path: "/monitor" }, { label: "数据分发", path: "/exporttask" }, { label: "种子管理", path: "/seedmgr" }, { label: "站点地图", path: "/sitemap" }, { label: "Cookie管理", path: "/cookiejar" }, { label: "采集器健康", path: "/healthcheck" }, { label: "采集快照", path: "/snapshot" }, { label: "操作审计", path: "/audittrail" }]

export default function App() {
  const [operator] = useState('值班管理员')

  return (
    <div className="app-shell">
      <aside className="app-side">
        <h1 className="app-title">多源异构数据接入引擎</h1>
        <nav className="nav-list">
          {navItems.map((item) => (
            <Link key={item.path} to={item.path} className="nav-item">
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="app-main">
        <header className="app-head">
          <span className="head-desc">面向多源异构数据接入、智能代理调度、动态限速、爬虫深度管理、数据去噪、格式转换与采集质量监控的数据接入工程管理平台。</span>
          <span className="head-user">当前值班：{operator}</span>
        </header>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/connector" element={<ConnectorView />} />
          <Route path="/proxypool" element={<ProxypoolView />} />
          <Route path="/deepcrawl" element={<DeepcrawlView />} />
          <Route path="/jsrender" element={<JsrenderView />} />
          <Route path="/parser" element={<ParserView />} />
          <Route path="/dataclean" element={<DatacleanView />} />
          <Route path="/formatter" element={<FormatterView />} />
          <Route path="/dedupengine" element={<DedupengineView />} />
          <Route path="/throttle" element={<ThrottleView />} />
          <Route path="/captcha" element={<CaptchaView />} />
          <Route path="/monitor" element={<MonitorView />} />
          <Route path="/exporttask" element={<ExporttaskView />} />
          <Route path="/seedmgr" element={<SeedmgrView />} />
          <Route path="/sitemap" element={<SitemapView />} />
          <Route path="/cookiejar" element={<CookiejarView />} />
          <Route path="/healthcheck" element={<HealthcheckView />} />
          <Route path="/snapshot" element={<SnapshotView />} />
          <Route path="/audittrail" element={<AudittrailView />} />
        </Routes>
      </main>
    </div>
  )
}
