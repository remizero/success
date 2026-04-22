#!/usr/bin/env bash

set -e

# ==========================================
# Colors
# ==========================================
GREEN="\033[0;32m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m"

print()   { echo -e "${BLUE}➜${NC} $1"; }
success() { echo -e "${GREEN}✔${NC} $1"; }
warn()    { echo -e "${YELLOW}⚠${NC} $1"; }
error()   { echo -e "${RED}✖${NC} $1"; }

# ==========================================
# Banner (branding light)
# ==========================================
echo ""
echo -e "${BLUE}⚡ Success Framework Quickstarter${NC}"
echo ""

# ==========================================
# Resolve paths (clave absoluta)
# ==========================================
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SUCCESS_ROOT="$( cd "$SCRIPT_DIR/../../../" && pwd )"
PROJECT_ROOT="$( pwd )"

# ==========================================
# Validate input
# ==========================================
APP_NAME=$1

if [ -z "$APP_NAME" ]; then
  error "Usage: ./setup.sh <app_name>"
  exit 1
fi

TARGET_DIR="$PROJECT_ROOT/$APP_NAME"

if [ -d "$TARGET_DIR" ]; then
  error "Directory '$APP_NAME' already exists."
  exit 1
fi

# ==========================================
# Start
# ==========================================
print "Creating app: $APP_NAME"

# ==========================================
# Copy quickstarter template
# ==========================================
print "Copying quickstarter template..."

rsync -av \
  --exclude='setup.sh' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='examples' \
  "$SCRIPT_DIR/" "$TARGET_DIR" > /dev/null

success "Template ready"

# ==========================================
# Copy framework
# ==========================================
print "Embedding Success framework..."

rsync -av \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='examples' \
  --exclude='docs' \
  --exclude='README.md' \
  "$SUCCESS_ROOT/" "$TARGET_DIR/success" > /dev/null

success "Framework embedded"

cd "$TARGET_DIR"

# ==========================================
# Environment setup project
# ==========================================
if [ -f "env.example" ]; then
  print "Configuring environment for project..."
  mv env.example success/.env
  success ".env created"
else
  warn "env.example not found"
fi

# ==========================================
# Environment setup application
# ==========================================
if [ -f "apps/example/env.example" ]; then
  print "Configuring environment for application..."
  mv apps/example/env.example apps/example/.env
  success ".env created"
else
  warn "env.example not found"
fi

# (opcional pero pro: versionado interno)
# echo "SUCCESS_ENV=development" >> .env 2>/dev/null || true

# ==========================================
# Python environment
# ==========================================
if command -v python3 &> /dev/null; then
  print "Setting up virtual environment..."

  python3 -m venv venv
  source venv/bin/activate

  success "Virtualenv ready"

  if [ -f "requirements.txt" ]; then
    print "Installing dependencies..."
    pip install --upgrade pip > /dev/null
    pip install -r requirements.txt > /dev/null
    success "Dependencies installed"
  else
    warn "requirements.txt not found"
  fi
else
  warn "python3 not found, skipping venv"
fi

# ==========================================
# Final output
# ==========================================
echo ""
echo -e "${GREEN}🔥 Success app ready!${NC}"
echo ""

echo "Project structure:"
echo "  $APP_NAME/"
echo "    ├── apps/       (your application)"
echo "    ├── success/    (framework snapshot)"
echo "    ├── venv/       (virtual environment)"
echo "    ├── requirements.txt"
echo "    └── wsgi.py"
echo ""

echo "Next steps:"
echo "  cd $APP_NAME"
echo "  source venv/bin/activate"
echo "  python3 wsgi.py"
echo ""

echo "Open in browser:"
echo "  http://localhost:5000"
echo ""

success "Now, you're running Success."
success "Ready to build something awesome."
success "Enjoy building with Success 🚀"
echo ""
