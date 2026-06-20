#!/bin/zsh

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PORT="$(python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1]); s.close()')"
URL="http://127.0.0.1:${PORT}/university-logo-grid.html"

cd "$ROOT_DIR"

python3 -m http.server "$PORT" --bind 127.0.0.1 >/tmp/nura-logo-canvas-server.log 2>&1 &
SERVER_PID=$!

cleanup() {
  kill "$SERVER_PID" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

sleep 0.6
open "$URL"

echo "NURA Logo Canvas"
echo "$URL"
echo ""
echo "이 창을 닫으면 로컬 서버가 종료됩니다."

wait "$SERVER_PID"
