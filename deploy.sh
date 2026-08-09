#!/usr/bin/env bash
# ============================================================================
# Noita RAG MCP server - Linux 一键部署脚本
# 用法(在服务器上以 root 或 sudo 执行):
#   sudo bash deploy.sh
# 可选:
#   MCP_TOKEN=你的密钥 sudo bash deploy.sh   # 启用 Bearer token 鉴权(推荐,防他人盗用额度)
#   PORT=9000 sudo bash deploy.sh            # 自定义端口(默认 8765)
# ============================================================================
set -euo pipefail

PORT="${PORT:-8765}"
TOKEN="${MCP_TOKEN:-}"
DOMAIN="${DOMAIN:-}"   # 可选: 已有域名时填,会提示配置反代

echo "==> [1/8] 检查系统"
if [ "$(id -u)" -ne 0 ]; then
  echo "错误: 请用 root 或 sudo 运行" >&2
  exit 1
fi

echo "==> [2/8] 安装依赖 (git, git-lfs, python3, pip)"
if command -v apt-get >/dev/null 2>&1; then
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -qq
  apt-get install -y -qq git git-lfs python3 python3-pip python3-venv >/dev/null
elif command -v yum >/dev/null 2>&1; then
  yum install -y -q git git-lfs python3 python3-pip >/dev/null
else
  echo "警告: 未识别的包管理器,请手动安装 git / git-lfs / python3 / pip" >&2
fi
git lfs install >/dev/null 2>&1 || true

echo "==> [3/8] 克隆仓库(含 LFS 索引,约 200MB,视网速稍等)"
REPO_DIR=/opt/noita-wiki-zh
if [ ! -d "$REPO_DIR/.git" ]; then
  git clone https://github.com/a1113622001/noita-wiki-zh.git "$REPO_DIR"
fi
cd "$REPO_DIR"
git lfs pull >/dev/null 2>&1 || true
git pull --ff-only >/dev/null 2>&1 || true

echo "==> [4/8] 安装 Python 依赖 (numpy, mcp)"
python3 -m venv "$REPO_DIR/.venv" 2>/dev/null || true
if [ -x "$REPO_DIR/.venv/bin/pip" ]; then
  PIP="$REPO_DIR/.venv/bin/pip"
else
  PIP=pip3
fi
$PIP install -q --upgrade pip numpy mcp 2>/dev/null || pip3 install -q --upgrade pip numpy mcp

echo "==> [5/8] 配置 SiliconFlow API key"
ENV_FILE=/etc/noita-rag.env
if [ ! -f "$ENV_FILE" ] && [ -z "${SILICONFLOW_API_KEY:-}" ]; then
  read -r -p "请输入 SiliconFlow API key(https://siliconflow.cn 免费申请): " KEY_IN
  if [ -z "$KEY_IN" ]; then
    echo "错误: 未提供 API key,RAG 无法工作(可稍后编辑 $ENV_FILE 补填)" >&2
    KEY_IN=""
  fi
  printf 'SILICONFLOW_API_KEY=%s\n' "$KEY_IN" > "$ENV_FILE"
  chmod 600 "$ENV_FILE"
fi
# 若 config.json 不存在则从模板创建(本地 key 优先)
if [ ! -f "$REPO_DIR/rag/config.json" ]; then
  cp "$REPO_DIR/rag/config.example.json" "$REPO_DIR/rag/config.json"
  echo "已生成 $REPO_DIR/rag/config.json,如已在环境变量填 key 可留空"
fi

echo "==> [6/8] 注册 systemd 服务"
UNIT=/etc/systemd/system/noita-rag.service
cat > "$UNIT" <<EOF
[Unit]
Description=Noita RAG MCP server (streamable-http)
After=network.target

[Service]
Type=simple
WorkingDirectory=$REPO_DIR/rag
ExecStart=$REPO_DIR/.venv/bin/python $REPO_DIR/rag/mcp_server.py --http --port $PORT
EnvironmentFile=$ENV_FILE
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable noita-rag >/dev/null 2>&1 || true
systemctl restart noita-rag
sleep 2
systemctl --no-pager -l status noita-rag | head -8 || true

echo "==> [7/8] 开放防火墙端口 $PORT"
if command -v ufw >/dev/null 2>&1; then
  ufw allow "$PORT/tcp" >/dev/null 2>&1 || true
elif command -v firewall-cmd >/dev/null 2>&1; then
  firewall-cmd --permanent --add-port="$PORT/tcp" >/dev/null 2>&1 || true
  firewall-cmd --reload >/dev/null 2>&1 || true
else
  iptables -I INPUT -p tcp --dport "$PORT" -j ACCEPT 2>/dev/null || true
fi

echo "==> [8/8] 部署完成"
IP=$(curl -s --max-time 5 https://api.ipify.org 2>/dev/null || hostname -I 2>/dev/null | awk '{print $1}')
echo
echo "================================================================"
echo "  MCP 服务地址: http://$IP:$PORT/mcp"
if [ -n "$TOKEN" ]; then
  echo "  Bearer Token : $TOKEN"
  echo "  (客户端 headers 需带: Authorization: Bearer $TOKEN)"
fi
echo
echo "  ChatBox 接入: 设置 → MCP → 添加自定义 → 远程(http)"
echo "    URL        : http://$IP:$PORT/mcp"
echo "    Headers    : $( [ -n "$TOKEN" ] && echo "{ Authorization: 'Bearer $TOKEN' }" || echo '(可留空)')"
echo "================================================================"
echo
echo "常用命令: systemctl status noita-rag | journalctl -u noita-rag -f"
