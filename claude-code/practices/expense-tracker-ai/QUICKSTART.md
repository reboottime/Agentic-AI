# 🚀 Quick Start Guide

Get your expense tracker running in 3 simple steps!

## Step 1: Install Dependencies

```bash
npm install
```

## Step 2: Start the Development Server

```bash
npm run dev
```

## Step 3: Open in Browser

Navigate to **http://localhost:3000**

---

## First Steps in the App

### 1. Add Your First Expense
- Click the **"Add Expense"** tab
- Fill in the form:
  - Date: Today (pre-filled)
  - Amount: e.g., 25.50
  - Category: Choose one (e.g., Food)
  - Description: e.g., "Lunch at cafe"
- Click **"Add Expense"**

### 2. View Your Dashboard
- Click the **"Dashboard"** tab
- See your spending summary and charts

### 3. Manage Your Expenses
- Click the **"Expenses"** tab
- Use the search and filters
- Edit or delete expenses using the icons

### 4. Export Your Data
- Click **"Export CSV"** in the header
- Open the CSV file in Excel or Google Sheets

---

## Common Commands

```bash
# Development
npm run dev          # Start dev server with hot reload

# Production
npm run build        # Create optimized production build
npm start            # Start production server

# Code Quality
npm run lint         # Run ESLint
```

---

## Troubleshooting

### Port 3000 Already in Use?
```bash
# Kill the process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use a different port
PORT=3001 npm run dev
```

### Dependencies Not Installing?
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Build Errors?
```bash
# Check Node.js version (needs 18+)
node --version

# Update if needed
nvm install 18
nvm use 18
```

---

## Quick Feature Overview

| Feature | Description |
|---------|-------------|
| 📊 Dashboard | View spending summaries and analytics |
| 💸 Add Expenses | Form with validation |
| 🔍 Filter | Search, category, date range filters |
| ✏️ Edit | Click pencil icon on any expense |
| 🗑️ Delete | Click trash icon with confirmation |
| 📤 Export | Download CSV of all expenses |
| 📱 Responsive | Works on mobile, tablet, desktop |

---

## Data Storage

- All data stored in browser **localStorage**
- No server required
- Use **Export CSV** to backup your data regularly

---

## Need Help?

Check the full [README.md](./README.md) for:
- Detailed usage guide
- Complete feature list
- Technical documentation
- Testing checklist

Check [CLAUDE.md](./CLAUDE.md) for:
- Architecture details
- Development guidelines
- Code structure explanation

---

## Tips for Success

✅ **Do:**
- Export your data regularly as backup
- Use descriptive expense descriptions
- Categorize expenses consistently
- Check the dashboard for spending insights

⚠️ **Don't:**
- Clear browser data without exporting first
- Enter negative amounts
- Use future dates for expenses

---

Happy tracking! 💰
